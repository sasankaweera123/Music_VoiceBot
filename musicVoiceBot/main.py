import speech_recognition as spr

listener = spr.Recognizer()

try:
    with spr.Microphone() as source:
        print('Hey I am listening...')
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except Exception as e:
    print(e)
