import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak the name of the video you want to play:")
    audio = r.listen(source)

try:
    query = r.recognize_google(audio)
    print("You said: " + query)
except sr.UnknownValueError:
    print("Sorry, I could not understand your voice.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = "AIzaSyCa7FCrJQLtEiMYDdVTe9JV6-c7BxfIP-w"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search_video(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=query,
        type="video",
        part="id,snippet",
        maxResults=1
    ).execute()

    video_id = search_response["items"][0]["id"]["videoId"]
    return video_id


import vlc

video_id = search_video(query)
url = "https://www.youtube.com/watch?v=" + video_id

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(url)
media.get_mrl()
player.set_media(media)
player.play()