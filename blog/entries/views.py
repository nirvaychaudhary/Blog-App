from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import EntryModel
from django.shortcuts import get_object_or_404 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogForm


# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    model = EntryModel
    template_name = 'entries/index.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 3
    

class EntryView(LoginRequiredMixin, DetailView):
    model = EntryModel
    template_name = "entries/entry_detail.html"

class CreateEntryView(LoginRequiredMixin,CreateView):
    model = EntryModel
    template_name = 'entries/create_entry.html'
    fields = ['entry_title', 'entry_text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)


def updateBlogEntryView(request, pk):
    instance_obj = get_object_or_404(EntryModel, id=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,instance = instance_obj)
        if form.is_valid():
            print("Form is Valid")
            print(form.cleaned_data)
            form.save()
            return redirect('blog-home')

        else:
            print("Form is invalid")
    else:
        form = BlogForm(instance=instance_obj)
    return render(request, 'entries/create_entry.html', {
        'form' : form
    })

    
def DeleteEntryView(request, pk): 
    delete_instance = get_object_or_404(EntryModel, id= pk)
    delete_instance.delete()
    return redirect('blog-home')