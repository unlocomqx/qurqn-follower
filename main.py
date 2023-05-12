import speech_recognition as sr

r = sr.Recognizer()

def callback(recognizer, audio):
    try:
        print("You said " + recognizer.recognize_google(audio, language='ar-AR'))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

with sr.Microphone() as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    r.pause_threshold = 0.5
    t = r.recognize_google(audio, language='ar-AR', show_all=True)
    print(t)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
