# 🦙 Build Your First AI Chatbot with LLaMA 3.3

**Workshop Duration:** 6:00 PM – 7:30 PM
**Format:** Hybrid (In-Person & Remote)
**Hosted by:** Versent

Welcome to our hands-on workshop! In this session, you'll learn how to build a simple command-line chatbot using Python, powered by the open-source LLaMA 3.3 model hosted on Azure AI Foundry.

---

## 🧠 Workshop Objectives

By the end of this workshop, you will:

* Understand the basics of Large Language Models (LLMs) and LLaMA 3.3.
* Set up and configure a Python environment for API interactions.
* Build a CLI-based chatbot that communicates with the LLaMA 3.3 model.
* Learn how to structure prompts and handle responses effectively.

---

## 🛠️ Prerequisites

Before we begin, ensure you have the following:

* **Python 3.7+** installed on your machine.
* A code editor (e.g., VS Code, PyCharm) or access to an online IDE like [Replit](https://replit.com/).
* Internet connectivity to access the hosted LLaMA 3.3 model.
* Your unique **API Key** and **Endpoint URL** provided by the instructor.

---

## 📁 Project Structure

```bash
llama_chatbot/
├── chatbot.py
├── .env
└── requirements.txt
```

---

## 📦 Setup Instructions

1. **Clone the Repository**

   If using Git:

   ```bash
   git clone hhttps://github.com/dylan-mccarthy/llama-hackathon
   ```

   Or download the ZIP file and extract it.

2. **Create and Activate a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   cd llama_chatbot
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the project root directory:

   ```env
   LLAMA_API_URL=https://your-endpoint-url.com/v1/chat/completions
   LLAMA_API_KEY=your-api-key-here
   ```

   Replace `https://your-endpoint-url.com/v1/chat/completions` and `your-api-key-here` with the credentials provided.

---

## 💬 Running the Chatbot

Execute the chatbot script:

```bash
python chatbot.py
```

You should see:

```bash
🤖 Welcome to the LLaMA 3.3 Chatbot! Type 'exit' to quit.
You:
```

Start typing your messages, and the chatbot will respond accordingly.

---

## 🧪 Customization Ideas

* **System Prompt:** Modify the initial behavior of the chatbot by changing the system prompt in the code.

  ```python
  messages = [{"role": "system", "content": "You are a helpful assistant."}]
  ```

* **Adjust Parameters:** Tweak `temperature` and `max_tokens` in the payload to control response creativity and length.

* **Enhance CLI:** Add features like command history, colored text, or even integrate with speech-to-text libraries for voice input.

---

## 🧰 Troubleshooting

* **No Response / Errors:**

  * Ensure your API URL and Key are correctly set in the `.env` file.
  * Check your internet connection.
  * Verify that the LLaMA 3.3 model is deployed and accessible.

* **Module Not Found:**

  * Ensure all dependencies are installed:

    ```bash
    pip install -r requirements.txt
    ```

---

## 📚 Additional Resources

* [LLaMA GitHub Repository](https://github.com/facebookresearch/llama)
* [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
* [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)

---

## 🙌 Acknowledgments

This workshop is proudly presented by [Versent](www.versent.com.au), aiming to inspire and empower the next generation of engineers and technologists.

---

Feel free to reach out if you have any questions or need further assistance during the workshop. Happy coding! 🚀
