from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import *


def addTask(request):
  task = request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')

def mark_as_done(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = True
  task.save()
  return redirect('home')

def mark_as_not_done(request,pk):
  task = get_object_or_404(Task,pk=pk)
  task.is_completed = False
  task.save()
  return redirect('home')