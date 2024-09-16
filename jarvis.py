import pyttsx3  # Text to speech
import datetime # Used to import time 
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5') # It is used to get API to use inbuilt windows voice.
voices= engine.getProperty('voices') # getting details of current voice

engine.setProperty('voice', voices[0].id) # 1 for female voice and 0 for male voice.


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# This code will be used to wish our program user

def wishme():

    hour = int(datetime.datetime.now().hour)
    
    if hour>=4 and hour<12:
        speak("Good Morning!")
        
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")  
    elif hour >= 16 and hour < 20:
        speak("Good Evening!")
        
    else:
        speak("Good Night!")      
        
    speak("Hello I am Jarvis sir, Speed 2.4 gigahertz and memory Five hundred twelve GB , Please tell me how may I assist you")      
   
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()  # takes voice 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Seconds of non-speaking
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        # print(e)     It is not used as it will print error which does not look good.
        print("Say that again please...")   # Say that again will be printed in case of improper voice 
        return "None" # None as a string will be returned
    return query
 

                 
if __name__=="__main_":
   wishme()   
   while True:
#    if 1:    # To run a program once
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) # To read first two sentences.
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  # To open youtube
            
        elif 'open google' in query:
            webbrowser.open("google.com") 
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            
        elif 'play music' in query:
            music_dir = 'A:\\My songs'  # Double slash is used to esacape character
            songs = os.listdir(music_dir)  # It list all files in music folder
            print(songs)  # It prints all songs name.
            os.startfile(os.path.join(music_dir, songs[1]))   # It will open and play first song.
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    # To print time right now.
            print("The time now is:", strTime)
            speak(f"Sir, the time is {strTime}")    
                
        elif 'open code' in query:
            codePath = "A:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
        
        elif 'exit' in query: 
            print("Thank you for using our program, See you again sir")
            speak("Thank you for using our program, See you again sir")  
            exit()