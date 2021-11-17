from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import GameForm
from .models import Game


#functional view
# def index(request):
#     game = Game.objects.all().order_by('-id')
#     contex = {
#         'game': game,
#     }
#     return render(request, 'game/index.html', contex)

#class based view
class IndexListView(ListView):
    model = Game
    template_name = 'game/index.html'
    context_object_name = 'game'


# def detail(request, game_id):
#     game_item = Game.objects.get(pk=game_id)
#     contex = {
#         'game_item': game_item,
#     }
#     return render(request, 'game/detail.html', contex)
class DetailView (DetailView):
    model=Game
    template_name='game/detail.html'


def add_game(request):
    form = GameForm(request.POST or None, request.FILES)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('game:index')
    return render(request, 'game/add.html', context=context)


def update_game(request, id):
    game = Game.objects.get(id=id)
    form = GameForm(request.POST or None, files=request.FILES or None, instance=game)
    context = {'game': game,
               'form': form}
    if form.is_valid():
        form.save()
        return redirect('game:index')
    return render(request, 'game/add.html', context=context)


def delete_game(request, id):
    game = Game.objects.get(id=id)
    context = {'game': game
               }
    if request.method=='POST':
        game.delete()
        return redirect('game:index')
    return render(request, 'game/delete.html', context=context)
