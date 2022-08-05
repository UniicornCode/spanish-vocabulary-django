import json
import random
import numpy as np
from array import array
from django.shortcuts import render, redirect
from SpanishVocabularyApp.models import City, Category, Word


# Create your views here.


def home(request):
    return render(request, "home.html")


def categories(request):
    queryset = Category.objects.all()
    context = {"categories": queryset}
    return render(request, "categories.html", context)


def visit_spain(request):
    queryset = City.objects.all()
    context = {"cities": queryset}
    return render(request, "visit-spain.html", context)


def vocabulary(request, category="all"):
    if category == "all":
        words = list(Word.objects.all())
        queryset = random.sample(words, 10)
        request.session['list_words'] = make_array(queryset)
    else:
        queryset = Word.objects.filter(category__url_name=category)
        request.session['list_words'] = make_array(queryset)
    context = {"words": queryset}
    return render(request, "vocabulary.html", context)


def quiz_results(request):
    spanish = request.session['spanish_questions']
    answers = request.session['answers']
    color = request.session['color']
    correct_answers = request.session['correct_answers']
    lists = zip(spanish, color, answers, correct_answers)
    context = {"lists": lists}
    return render(request, "quiz-results.html", context)


def quiz(request):
    if request.method == 'POST':
        spanish = request.session['spanish_questions']
        answers = []
        color = []
        correct_answers = []
        for w in spanish:
            correct_answers.append(Word.objects.get(spanish=w).macedonian)
        for s in spanish:
            answers.append(request.POST.get(s))
            if Word.objects.get(spanish=s).macedonian == request.POST.get(s):
                color.append("#00FF7F")
            else:
                color.append("#DC143C")
        request.session['answers'] = answers
        request.session['correct_answers'] = correct_answers
        request.session['color'] = color
        return redirect('quiz-results')
    else:
        words_array = request.session['list_words']
        words = []
        for w in words_array:
            words.append(Word.objects.get(spanish=w))
        questions = random.sample(words, 6)
        request.session['spanish_questions'] = make_array(questions)
        count = ['0', '1', '2', '3', '4', '5']
        get_answers(request, questions, count)
        two_lists = zip(questions, count)
        context = {"two_lists": two_lists}
        return render(request, "quiz.html", context)


def get_answers(request, questions, count):
    for i in count:
        new_list = list(Word.objects.exclude(spanish=questions[int(i)]))
        correct_answer = Word.objects.get(spanish=questions[int(i)])
        answers = random.sample(new_list, 2)
        answers.append(correct_answer)
        random.shuffle(answers)
        request.session[i] = make_array_macedonian(answers)
        request.session.modified = True


def make_array(queryset):
    list_of_words = []
    for w in queryset:
        list_of_words.append(w.spanish)
    return list_of_words


def make_array_macedonian(queryset):
    list_of_words = []
    for w in queryset:
        list_of_words.append(w.macedonian)
    return list_of_words
