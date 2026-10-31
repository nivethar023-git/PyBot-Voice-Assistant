# Python Voice Chatbot

A simple Python chatbot that works in **text mode** and **voice mode**. It can tell the time and date, search Wikipedia and Google, open websites, and tell jokes.

## Features

- Greetings and small talk
- Current time and date
- Wikipedia summaries (`search`, `what is`, `who is`, `explain`, `define`)
- Google search from the chat (`google ai news`)
- Open websites (`open youtube`, `open github`)
- Random programming jokes
- Optional voice input (speech recognition) and voice output (text-to-speech)

## Tech Stack

- Python 3
- `wikipedia`
- `SpeechRecognition` + `PyAudio` (voice input)
- `pyttsx3` (voice output)
- `webbrowser`, `datetime`, `re`, `random` (standard library)

## Installation

```bash
git clone https://github.com/<your-username>/python-voice-chatbot.git
cd python-voice-chatbot
pip install wikipedia
```

For voice mode (optional):

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

> **Note:** `PyAudio` may not install on Python 3.13. Use Python 3.12 for voice mode.

## Usage

```bash
python chatbot.py
```

| Command | What it does |
|---|---|
| `hello` | Greets you |
| `time` / `date` | Shows current time / date |
| `joke` | Tells a joke |
| `open youtube` | Opens the website |
| `search python language` | Wikipedia summary |
| `explain AI` | Wikipedia summary |
| `google ai news` | Google search in browser |
| `voice on` / `voice off` | Toggle voice mode |
| `help` | Lists commands |
| `bye` | Exits |

## Future Improvements

- AI-powered replies using an LLM API
- Web interface with Flask
- Weather and news features

## Author

Nivetha
