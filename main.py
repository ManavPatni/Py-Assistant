import pyttsx3 #Text to speech convert
import speech_recognition as sr #Speech to text convert

# object creation
engine = pyttsx3.init() 
#Speed of the voice
# setting up new voice rate
engine.setProperty('rate', 125)     
# setting up volume level  between 0 and 1
engine.setProperty('volume',1.0)    
#getting details of current voice
voices = engine.getProperty('voices')   
#changing index, changes voices. 1 for female    
engine.setProperty('voice', voices[1].id)   


engine.say("Hello Subscribers, this is a test")
engine.runAndWait()


engine.stop()