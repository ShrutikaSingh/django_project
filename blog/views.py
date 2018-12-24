from django.shortcuts import render
from django.http import HttpResponse  #for importing httpresponse

posts=[
{
'author':'abc',
'title':'blog post 1',
'content':' first post content',
'date_posted':'dec 9,2018'
},
{
'author':'nemo',
'title':'blog post 2',
'content':' second post content',
'date_posted':'dec 10,2018'
},
]


# Create your views here.

#for handling the traffic from homepage,
#return what is to be sent by blog to user
def home(request):
    context={
    'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title':'about'})
