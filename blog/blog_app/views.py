from django.shortcuts import HttpResponse
from .models import User, Post
import time
from .models import User, Post, Comment
import threading
from django.db import transaction  

def run_test_view(request):
    user = User.objects.create(name="Aditya Kolekar", email="aditya@gmail.com")
    start_time = time.time()
    print("Creating a post...")
    Post.objects.create(title="Test Post", content="This is a test post.", writer=user)
    print("Post created successfully.")
    total_time = time.time() - start_time
    print(f"Time taken to create the post: {total_time} seconds")

    return HttpResponse(f"Test complete. It took {total_time:.2f} seconds.")

def create_comment_view(request):
    user = User.objects.create(name="Aditya Kolekar", email="aditya@gmail.com")
    post = Post.objects.create(title="Test Post", content="Test content", writer=user)

    print(f"Main thread: {threading.current_thread().name}")

    Comment.objects.create(commenter=user, content="This is a test comment.", post=post)

    return HttpResponse("Comment successfully created and signal triggered.")

def create_user_view(request):
    try:
        with transaction.atomic():
            User.objects.create(name="Aditya Kolekar", email="aditya@gmail.com")
    except ValueError as e:
        print(f"Error caught: {e}")

    user_count = User.objects.count()
    print(f"Total users in the database: {user_count}")

    return HttpResponse(f"Transaction complete. Total user count: {user_count}")