from win32com.client import Dispatch
import time
import os
import datetime as dt
import speech_recognition as sr
import webbrowser
from googlesearch.googlesearch import GoogleSearch as gs
speak = Dispatch("SAPI.SpVoice")
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' # path to the google chrome application 
url= "youtube.com"
 
def recog():
    mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"

    sample_rate = 48000

    chunk_size = 2048

    r = sr.Recognizer()
     

    mic_list = sr.Microphone.list_microphone_names()
     

    with sr.Microphone(sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:

        r.adjust_for_ambient_noise(source)
        print "Say Something"
       
        audio = r.listen(source)
             
        try:
            
            text = r.recognize_google(audio)
            print "you said: " + text
            return text
        except:
            print "did not reognize"


def Personal_assist():
    try:
        
        if "hello" in text:
            speak.Speak("hello, How are you?")
           ## time.sleep(1)
            speak.Speak("What can i do for you")

        elif "time" in text:
            date = str(dt.datetime.now())
            speak.Speak("the current date and time is"+date)
        elif "how are you" in text:
            speak.Speak("i am a program so i guess i am the best")
            speak.Speak("thank you for asking")
        elif "what is" in text:
            speak.Speak("hold on yash i am looking for"+text) #insert your name in place of "yash"
            response = gs().search(text)
            speak.Speak("this is what i found")
            for result in response.results:
                print("title"+result.title)

                speak.Speak("title"+result.title)
                speak.Speak("which says that"+results.getText())
        elif "YouTube" in text:
            speak.Speak("hold on yash openinig youtube")
            webbrowser.get(chrome_path).open(url)
    except:
        speak.Speak("sorry i did not understand please try again and help me improve")
        
while True:
    text = recog()
    Personal_assist()
    
    
