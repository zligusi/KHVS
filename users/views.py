from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import CustomUserLoginForm, CustomUserRegisterForm


def login(request):
    