from rest_framework.decorators import api_view
import urllib.parse
import urllib.request
import pygame

from django.http import HttpResponse

@api_view(['GET', 'POST'])
def tts_play(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        txt = request.GET['text']
        convert_textTomp3(txt)
        play_mp3()
        print("done..")
        return HttpResponse('')

    elif request.method == 'POST':
        txt = request.GET['text']
        convert_textTomp3(txt)
        play_mp3()
        print("done..")
        return HttpResponse('')
    
    
def convert_textTomp3(txt):
   
    client_id = "Zeo_nwjkCps3cGq_0LSa"
    client_secret = "jRbn4kxYMw"


    encText = urllib.parse.quote(txt)
    data = "speaker=jinho&speed=0&text=" + encText;
    url = "https://openapi.naver.com/v1/voice/tts.bin"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()

    if(rescode==200):
        print("TTS mp3 저장중")
        response_body = response.read()
        #with open("C:\\Users\\han\\Documents\\IOT\\�꽱�꽌_��湲�\\���옣\\��湲�.mp3", 'wb') as f:
        with open("../test1.mp3", 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)
        
def play_mp3():
    pygame.init()
    pygame.mixer.init()
    
    pygame.mixer.music.load('../test1.mp3')
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        clock.tick(1000)