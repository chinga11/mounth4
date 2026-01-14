from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .form import ProductForm


def home(request):
   if request.method == "GET":
      return render(request,'index.html')


def product_list(request):
   if request.method == "GET":
      products = Post.objects.all()
      return render(request,'app/post_list.html',context={'products': products})


def product_datail(request,product_id):
   if request.method == "GET":
      product = Post.objects.filter(id=product_id).first()
      return render(request,'app/post_detail.html',context={"product":product})
   

def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                photo=form.cleaned_data['photo'],
            )
            return HttpResponse("Product created")
    else:
        form = ProductForm()

    return render(request, "app/product_create.html", {"form": form})
