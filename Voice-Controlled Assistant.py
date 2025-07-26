import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    speak("Listening...")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio).lower()
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
    else:
        speak("Sorry, I can't do that yet.")
except:
    speak("Didn't catch that.")
