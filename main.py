import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import wikipedia
import os
import requests
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import random
import subprocess
import time

from ttkthemes import ThemedTk, THEMES
from tkinter import END, ttk
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk,Image
import threading



#Initializing text to speech
engine = pyttsx3.init()
#getting current voice details 
voices = engine.getProperty('voices')
#changing index, changes voices. 1 for female, 0 for male.
engine.setProperty('voice', voices[1].id)
#changing voice speed
engine.setProperty('rate', 130)



def there_exists(terms,query):
    for term in terms:
        if term in query:
            return True

def CommandsList():
    '''show the command to which voice assistant is registered with'''
    os.startfile('commands.txt')




def text_to_speech(text):
   engine.say(text) 
   engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        scrollable_text.insert(END,"Listening.... \n")
        scrollable_text.see(tk.END)
        audio = recognizer.listen(source)
        data = " "
        try:
            data = recognizer.recognize_google(audio)
            scrollable_text.insert(END, "You said: " + data +"\n")  
            scrollable_text.see(tk.END)
        except sr.UnknownValueError:
           scrollable_text.insert(END,"Ruby: Sorry... I could not understand it. Can you repeat it. \n")
           scrollable_text.see(tk.END)
        except sr.RequestError:
            scrollable_text.insert(END,"Error: Please check your internet connection and try again. \n")
            scrollable_text.see(tk.END)
        return data

def number_details():
    scrollable_text.insert(END,"Ruby: Ok. Say a mobile number.\n")
    scrollable_text.see(tk.END)
    engine.say("Ok. Say a mobile number")
    engine.runAndWait()
    number = speech_to_text().lower()
    number = number.replace("plus","+")
    number = number.replace(" ","")
    while True:
        if number == " ":
           scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it. \n")
           scrollable_text.see(tk.END)
           engine.say("Sorry. I could not understand it. Can you repeat it.")
           engine.runAndWait()
           number = number.replace("plus","+")
           number = speech_to_text().lower()
           number = number.replace(" ","")
        elif number != " ":
             break
    try:
        phone_number = phonenumbers.parse(number)
        validater = phonenumbers.is_valid_number(phone_number)
        if validater == True:
            scrollable_text.insert(END,"Ruby: Location of the mobile number is " +geocoder.description_for_number(phone_number,'en'),"\n")
            scrollable_text.see(tk.END)
            engine.say("Location of the mobile number is " +geocoder.description_for_number(phone_number,'en'))
            engine.runAndWait()
            scrollable_text.insert(END,"Ruby: Service provider of the moblie number is "+carrier.name_for_number(phone_number,'en'), "\n")
            scrollable_text.see(tk.END)
            engine.say("Service provider of the moblie number is "+carrier.name_for_number(phone_number,'en'))
            engine.runAndWait()
        else:
            scrollable_text.insert(END,"Ruby: The number you game does not exist please try again. \n")
            scrollable_text.see(tk.END)
            engine.say("The number you game does not exist please try again.")
            engine.runAndWait()
    except:
        return "error"
    
def cointoss():
    return random.choice(["Heads", "Tails"])

def make_note():
    data = datetime.datetime.now()
    file_name = str(data).replace(":","-")+"-notes.txt"
    scrollable_text.insert(END,"Ruby: Ok. say what you want to write in note.\n")
    scrollable_text.see(tk.END)
    engine.say("Ok. say what you want to write in note.")
    engine.runAndWait()
    note = speech_to_text()
    while True:
        if note == " ":
            scrollable_text.insert(END,"Sorry. I could not understand it. Can you repeat it.\n")
            scrollable_text.see(tk.END)
            engine.say("Sorry. I could not understand it. Can you repeat it.")
            engine.runAndWait()
            note = speech_to_text()
        elif note != " ":
            break
    with open(file_name, "w") as f:
        f.write(note)
    subprocess.Popen(["notepad.exe", file_name])
    scrollable_text.insert(END,"Ruby: Ok. I have made a note of that.\n")
    scrollable_text.see(tk.END)
    engine.say("Ok. I have made a note of that.")
    engine.runAndWait()

def mainframe():
    while(True):
            question_asked = speech_to_text().lower()
            if "your name" in question_asked:
                scrollable_text.insert(END,"Assistant: My name is ruby\n")
                scrollable_text.see(tk.END)
                engine.say("My name is ruby")
                engine.runAndWait()
                break
            elif "where are you" in question_asked:
                scrollable_text.insert(END,"Ruby: I am in your computer\n")
                scrollable_text.see(tk.END)
                engine.say("I am in your computer")
                engine.runAndWait()
                break
            elif "time" in question_asked:
                time_now = datetime.datetime.now().strftime("%I%M%p")
                say = str(time_now)
                scrollable_text.insert(END,"Ruby: Current time is: "+ say + "\n")
                scrollable_text.see(tk.END)
                engine.say(time_now)
                engine.runAndWait()
                break
            elif "date" in question_asked:
                date_today = str(date.today())
                scrollable_text.insert(END,"Ruby: Todays date is " + date_today + "\n")
                scrollable_text.see(tk.END)
                engine.say("Todays date is " + date_today)
                engine.runAndWait()
                break
            elif "open" in question_asked:
                if "youtube" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening youtube.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening youtube.")
                    engine.runAndWait()
                    webbrowser.open("https://www.youtube.com/")
                    break
                elif "facebook" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening facebook.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening facebook.")
                    engine.runAndWait()
                    webbrowser.open("https://www.facebook.com/")
                    break
                elif "instagram" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening instagram.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening instagram.")
                    engine.runAndWait()
                    webbrowser.open("https://www.instagram.com/")
                    break
                elif "whatsapp web" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening whatsapp web.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening whatsapp web.")
                    engine.runAndWait()
                    webbrowser.open("https://www.whatsapp.com/")
                    break
                elif "chrome" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening google chrome.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening google chrome")
                    engine.runAndWait()
                    os.startfile("chrome.exe")
                    break
                elif "notepad" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening notepad.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening notepad")
                    engine.runAndWait()
                    os.startfile("notepad.exe")
                    break
                elif "calculator" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening calculater.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening calculater")
                    engine.runAndWait()
                    os.startfile("calc.exe")
                    break
                elif "word" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening microsoft word.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening microsoft word")
                    engine.runAndWait()
                    os.startfile("WINWORD.EXE")
                    break
                elif "excel" in question_asked:
                    scrollable_text.insert(END,"Ruby: Ok opening microsoft excel.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok opening microsoft excel")
                    engine.runAndWait()
                    os.startfile("EXCEL.EXE")
                    break
            elif "train status" in question_asked:
                scrollable_text.insert(END,"Ruby: Say your train number.\n")
                scrollable_text.see(tk.END)
                engine.say("Say your train number")
                engine.runAndWait()
                train_pin = speech_to_text()
                while True:
                    if train_pin == " ":
                        scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                        scrollable_text.see(tk.END)
                        engine.say("Sorry. I could not understand it. Can you repeat it.")
                        engine.runAndWait()
                        train_pin = speech_to_text()
                    elif train_pin != " ":
                        break
                scrollable_text.insert(END,"Ruby: Ok showing you the train status.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok showing you the train status")
                engine.runAndWait()
                webbrowser.open("https://www.railyatri.in/live-train-status/"+train_pin+"?utm_source=lts_dweb_Check_status")
                break
            elif "flight status" in question_asked:
                scrollable_text.insert(END,"Ruby: Say your flight code.\n")
                scrollable_text.see(tk.END)
                engine.say("Say your flight code")
                engine.runAndWait()
                flight_code = speech_to_text().upper()
                flight_code = flight_code.replace(" ","")
                while True:
                    if flight_code == " ":
                        scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                        scrollable_text.see(tk.END)
                        engine.say("Sorry. I could not understand it. Can you repeat it.")
                        engine.runAndWait()
                        flight_code = speech_to_text()
                        flight_code = speech_to_text().upper()
                        flight_code = flight_code.replace(" ","")
                    elif flight_code != " ":
                        break
                scrollable_text.insert(END,"Ruby: Ok showing you the flight status.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok showing you the flight status")
                engine.runAndWait()
                webbrowser.open("https://planefinder.net/flight/"+flight_code)
                break
            elif "search flight" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok.\n")
                engine.say("Ok")
                engine.runAndWait()
                scrollable_text.insert(END,"Ruby: Say your Departure point.\n")
                scrollable_text.see(tk.END)
                engine.say("Say your Departure point")
                engine.runAndWait()
                departure = speech_to_text().lower()
                while True:
                    if departure == " ":
                        scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                        scrollable_text.see(tk.END)
                        engine.say("Sorry. I could not understand it. Can you repeat it.")
                        engine.runAndWait()
                        departure = speech_to_text().lower()
                    elif departure != " ":
                        break
                scrollable_text.insert(END,"Ruby: Say your Arrival Destination.\n")
                scrollable_text.see(tk.END)
                engine.say("Say your Arrival Destination")
                engine.runAndWait()
                arrival = speech_to_text().lower()
                while True:
                    if arrival == " ":
                        scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                        scrollable_text.see(tk.END)
                        engine.say("Sorry. I could not understand it. Can you repeat it.")
                        engine.runAndWait()
                        arrival = speech_to_text().lower()
                    elif arrival != " ":
                        break
                scrollable_text.insert(END,"Ruby: Ok searching flight for you.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok searching flight for you")
                engine.runAndWait()
                webbrowser.open("https://www.yatra.com/flight-schedule/"+departure+"-to-"+arrival+"-flights.html")
                break
            elif "weather" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok. Say your city name.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. Say your city name")
                engine.runAndWait()
                city = speech_to_text().lower()
                url = "https://wttr.in/{}".format(city)
                webbrowser.open(url)
                scrollable_text.insert(END,"Ruby: Ok. You can see weather on your screen.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. You can see weather on your screen.")
                engine.runAndWait()
                break
            elif "number details" in question_asked or "number detail" in question_asked:
                feedback = number_details()
                while True:
                    if feedback == "error":
                        feedback = number_details()
                    elif feedback != "error":
                        break
                break
            elif "search video on youtube" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok. What would you like to search on youtube.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. What would you like to search on youtube.")
                engine.runAndWait()
                youtube_query = speech_to_text()
                while True:
                    if youtube_query == " ":
                       scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                       scrollable_text.see(tk.END)
                       engine.say("Sorry. I could not understand it. Can you repeat it.")
                       engine.runAndWait() 
                       youtube_query = speech_to_text()
                    elif youtube_query != " ":
                        break
                scrollable_text.insert(END,"Ruby: ok searching "+youtube_query+"on youtube.\n")
                scrollable_text.see(tk.END)
                engine.say("ok searching "+youtube_query+"on youtube.")
                engine.runAndWait()
                webbrowser.open("https://www.youtube.com/results?search_query="+youtube_query)
                break
            elif "search on google" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok. What would you like to search on google.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. What would you like to search on google.")
                engine.runAndWait()
                google_query = speech_to_text()
                while True:
                    if google_query == " ":
                       scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                       scrollable_text.see(tk.END)
                       engine.say("Sorry. I could not understand it. Can you repeat it.")
                       engine.runAndWait() 
                       google_query = speech_to_text()
                    elif google_query != " ":
                        break
                scrollable_text.insert(END,"Ruby: ok searching "+google_query+"on google.\n")
                scrollable_text.see(tk.END)
                engine.say("ok searching "+google_query+"on google.")
                engine.runAndWait()
                webbrowser.open("https://www.google.com/search?q="+google_query)
                break
            elif "search on wikipedia" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok. say what you want to search on wikipedia.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. say what you want to search on wikipedia.")
                engine.runAndWait()
                wikipedia_query = speech_to_text()
                while True:
                    if wikipedia_query == " ":
                       scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                       scrollable_text.see(tk.END)
                       engine.say("Sorry. I could not understand it. Can you repeat it.")
                       engine.runAndWait()
                       wikipedia_query = speech_to_text()
                    elif wikipedia_query != " ":
                        break
                scrollable_text.insert(END,"Ruby: Ok. Would you like to see summary or go to the wikipedia page.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. Would you like to see summary or go to the wikipedia page.")
                engine.runAndWait()
                show_output = speech_to_text()
                while True:
                    if show_output == " ":
                       scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                       scrollable_text.see(tk.END)
                       engine.say("Sorry. I could not understand it. Can you repeat it.")
                       engine.runAndWait()
                       show_output = speech_to_text()
                    elif show_output != " ":
                        break
                if "page" in show_output:
                    scrollable_text.insert(END,"Ruby: Ok. Showing you the results.\n")
                    scrollable_text.see(tk.END)
                    engine.say("Ok. Showing you the results.")
                    engine.runAndWait()
                    webbrowser.open("https://en.wikipedia.org/wiki/"+wikipedia_query)
                elif "summary" in show_output:
                    try: 
                        scrollable_text.insert(END,"Ruby: Ok. Creating summary on the topic" + wikipedia_query + "for you.\n")
                        scrollable_text.see(tk.END)
                        engine.say("Ok. Creating summary on the topic" + wikipedia_query + "for you.")
                        engine.runAndWait()
                        scrollable_text.insert(END,"Creating Summary...\n")
                        scrollable_text.see(tk.END)
                        scrollable_text.insert(END,"Ruby: Would you like me to read it out for you?\n")
                        scrollable_text.see(tk.END)
                        engine.say("Would you like me to read it out for you?")
                        engine.runAndWait()
                        response = speech_to_text()
                        while True:
                            if response == " ":
                                scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                                scrollable_text.see(tk.END)
                                engine.say("Sorry. I could not understand it. Can you repeat it.")
                                scrollable_text.see(tk.END)
                                engine.runAndWait()
                                response = speech_to_text()
                            elif response != " ":
                                break
                        if "yes" in response:
                            scrollable_text.insert(END,wikipedia.summary(wikipedia_query),"\n")
                            engine.say(wikipedia.summary(wikipedia_query))
                            engine.runAndWait()
                            break
                        elif "no" in response:
                            scrollable_text.insert(END,wikipedia.summary(wikipedia_query),"\n")
                            break
                    except:
                       scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                       scrollable_text.see(tk.END)
                       engine.say("Sorry. I could not understand it. please try again.")
                       engine.runAndWait()
                       break
            elif "toss" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok")
                engine.runAndWait()
                engine.say(cointoss())
                engine.runAndWait()
                break
            elif "note" in question_asked:
                make_note()
                break
            elif "search location" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok. which location you want to search.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. which location you want to search.")
                engine.runAndWait()
                location = speech_to_text()
                while True:
                    if location == " ":
                        scrollable_text.insert(END,"Ruby: Sorry. I could not understand it. Can you repeat it.\n")
                        scrollable_text.see(tk.END)
                        engine.say("Sorry. I could not understand it. Can you repeat it.")
                        engine.runAndWait()
                        location = speech_to_text()
                    elif location != " ":
                        break
                map_url = "https://www.google.com/maps/place/" + location
                scrollable_text.insert(END,"Ruby: Ok. Showing you the location of "+location+"\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. Showing you the location of "+location)
                engine.runAndWait()
                webbrowser.open(map_url)
                break
            elif "help" in question_asked or "show commands" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok. I think you have stucked somewhere.\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. I think you have stucked somewhere.")
                engine.runAndWait()
                scrollable_text.insert(END,"Ruby: You can operate me by using this commands. Hope this helps you.\n")
                scrollable_text.see(tk.END)
                engine.say("You can operate me by using this commands. Hope this helps you.")
                engine.runAndWait()
                fp = open("commands.txt","r")
                scrollable_text.insert(END,fp.read(),"\n")
                scrollable_text.see(tk.END)
                time.sleep(1.0)
                break
            elif "made you" in question_asked:
                scrollable_text.insert(END,"Ruby: I was created by 3 brillent Developer with the motive of helping mankind.\n")
                scrollable_text.see(tk.END)
                engine.say("I was created by 3 brillent Developer with the motive of helping mankind.")
                engine.runAndWait()
                break
            elif "name of the person who invented you" in question_asked:
                scrollable_text.insert(END,"Ruby: That's a secret i can't tell you.\n")
                scrollable_text.see(tk.END)
                engine.say("That's a secret i can't tell you.")
                engine.runAndWait()
                break
            elif "exit ruby" in question_asked:
                scrollable_text.insert(END,"Ruby: Ok. Bye Bye\n")
                scrollable_text.see(tk.END)
                engine.say("Ok. Bye Bye")
                engine.runAndWait()
                root.destroy()
    

def gen(n):
    for i in range(n):
        yield i

class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        mainframe()

def Launching_thread():
    Thread_ID=gen(1000)
    global MainframeThread_object
    MainframeThread_object=MainframeThread(Thread_ID.__next__(),"Mainframe")
    MainframeThread_object.start()


#tkinter code
if __name__=="__main__":

        root= ThemedTk(themebg=True)
        root.set_theme("black")

        root.geometry("901x400")
        root.resizable(0,0)

        root.title("Py Assistant - Ruby")
        
        scrollable_text=scrolledtext.ScrolledText(root,height=24,width=109,relief='sunken',bd=5,wrap=tk.WORD,bg='#000000',fg='#ffffff')
        scrollable_text.place(x=1,y=1)

        mic_img=Image.open("Mic.png")
        mic_img=mic_img.resize((55,55),Image.ANTIALIAS)
        mic_img=ImageTk.PhotoImage(mic_img)

        Listen_Button=tk.Button(root,image=mic_img,borderwidth=0,activebackground='#2c4557',bg='#2c4557',command=Launching_thread)
        Listen_Button.place(x=430,y=330)

        myMenu=tk.Menu(root)
        m1=tk.Menu(myMenu,tearoff=0) 
        m1.add_command(label='Commands List',command=CommandsList)
        myMenu.add_cascade(label="Help",menu=m1)
        
        root.config(menu=myMenu)
        root.mainloop()
