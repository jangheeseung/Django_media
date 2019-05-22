from django.shortcuts import get_object_or_404, render, redirect
from .models import Media
from .forms import MediaForm

# Create your views here.
def index(request):
    medias = Media.objects
    return render(request, 'media_app/index.html', {'medias': medias})

def form(request):
    return render(request,'media_app/form.html')

def mediaform(request,media=None):
    if request.method=="POST":
        form=MediaForm(request.POST,request.FILES,instance=media)
        if form.is_valid():
            media = form.save(commit=False)
            media.title = form.cleaned_data['title']
            media.image = form.cleaned_data['image']
            media.description=form.cleaned_data['description']
            media.save()
            return redirect('index')
    else:
        form = MediaForm(instance=media)
        return render(request,'media_app/form.html',{'form':form})
