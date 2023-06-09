from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Board

def index(request):
    board_list = Board.objects.all()
    return render(request, 'board/index.html',{'board_list':board_list})

def list(request):
    list_all = Board.objects.all()
    return render(request, 'board/list.html',{'list_all':list_all})

def add(request):
    if request.method == 'GET' :
        return render(request, 'board/add.html')
    elif request.method == 'POST':
        title1 =  request.POST['title']
        writer1 =   request.POST['writer']
        content1 =  request.POST['content']
        Board.objects.create(title=title1,writer=writer1,content=content1)
        return HttpResponseRedirect(reverse('board:index'))

def update(request, id):
    if request.method == 'GET' :
        list_id= Board.objects.get(id=id)
        context={
            'list_id' : list_id 
        }
        return render(request, 'board/update.html',context)
    
    elif request.method == 'POST':
        title1 =  request.POST['title']
        writer1 =   request.POST['writer']
        content1 =  request.POST['content']
        Board.objects.filter(id=id).update(title=title1,writer=writer1,content=content1)
        return HttpResponseRedirect(reverse('board:list'))

def detail(request, id):
    list_id = Board.objects.get(id=id)
    list_id.incrementReadCount()
    return render(request, 'board/detail.html',{'list_id':list_id})
def delete(request, id):
    list_id = Board.objects.get(id=id)
    if request.method == 'GET':
        return render(
            request,
            'board/delete.html',
            {'list_id':list_id}
        )
    elif request.method == 'POST':
        list_id.delete()
        return HttpResponseRedirect(reverse('board:list'))
    