# n8n-streamlit-Chatbot-Web-Application

# 🤖 ChatBot Web Application — Streamlit + n8n + Gemini AI

A modern, AI-powered **ChatBot Web App** built using **Streamlit** for the frontend and **n8n (AI Agent + Gemini)** as the backend engine.
This chatbot provides smart, conversational responses with memory support, allowing context-aware interactions similar to real assistants.

---
## 📸 Screenshots

### ChatBot UI

<img width="1428" height="839" alt="Chatbot App UI using streamlit" src="https://github.com/user-attachments/assets/616bd189-1cd0-4179-873d-d1bf336bd859" />


### n8n Workflow

<img width="1274" height="580" alt="Chatbot workflow snapshot" src="https://github.com/user-attachments/assets/93e2e105-e587-4c24-91b9-246288642ed4" />


---

## 🚀 Features

* Real-time chatbot UI built with **Streamlit**
* Backend processing handled by **n8n Webhook + Gemini AI Agent**
* **Memory support** for context-aware conversations
* Clean message UI with user & bot icons
* Fully customizable system instructions
* Runs locally using **VS Code**

---

## 🧩 How It Works

1. User sends a message in Streamlit
2. The app sends the input to an **n8n Webhook**
3. n8n AI Agent (Gemini Model + Memory) processes the conversation
4. n8n returns the response
5. Streamlit displays the chat in a structured UI

---

## 📁 Project Structure

```
.
├── app.py                           # Streamlit frontend
├── requirements.txt                 # Python dependencies
├── chatbot_n8n_workflow.json        # n8n workflow (Webhook + AI Agent)
├── Chatbot UI.png                   # Screenshot of Streamlit app
└── Chatbot workflow.png             # Screenshot of n8n workflow
```

---

## ⚙️ Installation

### 1. Install Python Dependencies

```
pip install -r requirements.txt
```

### 2. Run the Streamlit App

```
streamlit run app.py
```

### 3. n8n Setup

* Import the **Chatbot using n8n+streamlit json file.json**
* Add:

  * Webhook URL
  * Gemini API key
  * Memory node configuration
* Update the Webhook endpoint inside `app.py`

---

## 🛠️ Tech Stack

* **Streamlit** — Frontend UI
* **n8n** — Workflow automation
* **Gemini Chat Model** — AI responses
* **Simple Memory** — Maintains conversation context
* **VS Code** — Development environment

---

## Demo Video

[YouTube]()

## ⭐ Contribute

Pull requests and suggestions are welcome — feel free to enhance the UI, add tools, or integrate more AI features.
