"""
Simple Python Chatbot
Features: greetings, time/date, Wikipedia search, open websites, jokes,
        optional voice input (speech_recognition) and voice output (pyttsx3).

Install:
    pip install wikipedia pyttsx3 SpeechRecognition pyaudio
(Only `wikipedia` is needed for text mode; the rest are optional.)
"""
import datetime
import random
import re
import webbrowser

try:
    import wikipedia
except ImportError:
    wikipedia = None

try:
    import pyttsx3
    engine = pyttsx3.init()
except Exception:
    engine = None

try:
    import speech_recognition as sr
    recognizer = sr.Recognizer()
except Exception:
    sr = None

VOICE_MODE = False

GREETINGS = ["hi", "hello", "hey", "good morning", "good evening"]
JOKES = [
    "Why do Python programmers wear glasses? Because they can't C!",
    "I would tell you a UDP joke, but you might not get it.",
    "Why did the AI go to school? To improve its learning rate!",
]
SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://www.github.com",
    "linkedin": "https://www.linkedin.com",
}


def speak(text):
    print(f"Bot: {text}")
    if VOICE_MODE and engine:
        engine.say(text)
        engine.runAndWait()


def listen():
    if VOICE_MODE and sr:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Bot: Sorry, I couldn't understand. Please repeat.")
            return ""
        except sr.RequestError as e:
            print(f"Bot: Speech service needs internet. Error: {e}")
            return ""
    return input("You: ").lower().strip()


def respond(msg):
    if any(re.search(rf"\b{g}\b", msg) for g in GREETINGS):
        return random.choice(["Hello! How can I help?", "Hey there!", "Hi! What's up?"])
    if "time" in msg:
        return datetime.datetime.now().strftime("It's %I:%M %p.")
    if "date" in msg or "today" in msg:
        return datetime.datetime.now().strftime("Today is %A, %d %B %Y.")
    if "joke" in msg:
        return random.choice(JOKES)
    if msg.startswith("open "):
        name = msg[5:].strip()
        url = SITES.get(name, f"https://www.{name.replace(' ', '')}.com")
        webbrowser.open(url)
        return f"Opening {name}..."
    if msg.startswith(("search ", "wikipedia ", "who is ", "what is ", "explain ", "tell me about ", "define ")):
        query = re.sub(r"^(search|wikipedia|who is|what is|explain|tell me about|define)\s+", "", msg)
        if not wikipedia:
            return "Install the wikipedia package: pip install wikipedia"
        try:
            return wikipedia.summary(query, sentences=2, auto_suggest=False)
        except wikipedia.DisambiguationError as e:
            return f"Too many matches. Be specific, e.g.: {', '.join(e.options[:4])}"
        except wikipedia.PageError:
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            return "Not on Wikipedia, so I opened a Google search instead."
        except Exception as e:
            return f"Wikipedia error (check internet): {e}"
    if msg.startswith(("google ", "web ")):
        query = msg.split(" ", 1)[1]
        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        return f"Searching Google for {query}..."
    if "your name" in msg:
        return "I'm PyBot, your Python assistant."
    if "help" in msg:
        return ("Try: 'time', 'date', 'joke', 'open youtube', "
                "'search python language', 'explain AI', 'google ai news', 'voice on', 'voice off', 'bye'.")
    return "Sorry, I didn't get that. Type 'help' to see what I can do."


def main():
    global VOICE_MODE
    speak("Hi! I'm PyBot. Type 'help' for commands, 'bye' to exit.")
    while True:
        msg = listen()
        if not msg:
            continue
        if msg in ("bye", "exit", "quit"):
            speak("Goodbye!")
            break
        if msg == "voice on":
            try:
                import pyaudio  # noqa: F401
            except ImportError:
                speak("PyAudio is missing, so the microphone can't work.")
                continue
            if sr and engine:
                VOICE_MODE = True
                speak("Voice mode on.")
            else:
                speak("Install SpeechRecognition and pyttsx3 first.")
            continue
        if msg == "voice off":
            VOICE_MODE = False
            speak("Voice mode off.")
            continue
        speak(respond(msg))


if __name__ == "__main__":
    main()
