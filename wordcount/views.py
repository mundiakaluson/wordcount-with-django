from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("This is the about page!")

def count(request):

    fulltext = request.GET['fulltext']

    wordcount = {}

    words = fulltext.split()

    for word in words:
        if word in wordcount:

            wordcount[word] += 1

        else:
            wordcount[word] = 1

    sortedWords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {'fulltext': fulltext, 'count': len(words), 'sortedWords':sortedWords})