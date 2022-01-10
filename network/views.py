from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse

from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json
from itertools import chain


def index(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse("index"))

    else:
        form = CreatePostForm()

    allPosts = Post.objects.order_by("-dateTime").all()
    
    # Pagination
    postsPerPage = Paginator(allPosts, 10)
    page_number = request.GET.get('page')
    page_obj = postsPerPage.get_page(page_number)

    return render(request, "network/index.html", {
        "allPosts": page_obj,
        "form": form
    })

def following(request):
    followedPeople = Follower.objects.filter(user = request.user).values("followingUser")
    posts = Post.objects.filter(user__in = followedPeople)

    return render(request, "network/following.html", {
        "posts": posts
    })

def follow(request, userFollow):
    if "user-follow" in request.POST:
        # Follow user
        userToFollow = User.objects.get(username = userFollow) 
        newFollow = Follower(user = request.user, followingUser = userToFollow)
        newFollow.save()
        return HttpResponseRedirect(reverse("following"))
    elif "user-unfollow" in request.POST:
        # Unfollow user
        userToUnfollow = User.objects.get(username = userFollow)
        removeFollow = Follower.objects.filter(followingUser = userToUnfollow)
        removeFollow.delete()
        return HttpResponseRedirect(reverse("following"))

def profile(request, username):
    profile = User.objects.get(username = username)
    profilePosts = Post.objects.filter(user__username = username).order_by("dateTime")
    followedPeople = Follower.objects.filter(user = request.user).values_list("followingUser", flat = True)
    following = Follower.objects.filter(user = profile).values_list("followingUser", flat=True)
    followers = Follower.objects.filter(followingUser = profile).values_list("user", flat=True)

    # Pagination
    postsPerPage = Paginator(profilePosts, 10)
    page_number = request.GET.get('page')
    page_obj = postsPerPage.get_page(page_number)

    return render(request, "network/profile.html", {
        "profile": profile,
        "profilePosts": page_obj,
        "followedPeople": followedPeople,
        "following": following,
        "followers": followers
    })

def edit(request, postID):
    if request.method == "POST":
        editForm = CreatePostForm(request.POST)

        if editForm.is_valid():
            postToEdit = Post.objects.get(pk = postID)
            postToEdit.content = editForm.cleaned_data["content"]
            postToEdit.save()
            return HttpResponseRedirect(reverse("index"))

    post = Post.objects.get(pk = postID)

    return render(request, "network/edit.html", {
        "editForm": CreatePostForm(initial = {"content": post.content}),
        "editPost": post
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

# API functions
@csrf_exempt
def likePost(request, postID):
    post = Post.objects.get(pk = postID)

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("like") is not None:
            post.like += data["like"]
        post.save()
        return JsonResponse(post.like, safe = False)
        
        
