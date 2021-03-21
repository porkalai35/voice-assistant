import pyttsx3
import speech_recognition as sr
import datetime
import calendar
import webbrowser
import wikipedia
import pywhatkit
import pyjokes
import tkinter as tk
from PIL import ImageTk ,Image
import tkinter.font as font

window=tk.Tk()
window.title("Ziva Virtual Assistant")
img=ImageTk.PhotoImage(Image.open ("sample.jpg"),height="200",width="200")
lab=tk.Label(image=img)
lab.pack(padx=5, pady=5, side=tk.BOTTOM) 
all_commands = lambda:[acceptCommands(),Take_query()]

myFont =font.Font(size=40)

button =tk.Button(window,fg='white', bg='#4B0082', activebackground='pink' , text="Start Here", command=all_commands)

button.pack(padx=10, pady=25, side=tk.BOTTOM)
w =tk.Label(text="Hai I'm Ziva \n Your Personal \n  Virtual Assistant", width = "50", height = "50",fg="white",bg="#F52887",font=("Cooper Black", 28)) 

button['font'] = myFont
w.pack(padx=5, pady=5, side=tk.TOP)
 
window.mainloop() 
 

def acceptCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print('recognising....')
            Query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            print(e)
            return 'None'
    return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.date.today()
    speak(calendar.day_name[day.weekday()])

def welcome():
    speak('Welcome user ! I am Ziva your personal assistant How can I help you')
    

def Telltime():
    current_time = datetime.datetime.now().strftime("%I:%M%P")
    output = "your current local time is "+current_time
    speak(output)

def Take_query():
    welcome()
    while (True):
        query = acceptCommands().lower()
        if ' what day is it' in query:
            tellDay()
            continue
        elif 'tell me the time' in query:
             Telltime()
             continue
        elif 'open browser' in query:
             speak("opening google chrome")
             webbrowser.open("www.google.com")
             continue
        elif 'play'in query:
             speak("playing"+query)
             pywhatkit.playonyt(query)
             continue
        elif 'search web' in query:
            pywhatkit.search(query)
            speak("searching result in google!")
            continue
        elif 'from wikipedia' in query:
            speak("checking the wikipedia")
            result = wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            speak(result)
        elif ' joke' in query:             
            speak(pyjokes.get_joke())
            continue
        elif 'your name' in query:
            speak("I am Ziva")
        elif 'how are you' in query:
            speak("I am fine , thank you , what about you")
        elif 'good bye' in query:
            speak("Good bye! , thank you")
        elif 'good morning' in query:
            speak("Good Morning")   
        elif 'good evening' in query:
            speak("Good Evening")    
        elif 'good afternoon' in query:
            speak("Good Afternoon")
        elif 'good night' in query:
            speak("Good Night , Take care , have a sweet dreams!!")      
            exit()

if __name__ == '__main__':
    Take_query()

