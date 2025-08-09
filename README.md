Project Architecture & Working Process
The AutomataBot is an AI assistant for Automata Theory and Compiler Design. It operates on a three-part architecture that separates the user interface, server logic, and AI intelligence.

1. The Working Process
A user query travels through the system in this sequence:

User Input: You type a message into the chat interface (the Frontend).

Frontend to Backend: Your browser's JavaScript sends the message to the Python Flask server (the Backend).

Backend to AI: The Flask server takes your message, authenticates with your API key, and sends the query to the Google Gemini LLM.

AI Generates Response: The Gemini LLM processes the query and generates a response.

AI to Backend: The AI's response is sent back to your Flask server.

Backend to Frontend: The Flask server sends the AI's response back to your browser.

Frontend Displays: Your browser's JavaScript displays the AI's response in the chat window.

2. Key Technologies Used
Frontend:

HTML, CSS, JavaScript: Used for the user interface, styling, and all browser-side logic.

AJAX (fetch API): Facilitates communication between the frontend and the backend without reloading the page.

Backend:

Python: The programming language for the server.

Flask: A lightweight web framework that creates the server and API endpoint (/chat).

google.generativeai: The Python library for connecting to the Google Gemini API.

flask-cors: A Flask extension that handles cross-origin security, allowing your local HTML file to communicate with the server.

AI Model:

Google Gemini API: The API service that provides access to Large Language Models (LLMs).

gemini-1.5-flash: The specific LLM model chosen for the chatbot, as it is fast, efficient, and available for your account.

GitHub Repository Content
Here is the full content for your project's GitHub repository.

Repository Description
This is the short description that appears on the main repository page.

🤖 AutomataBot: An LLM-Powered Chatbot for Automata Theory & Compiler Design

An AI assistant that uses the Google Gemini API to provide interactive support for concepts in Automata Theory and Compiler Design. It is built with a Python Flask backend and a JavaScript frontend.

README.md
This is the detailed file that provides a complete overview for anyone visiting your project.

🌟 AutomataBot: An LLM-Powered Chatbot for Computer Science
This project is an AI assistant designed to provide interactive support for the fields of Automata Theory and Compiler Design. Built as a practical demonstration of modern AI integration, the bot leverages a Large Language Model (LLM) to offer accurate and instant answers to complex queries.

🚀 Key Features
Intelligent Q&A: The bot uses the Google Gemini API to understand natural language questions and generate accurate, context-aware answers.

Targeted Expertise: It's configured to act as a subject-matter expert in fields of computer science like finite automata, parsing, and computability.

Decoupled Architecture: The system is built on a clear client-server model, ensuring a secure separation between the user interface and the AI's processing logic.

User-Friendly Interface: The simple, web-based frontend provides a familiar chat experience with real-time feedback.

💻 Technologies Used
Frontend:

HTML, CSS, JavaScript: For the user interface and browser-side logic.

AJAX (fetch API): Facilitates asynchronous communication with the backend.

Backend:

Python: The primary programming language.

Flask: A lightweight web framework that handles API requests.

google-generativeai: The official library for connecting to the Google Gemini API.

flask-cors: A Flask extension to manage cross-origin security between the frontend and backend.

⚙️ How to Run the Project
Follow these steps to get a local copy of AutomataBot running on your machine.

Prerequisites
Python 3.6+ and pip

A Google Gemini API key

Step 1: Clone the Repository & Set Up Backend
Clone this repository and navigate to the project directory.

Bash

git clone https://github.com/YourUsername/automata-llm-bot.git
cd automata-llm-bot
Create and activate a Python virtual environment to install the dependencies.

Bash

python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
Install the necessary libraries:

Bash

pip install Flask flask-cors google-generativeai
Step 2: Configure Your API Key (Crucial!)
Important: Never hardcode your API key directly into a public repository. For local use, you can directly place it in the genai.configure() line in app.py.

Python

# In app.py, replace this line:
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# With your key string (for local testing only):
genai.configure(api_key="YOUR_ACTUAL_API_KEY_HERE")
Step 3: Launch the Chatbot
Start the Flask server from your terminal.

Bash

python app.py
Open the index.html file in your project directory using a web browser. The chatbot interface should now be fully functional.
