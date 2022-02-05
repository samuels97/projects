from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all() #getting all posts from database
    return render(request, 'post/index.html', {'posts': posts})

def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id) #get the liked posts
        m = Like(post=likedpost) #create like object
        m.save() #saving it in database
        return HttpResponse("success!") #sending a success response
    else:
        return HttpResponse("Request method is not a GET")

