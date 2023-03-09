import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define the AI's responses
def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")

# Define the AI's commands
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"You said: {command}\n")
    except:
        command = ""
    return command.lower()

def run_command(command):
    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia, ")
        speak(results)
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com/")
    elif "play music" in command:
        speak("Playing music...")
        music_dir = "C:\\Music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}.")
    elif "thank you" in command:
        speak("You're welcome!")
    else:
        speak("Sorry, I didn't understand that command.")

# Run the AI
speak("Initializing...")
greet()
while True:
    command = take_command()
    run_command(command)