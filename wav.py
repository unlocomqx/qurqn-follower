from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

fs = 44100  # Sample rate
seconds = 5  # Duration of recording
r = sr.Recognizer()

print("Start recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, recording)  # Save as WAV file

file = sr.AudioFile('output.wav')
with file as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
try:
    r.pause_threshold = 0.5
    t = r.recognize_vosk(audio, language='ar-AR')
    print(t)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
