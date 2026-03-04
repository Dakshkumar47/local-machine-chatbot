# local-machine-chatbot
A chatbot which will run locally on your machine, ensuring no dependency on cloud infrastructure and data privacy.


```markdown
# 🧠 Local Memory Chatbot (Llama 3 + Streamlit)

A privacy-first, locally hosted chatbot application built with Python, Streamlit, and LangChain. This project utilizes [Ollama](https://ollama.com/) to run the Llama 3 large language model entirely on your local machine, meaning zero API costs and complete data privacy.

The app features persistent chat memory, dynamic session state management, and a clean UI for managing multiple conversation threads.

## ✨ Features

* **100% Local Inference:** Powered by Llama 3 via Ollama. No OpenAI or Anthropic API keys required.
* **Persistent Memory:** Conversations are saved locally to a file-based database (`.txt` files) using custom delimiters, allowing you to close the app and resume chats later.
* **Dynamic Sidebar Management:** * Create new distinct chat threads.
  * Switch seamlessly between older conversations.
  * Active chats are dynamically highlighted in the UI using Streamlit session state callbacks.
* **Modern Chat UI:** Human and AI chat bubbles with seamless message streaming and rendering.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM Orchestration:** [LangChain](https://www.langchain.com/) (`langchain-core`, `langchain-community`)
* **Local Model Provider:** [Ollama](https://ollama.com/)
* **Model:** Meta Llama 3 (8B)

## 🚀 Prerequisites

Before running this application, you must have the following installed on your system:
1. **Python 3.8+**
2. **Ollama:** Download and install from [ollama.com](https://ollama.com/download).
3. **Llama 3 Model:** Once Ollama is installed, open your terminal and pull the model by running:
   ```bash
   ollama run llama3

```

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/yourusername/local-memory-chatbot.git](https://github.com/yourusername/local-memory-chatbot.git)
cd local-memory-chatbot

```


2. **Create a virtual environment (Recommended):**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```


3. **Install the required dependencies:**
```bash
pip install -r requirements.txt

```



## 🏃‍♂️ Running the Application

1. Ensure the Ollama app is running in the background on your machine.
2. Start the Streamlit server:
```bash
streamlit run chatbot_app_2.py

```


3. The app will automatically open in your default web browser at `http://localhost:8501`.

## 📁 Project Structure

When you run the app for the first time, it will automatically generate the required directory structure to save your chats safely across any operating system:

```text
├── chatbot_app_2.py        # Main Streamlit application
├── requirements.txt        # Python dependencies
└── nlp/
    └── elevance_skills/
        └── chats_database/ # Auto-generated folder where individual .txt chats are saved

```

## 🔮 Future Enhancements

* Add a "Delete/Clear Chat" functionality.
* Implement custom system prompts to alter the AI's persona.
* Add RAG (Retrieval-Augmented Generation) capabilities to let the bot read local PDFs.

```

***

**Next Steps for your Repo:** Make sure you update the `git clone` link in the README with your actual GitHub username and repository name!

Now that the code is stable, the dependencies are mapped, and the README is written, your project is officially portfolio-ready. Would you like me to help you draft a strong, professional LinkedIn post to show this off to your network and potential recruiters?

```
