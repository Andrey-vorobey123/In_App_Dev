from django.shortcuts import render
from django.views import generic
from firstapp.models import Cinema, Film

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )

""" def script(request):


    
    return render(
        request,
        'script.html',
    ) """

class script(generic.ListView):
    model = Cinema
    context_object_name = 'Cin'
    template_name = 'script.html' 

    """ def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(script, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context """
