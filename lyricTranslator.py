# Imports the Google Cloud client library
from google.cloud import translate
from googleapiclient.discovery import build

# Imports the PyLrics library
from PyLyrics import *

# Instantiates a client
translate_client = translate.Client()

# Creates service object
google_api_key = 'AIzaSyATZvqk9ImqhEyD6uGvL079-Yyo6XNsNUY'
translate_service = build('translate', 'v2', developerKey=google_api_key)

# The song title and artist
song_title = input("Please enter song title:")
song_artist = input("Please enter song artist:")

# The target languages
language_from = input("What language is this song in?")
language_to = input("What language would you like to translate to?")

# Searches song title on lyrics API
lyrics = PyLyrics.getLyrics(song_artist, song_title).replace('\n','<br>')

# Translates title and lyrics
text_to_translate = song_title + "\n" + lyrics
translation = translate_service.translations().list(source=language_from, target=language_to, q=[song_title, lyrics]).execute()

print(u'Song Title: {}'.format(translation['translations'][0]['translatedText']))
print(u'Lyrics: {}'.format(translation['translations'][1]['translatedText']).replace('<br>', '\n'))
