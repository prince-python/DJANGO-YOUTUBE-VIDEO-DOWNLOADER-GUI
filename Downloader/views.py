from django.shortcuts import render
from pytube import YouTube
from django.contrib import messages

def index(request):
    if request.method== "POST":
        link =  request.POST['link']
        video=YouTube(link)
        stream=video.streams.all()
        st=list(enumerate(stream))
        print(st)
        data={'name':video.title,
              'pic':video.thumbnail_url,
              }
        return  render(request,'index.html',{'data':data,'st':st,'link':link})
        
    else:
        return render(request,'index.html')
        
import os
def download(request):
    stream=request.POST.getlist('course')
    d =  request.POST['d']
    print(d)
    for i in stream:
        a=int(i)
        print(i)    
    video=YouTube(d)
    stream=video.streams.all()
    st=list(enumerate(stream))
    homedir = os.path.expanduser("~")
    location = homedir + '/Downloads'
    stream[a].download(location)
    messages.success(request,"SUCCESSFULLY DOWNLOADED CHECK DOWNLOADS FOLDER")
    return render(request,'index.html')
   