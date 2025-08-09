import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS

app = Flask(__name__) # Initialize Flask app ONCE
CORS(app) # Enable CORS for your frontend ONCE

# Configure your Gemini API key
# *** IMPORTANT: REPLACE "YOUR_ACTUAL_API_KEY_STRING_GOES_HERE" with your actual API key ***
# This line should now correctly use your key string directly.
genai.configure(api_key="AIzaSyCQ383V0YRlPHRfrVXD5HEANLN6d0l3LIo") # Correctly pass your key here

# Initialize the Gemini model with an AVAILABLE model from the list you provided
# We'll use 'models/gemini-1.5-pro' as it's a good general-purpose model.
# Make sure this line is UNCOMMENTED and correctly defines 'model'.
model = genai.GenerativeModel('models/gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Prepare the prompt for the LLM
        # You can make this more sophisticated, e.g., include conversation history
        prompt = f"You are AutomataBot, an expert in Automata Theory and Compiler Design. Provide concise and accurate answers. User query: {user_message}"

        # Call the Gemini API
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,       # Controls creativity (0.0-1.0)
                max_output_tokens=500  # Limits the length of the AI's response
            )
        )

        # Get the text from the response. This handles cases where response.text might be empty.
        if response.candidates:
            ai_response = response.candidates[0].content.parts[0].text
        else:
            ai_response = "I'm sorry, I couldn't generate a response. The AI model might have had an issue."

        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return jsonify({"error": "Failed to get response from AI. Check server logs for details."}), 500

if __name__ == '__main__':
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)