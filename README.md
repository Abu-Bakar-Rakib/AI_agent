# 🤖 AI Agent – Powered by LLaMA 3.1 (Groq)

A simple AI Agent built with **Streamlit** and **LangChain**, powered by **LLaMA 3.1 on Groq**.
Users can enter their **Groq API Key** to interact with the model and ask any question directly from the web interface.

## 🚀 Demo

🔗 Live App: [AI Agent (Streamlit)](https://aiagent-dkmjkcy9632mbypgbppnbs.streamlit.app/#ai-agent-powered-by-l-la-ma-3-1-groq)

## ✨ Features

* Interactive chatbot powered by **LLaMA 3.1 (Groq)**
* Simple and lightweight **Streamlit UI**
* Secure API key input (not stored)
* Instant answers with a one-click response button


Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

Install dependencies:

```bash
pip install -r requirements.txt


## 🔑 Usage

1. Get a **Groq API key** from [Groq Console](https://console.groq.com/keys).
2. Paste the key into the input box.
3. Type your question into the text area.
4. Click **Generate Response** and get instant answers.

## 📂 Project Structure

├── main.py             # Streamlit app source code
├── requirements.txt    # Project dependencies
└── README.md           # Documentation



## 📦 Requirements

From `requirements.txt`:

* `streamlit`
* `langchain`
* `langchain-groq`
* `groq`

---

## 🌐 Deployment

You can deploy this app on:

* [Streamlit Cloud](https://streamlit.io/cloud)

For Streamlit Cloud:

1. Push this repo to GitHub.
2. Connect GitHub repo on [Streamlit Cloud](https://share.streamlit.io/).
3. Set up app with `main.py` as entry point.
4. Deploy!

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

