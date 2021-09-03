import speech_recognition as sr
import time # in order to wait the respond from user it needs to be implemented.
import webbrowser
import playsound
import os
import random
import csv
import pycountry
import requests
from iso3166 import countries
import pandas as pd
import numpy as np
from gtts import gTTS

#Defining Official Country Names

#World Health Organization Dataset
with open('whodata.csv','r') as whofile:
    csvwho_reader = csv.reader(whofile, delimiter = ',') #DELIMITER OLABİLİR
    header = next(csvwho_reader)


"""
#headerwho = ("Name","WHO Region","Cases - cumulative total","Cases - cumulative total per 100000 population","Cases - newly reported in last 7 days","Cases - newly reported in last 7 days per 100000 population","Cases - newly reported in last 24 hours","Deaths - cumulative total","Deaths - cumulative total per 100000 population","Deaths - newly reported in last 7 days","Deaths - newly reported in last 7 days per 100000 population","Deaths - newly reported in last 24 hours")

link = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
datawho = requests.get(link)


with open(whofile,'wb') as f:
    f.write(datawho.content)
f.close()

with open('whodata.csv', mode='w') as whocsv:
    csvwhowriter = csv.writer(whocsv,delimiter=',')

# ECDC Dataset
ecdcfile = "ecdc.csv"
link = 'https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/csv/data.csv'
dataecdc = requests.get(link)

with open(ecdcfile, 'wb') as t:
    t.write(ecdcfile.content)
t.close()

"""
# John Hopkins Dataset
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer()

def record_audio(ask =False):

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry I could not understand that. Can you repeat it again or change the question?')
        except sr.RequestError:
            speak('At this moment I can not help you')
        return voice_data

#Google Text to Speech / Chatbot speaks
def speak(audio_string):
    tts = gTTS(text=audio_string, lang ='en' )
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) +'.mp3' # create mp3 file on the desktop
    tts.save(audio_file) #can be commented out
    playsound.playsound(audio_file)
    print(audio_file) #recording the chatbot and person's speech
    os.remove(audio_file) # can be commented out
###############################################

def respond(voice_data):
    if there_exists(['Hello','Hi','Hey']):
        sayhi = [f"Hello how can I help you?", f"Hello Again! What do you want to learn about Covid19?",f"Hey! Ask me a question on Covid19 I am here to answer it"]
        saylength = greet = sayhi[random.randint(0,len(sayhi)-1)]
        speak(sayhi)

    if there_exists(["what is covid", "what is coronavirus","what is covid19"]):
        speak(f'According to World Health Organization the definition of Covid 19 is like that: Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.')

    ## TODO:

    if  there_exists(['which country has had the most deaths due to covid19','which country has the most deaths due to covid19?','which country has most death due to covid19','which country has the most death number because of covid19']):
        speak('Hey')

    if there_exists(['which country has the most death number','which country has most death number', 'which country has the most death','which country have the most death number','which country have the most death']):
        speak('Hey')
    ########
    if there_exists(['which country has the least death number','which country has least death number', 'which country has the least death','which country have the least death number','which country have the least death']):
        speak('Hey')
    ######## COUNTRY NAME TANIMLA
    if there_exists(['what is the current pandemic situation in']):
        countryname = voice_data.split("in")[-1].strip()
        try:
            if countryname in countries:
                for row in csvwho_reader:
                    if row == countryname:
                        speak('Hey')
                speak(f'According to world health organization, currently at {countryname} there are cases. And also according to ECDC data there are cases.')

        except:
            speak('I could not find the result. Can you try it again?')



    ######### COUNTRY VE DATE TANIMLA
    if there_exists(['how many covid deaths occurred in (country) as of (date)']):
        countryname = voice_data.split("in")[-1].strip()
        if countryname in countries.get():
            speak(f"In {countryname} there are currently")



    if there_exists(["Bye","goodbye","see you","thank you bye","see you later","thanks for your help"]):
        speak(f'Good Bye! Thanks for using Covid19 Chatbot')
        exit()





speak('Hello! My name is Covid 19 Chatbot! What do you want to learn?')

while (1):
    voice_data = record_audio()
    respond(voice_data)
