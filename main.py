import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as web
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'how is alexa' in command:
        talk('hi ilyes, how can i help you')
    elif 'introduce yourself' in command:
        talk("i'm alexa, i'm a digital assistant")
    elif 'who i am' in command:
        talk("you are my boss, Ilyes")
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'did you love me' in command:
        talk('yes i love you so much, ilyes')
    elif 'thank you' in command:
        talk("you're welcome, Ilyes")
    elif 'what i must do right now' in command:
        talk("you must start learning new skills right now")
    else:
        talk('Please say the command again.')


def main():
    path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something ")
 
        audio = r.listen(source)
 
        print("Reconizing Now ... ")
 
 
 
        try:
            dest = r.recognize_google(audio)
            print("You have said : " + dest)
 
            web.get(path).open(dest)
 
        except Exception as e:
            print("Error : " + str(e))
 
 
if __name__ == "__main__":
    main()


while True:
    run_alexa()
