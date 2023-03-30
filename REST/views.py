from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3 
import requests 
from random import randrange
# Create your views here.
