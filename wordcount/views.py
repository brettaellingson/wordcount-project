from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse('Hello')
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    usrText = request.GET['fulltext']
    # print(len(usrText.split()))

    wordCount = len(usrText.split())
    # return render(request,'count.html',{'usrText':usrText,'txtCount':len(txtCount)}

    wordList = usrText.split()

    wordDict = {}

    for word in wordList:
        word = word.replace('.','')
        word = word.replace(',','')
        word = word.replace(';','')
        word = word.replace('\"','')
        word = word.replace(':','')
        word = word.replace(')','')
        word = word.replace('(','')


        print(word)
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html', {'wordCount':wordCount, 'sortedWords':sortedWords,'wordList':wordList})
