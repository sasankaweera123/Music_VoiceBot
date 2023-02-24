import pyjokes
import speech_recognition as spr
import pyttsx3
import pywhatkit

listener = spr.Recognizer()
engine = pyttsx3.init()


def broTalk(text):
    engine.say(text)
    engine.runAndWait()


def takeBroCommand():
    try:
        with spr.Microphone() as source:
            print('Hey I am listening...')
            broTalk('Hey I am listening')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bro' in command:
                command = command.replace('bro', '')
                print(command)
    except Exception as e:
        print(e)
    return command


def runBro():
    command = takeBroCommand()
    if 'play' in command:
        song = command.replace('play', '')
        broTalk('playing ' + song)
        print('playing', song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        broTalk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        broTalk('I did not get that,  please repeat it again')


while True:
    runBro()
