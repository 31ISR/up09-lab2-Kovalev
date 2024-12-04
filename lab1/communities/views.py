from django.shortcuts import render
from .models import Communities

def communities_list(request):
    communities = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})