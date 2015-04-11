import collections
import re

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from pennybags.models import CollectedMarker, Marker


@login_required
def index(request):
    prizes = collections.defaultdict(list)
    collected = collections.Counter()

    for marker_id in CollectedMarker.objects.filter(
            user=request.user).values_list('marker_id', flat=True):
        collected[marker_id] += 1

    for marker in Marker.objects.select_related('prize').order_by('id'):
        prizes[marker.prize].append(marker)

    results = [{
        'prize': prize,
        'markers': [{
            'code': '{}{}'.format(marker.id, prize.id),
            'count': collected[marker.id],
        } for marker in markers],
        'progress': (sum([1 for marker in markers if marker.id in collected]) / float(len(markers))) * 100,
    } for prize, markers in sorted(prizes.items(), key=lambda i: i[0].id)]

    print(results)

    return render(request, 'index.html', {
        'results': results,
    })


@login_required
def collect(request):
    if request.method == 'POST':
        marker_ids = [re.sub(r'\D+', '', m) for m in request.POST.get('marker', '').split(' ')]

        for marker_id in marker_ids:
            try:
                marker = Marker.objects.get(id=marker_id)
            except (Marker.DoesNotExist, ValueError):
                continue

            if request.POST.get('action') == 'remove':
                for cm in CollectedMarker.objects.filter(user=request.user, marker=marker)[:1]:
                    cm.delete()
            else:
                CollectedMarker.objects.create(user=request.user, marker=marker)

    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )

            auth.login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form,
    })
