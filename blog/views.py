from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author" : " Kamz",
        'Title': 'Blog Post',
        'Content': 'First Post content',
        'date_posted' :' August 27, 2018 '
            
    },
    {
        "author" : " Panther Pinkest",
        'Title': 'Blog Post 1',
        'Content': '2nd Post content',
        'date_posted' :' August 23, 2018 '          
    },
    
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
        }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'Title' : 'about'})
