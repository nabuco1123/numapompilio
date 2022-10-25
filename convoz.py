import pyttsx3
import speech_recognition as sr
import pywhatkit 


name = 'cafe'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def lisent():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')
                print(rec)

    except:
        pass
    return rec

def run():
    rec = lisent()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)

run()