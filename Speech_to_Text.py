import speech_recognition as sr
AUDIO_FILE= ("harvard.wav")
# use audio file as source

r=sr.Recognizer() # initialize the recognizer

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source) 

#reads the audio file

try:
    print("Audio file Contains " + r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google Speech Recgonition could not understand the audio")
except sr.RequestError :
    print("Couldn't get the results from google Speech Recognition")
