from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import NewEntry
from .forms import EntryForm
from events.models import Event

# Create your views here.


def register_new(request):
    if request.method == 'POST':
        event_pk = request.POST.get('pk')
        event = Event.objects.get(pk=event_pk)
    else:
        event = Event.objects.filter(pk=1)
    form = EntryForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.event = event
        instance.save()
        return HttpResponseRedirect('/')


    context = {
        'event': event,
        'form': form,
    }

    return  render(request, 'registration/new.html', context)

