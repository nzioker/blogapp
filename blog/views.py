from django.shortcuts import render,redirect
from .forms import PostsForm
from .models import Posts
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm


# TODO
# Create a django-admin user to help verify that the post is indeed created and added to the database.

# TODO
# Create a template folder and create_post.html file.

# TODO
# Create a post table. This will be in the form of a class in models.py

# TODO
# Create a Createform in forms.py which will be rendered out in the create_post.html.

# TODO 
# Write logic that will create the post.

# TODO
# Display the posts that have been created.

# This view creates a post
def create_post(request):
    if request.method == 'GET':
        form = PostsForm()
        context = {'form':form}
        return render(request, "blog/create_post.html", context=context)
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('create')
        else:
            return render(request, "blog/create_post.html")


# This view displays the posts from the database        
def display_posts(request):
    articles = Posts.objects.all()
    context = {'articles':articles}
    return render(request, "blog/display_posts.html", context=context)


def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'form':form}
        return render(request, "blog/login.html", context)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('display_posts')    
            else:
                return render(request,'blog/login.html')
    return render(request, "blog/login.html", context)





    