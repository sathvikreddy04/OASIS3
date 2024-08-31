import speech_recognition as sr
import win32com.client
import webbrowser


speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="hi-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(e)
            return "Some Error Occurred. Sorry from Python"

if __name__ == '__main__':
    print('Welcome to Python')
    say("Welcome to Python")
    while True:
        query = takeCommand().lower()
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["github", "https://www.github.com"],
            ["stack overflow", "https://stackoverflow.com"],
            ["twitter", "https://www.twitter.com"],
        ]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "how are you" in query:
            say("I'm doing well! Thank you for asking.")
        elif "who are you" in query:
            say("I am Python, your personal  assistant.")
        elif "what is your name" in query:
            say("My name is Python.")
        elif "stop" in query or "bye" in query:
            say("Goodbye, have a nice day!")
            break

