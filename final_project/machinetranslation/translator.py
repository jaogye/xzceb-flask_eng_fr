import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey="g0u51-XDIGp1Cq150Ln-D75ha5QPAtvpD1r1GURT0ykO"
url="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/95535a59-0052-47c3-8075-fe0e2eab862c"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishtext):
    if englishtext == '':
       return ''
    translation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    frenchtext = translation['translations'][0]['translation'] 
    return frenchtext

def frenchToEnglish(frenchtext):
    if frenchtext == '':
       return ''
    translation = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    englishtext = translation['translations'][0]['translation'] 
    return englishtext
