from django.shortcuts import render

from .models import Post



def home(request):
   return render(request,'index.html')


def product_list(request):
   products = Post.objects.all()
   return render(request,'app/post_list.html',{'products': products})
