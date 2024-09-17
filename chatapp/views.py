import json
import requests
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
import os
from openai import AzureOpenAI

# Azure OpenAI API setup
AZURE_OPENAI_ENDPOINT = "https://just-testing-22.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-08-01-preview"
AZURE_OPENAI_KEY = 'fa2ddc31093e4b7ab8abe30874d5cab7'


endpoint = os.getenv("ENDPOINT_URL", "https://just-testing-22.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4-32k")

      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key='fa2ddc31093e4b7ab8abe30874d5cab7',
    api_version="2024-05-01-preview",
)

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        # Parse the incoming request
        data = json.loads(request.body)
        prompt = data.get('prompt', '')
        images = data.get('images', [])

        # Make the request to Azure OpenAI API and stream response
        def stream_response():
            completion = client.chat.completions.create(
                model=deployment,
                messages= [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=800,
                temperature=0.7,
                top_p=0.95,
                stream=True
            )

            for chunk in completion:
                try:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
                except:
                    pass
                    

        return StreamingHttpResponse(stream_response(), content_type='text/plain')

    return render(request, 'index.html')
