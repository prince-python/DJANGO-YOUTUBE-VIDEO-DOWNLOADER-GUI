from django.shortcuts import render,HttpResponse
from pytube import YouTube
from django.contrib import messages

def index(request):
    if request.method== "POST":
        try:
            link =  request.POST['link']
            video=YouTube(link)
            stream=video.streams.filter(progressive=True,file_extension='mp4')
            st=list(enumerate(stream))

            data={'name':video.title,
                'pic':video.thumbnail_url,
                }
            return  render(request,'index.html',{'data':data,'st':st,'link':link})
        except: 
            return HttpResponse("<center><h1> link not found go back and try check again</h1></center>")
   
    else:
        return render(request,'index.html')
        
import os
def download(request):
    stream=request.POST.getlist('course')
    d =  request.POST['d']

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
   