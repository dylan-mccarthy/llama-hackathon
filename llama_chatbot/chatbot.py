"""
Ollama Chatbot

This module implements a simple command-line chatbot that uses the Ollama API
to generate responses to user inputs in a conversational format.
"""
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file for secure API credentials storage
load_dotenv()

# Retrieve API configuration from environment variables
# Default to localhost:11434 if not specified in environment
API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1")

# Set up the HTTP headers for content type (Ollama doesn't need auth token)
headers = {
    "Content-Type": "application/json"
}

def chat():
    """
    Implements an interactive chat loop with Ollama using its REST API.
    
    This function manages the conversation state, sends user messages to the API,
    and displays the AI's responses until the user exits.
    """
    # Initialize conversation with a system message to define AI behavior
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    print(f"🤖 Welcome to the Ollama Chatbot ({OLLAMA_MODEL})! Type 'exit' to quit.\n")
    
    while True:
        # Get user input and handle exit commands
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break
        
        # Add user message to conversation history
        messages.append({"role": "user", "content": user_input})
        
        # Prepare the API request payload for Ollama
        payload = {
            "model": OLLAMA_MODEL,     # Specifies which model to use
            "messages": messages,      # Full conversation history
            "stream": False,           # Get complete response, not streaming
            "options": {
                "temperature": 0.7,    # Controls randomness (0.0=deterministic, 1.0=creative)
            }
        }
        
        # Send request to Ollama API
        response = requests.post(API_URL, headers=headers, json=payload)
        
        # Process the API response
        if response.status_code == 200:
            # Extract and display the AI's response - Ollama has different response format
            assistant_message = response.json()["message"]["content"]
            print(f"AI: {assistant_message}\n")
            
            # Add AI response to conversation history for context in next turn
            messages.append({"role": "assistant", "content": assistant_message})
        else:
            # Handle API errors
            print(f"Error: {response.status_code} - {response.text}")
            break

if __name__ == "__main__":
    chat()
