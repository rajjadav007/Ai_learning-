import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("hey sir how may i help you")
    while True:

        r=sr.Recognizer()
        with sr.Microphone() as source:
            print ("say something")
            audio=r.listen(source)

            
        print ("recognizing...")
        try:
            command=r.recognize_google(audio)
            print (command)
        except sr.UnknownValueError:
            print ("sphinx could not understand audio")
        except sr.RequestError as e:
            print("sprinx error;{0}".format(e))