Objective
Create a Python application that:
• Interacts with the OpenAI API.
• Incorporates a simple retrieval mechanism to enhance responses.
• Produces structured outputs in JSON format.
• Demonstrates effective coding practices and problem-solving skills.
Task Description
You are required to create a Python script that performs the following:
1. Command-Line Input
• Accepts a user’s question as a command-line argument when running the script.
2. OpenAI API Integration
• Sets up an OpenAI client using the OpenAI Python library.
• Configures a system prompt that instructs the language model to respond in Yoda’s
speaking style.
3. Simple Retrieval Mechanism
• Reads from a provided text corpus file containing information about StarWars characters
(star_wars_corpus.txt).
• Searches the corpus for relevant information based on the user’s question.
• Extracts the most relevant snippet to include in the prompt to the language model,
enhancing the accuracy of the response.
4. Structured JSON Output
• Outputs a JSON object containing:
{
" user_prompt ": "The user ’s original question ",
" retrieved_context ": "The text retrieved from the corpus ",
" system_response ": "The language model ’s response in Yoda ’s
,→ style "
}
5. Error Handling
• Includes basic error handling for situations such as:
– Missing or incorrect command-line arguments.
– File not found errors when accessing the corpus.
– API request failures or exceptions.
– Empty or null responses.
Specific Task Details
Question to Test
Use the script to answer the following question:
"Who is Luke Skywalker’s father?"
Expected Behavior
• The script should retrieve relevant information from the corpus about Luke Skywalker’s father.
• It should then query the OpenAI API with an appropriate prompt that includes:
– The system prompt to adopt Yoda’s speaking style.
– The retrieved context to inform the language model.
•Finally, it should output the response in Yoda’s speaking style within the structured JSON.
Resources Provided
1. OpenAI API Key
• A temporary OpenAI API key will be provided to you for this task.
• Important: Handle the API key securely (e.g., use an environment variable). Do not
hardcode it into your script.
• Make use of the LLM model: “Gpt4o”
2. Text Corpus File (star_wars_corpus.txt)
• Contains information about Star Wars characters.
• Example Content:
Luke Skywalker is a Jedi Knight and the son of Anakin Skywalker ,
,→ who became Darth Vader .
Darth Vader , originally Anakin Skywalker , is a central character
,→ in the Star Wars universe .
Princess Leia is Luke Skywalker ’s twin sister .
Han Solo is a smuggler who becomes involved in the Rebel Alliance .
