from django.shortcuts import render # will render the html templates

# Create your views here.


posts = [
    {
        "author": "Robin",
        "title": "First Blog Post",
        "date": "june 27th 2020",
        "content": "This is the content of post 1"

    },
    {
        "author": "Lennart",
        "title": "second Blog Post",
        "date": "june 28th 2020",
        "content": "this is the content of post 2"

    }
]


def home(request):

    context = {
        'posts': posts # this posts variable can then be accessed
    }
    return render(request, "blog/home.html", context)

def about(request):
        return render(request, "blog/about.html", {"title": "RMDB about"})



    
