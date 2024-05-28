from django.shortcuts import render
from django.http import JsonResponse

def validate(request):
    return JsonResponse({
        'name' : 'Julian',
        'job' : 'GrupoASD ',
        'courses': [
            {'title': 'Python'},
            {'title': 'Java'},
            {'title': 'BD'},
        ]
    })
















