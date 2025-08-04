# Kira_Teaching_Assistant_Final

Kira is an **AI-powered voice teaching assistant** built using **LiveKit Agents v1**, **Anthropic Claude 3.5**, **Deepgram**, **Resemble TTS**, and various custom tools like **web search and calendar management**.  

Kira listens for **wake words**, logs your conversation, and can answer your questions based on **meeting logs** or real-time queries using integrated tools.  
The agent comes with a **Flask + LiveKit frontend** for testing real-time voice interactions.

---

## 🎯 Features

- **Voice-based AI Teaching Assistant**
  - Warm, conversational, and clear explanations for any topic.
  - Can summarize and explain concepts in simple terms.
- **Wake Word Detection**
  - Responds only when it hears `kira`
- **Meeting Log Integration**
  - Logs all conversations to `meeting_log.txt`.
  - Can reference the full log if you ask a question with a wake word.
- **Built-in Tools**
  - `search_web` → Search the web for answers.
  - `search_youtube` → Find YouTube videos for topics.
  - `add_calendar_event` → Add events to a simple in-memory calendar.
  - `update_calendar_event` → Update events.
  - `remove_calendar_event` → Delete events.
  - `list_calendar_events` → View all scheduled events.

---

## 🗂 Project Structure

Kira_Teaching_Assistant_Final/

│

├── agent.py # Main LiveKit voice agent

├── tools.py # Function tools (web search, calendar, YouTube)

├── prompts.py # AI personality and behavior instructions

├── meeting_log.txt # Logs user messages

├── .env # API keys and LiveKit credentials

└── README.md # Project documentation



---

## ⚡ Requirements

- Python 3.10+  
- Virtual Environment (recommended)  
- LiveKit Agent SDK  
- Git for installing the LiveKit Server SDK

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup Environment

1. Create a `.env` file in the project root:

```env
LIVEKIT_URL=wss://<your-livekit-domain>
LIVEKIT_API_KEY=<your-api-key>
LIVEKIT_API_SECRET=<your-api-secret>

GOOGLE_API_KEY=<optional>
CARTESIA_API_KEY=<optional>
DEEPGRAM_API_KEY=<your-deepgram-key>
RESEMBLE_API_KEY=<your-resemble-key>
OPENAI_API_KEY=<optional>
ANTHROPIC_API_KEY=<your-anthropic-key>


