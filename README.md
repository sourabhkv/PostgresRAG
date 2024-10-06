# PostgresRAG
Implementing RAG on Postgress

Place Finder: Users can search for various places through a search bar. The application uses natural language processing via the Azure OpenAI API to generate SQL queries based on user input, which are then executed on a PostgreSQL database. The results, including details like name, location, and category, are displayed in a user-friendly table. Users can click on a link to view detailed information about each place, including a map view using Azure Maps for location preview.

I have taken data from Azure Maps, currently it has data within bangalore region, can be expanded by adding more data

Interactive Chat: The application features an interactive chat section where users can converse with an AI model. The chat interface supports real-time streaming responses from the Azure OpenAI API (can also be used locally by SLM), providing a dynamic and engaging user experience. Messages from the AI are streamed and appended in real-time, allowing users to interact seamlessly with the chatbot.

comes with a personal chat app also

[Demo](https://bitbangaloreeduin-my.sharepoint.com/:v:/g/personal/1bi21cs147_bit-bangalore_edu_in/ESa6qJHBDF9HkoS6CmtoaOEBIta5c0YvRksyK2yWcwD7Kw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=lrpyvF)
