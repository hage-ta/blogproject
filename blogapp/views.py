from django.shortcuts import render, get_object_or_404, redirect
from .models import GameTip
from .forms import GameTipForm
from django.views.generic.base import TemplateView

# トップページ（IndexView）
class IndexView(TemplateView):
    template_name = 'index.html'

# 攻略情報の一覧表示
def game_list(request):
    games = GameTip.objects.all().order_by('-created_at')  # 登録されているゲームを取得
    return render(request, 'game_list.html', {'games': games})

# 攻略情報の登録
def game_create(request):
    if request.method == 'POST':
        form = GameTipForm(request.POST)
        if form.is_valid():
            form.save()  # フォームのデータを保存
            return redirect('blogapp:game_list')  # リダイレクト先は'blogapp:game_list'として名前付きURLを使う
    else:
        form = GameTipForm()
    
    return render(request, 'game_create.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import GameTip
from django.shortcuts import render

# ゲーム削除
def game_delete(request, pk):
    game = get_object_or_404(GameTip, pk=pk)  # ゲーム情報を取得
    if request.method == 'POST':
        game.delete()  # ゲームを削除
        return redirect('blogapp:game_list')  # 削除後にゲーム一覧ページにリダイレクト
    return render(request, 'game_delete_confirm.html', {'game': game})  # 削除後にゲーム一覧ページにリダイレクト

def game_delete_bulk(request):
    if request.method == 'POST':
        game_ids = request.POST.getlist('game_ids')  # チェックされたゲームのIDを取得
        for game_id in game_ids:
            game = get_object_or_404(GameTip, pk=game_id)
            game.delete()  # ゲームを削除

        return redirect('blogapp:game_list') 

def home(request):
    return render(request, 'index.html') 