from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from truck_app.forms import TruckForm, CommentForm
from truck_app.models import Truck, Comment, Like


def index(request):
    trucks = Truck.objects.all().order_by('make')
    context = {
        'trucks': trucks,
        'page_name': 'home page',
    }
    return render(request, 'index.html', context)


@login_required
def create(request):
    if request.method == 'GET':
        context = {
            'form': TruckForm(),
            'page_name': 'create page',
        }
        return render(request, 'truck/create.html', context)
    else:
        form = TruckForm(request.POST, request.FILES)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.owner = request.user
            truck.save()
            return redirect('home page')
        context = {
            'form': form,
            'page_name': 'create page',
        }
        return render(request, 'truck/create.html', context)


@login_required
def edit(request, pk):
    truck = Truck.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': TruckForm(instance=truck),
            'truck': truck,
        }
        return render(request, 'truck/edit.html', context)
    else:
        form = TruckForm(request.POST, request.FILES, instance=truck)
        if form.is_valid():
            form.save()
            return redirect('details page', pk)
        context = {
            'form': form,
            'truck': truck,
        }
        return render(request, 'truck/edit.html', context)


@login_required
def details_comment(request, pk):
    truck = Truck.objects.get(pk=pk)
    comments = truck.comment_set.all().order_by('-id')
    if request.method == 'GET':
        context = {
            'truck': truck,
            'form': CommentForm(),
            'comments': comments,
            'liked': Like.objects.filter(owner_id=request.user.id, truck_id=pk).first(),
            'can_manipulate': truck.owner_id == request.user.id,
        }
        return render(request, 'truck/details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'], owner=request.user, truck=truck)
            comment.save()
            return redirect('details page', pk)
        context = {
            'truck': truck,
            'form': form,
            'comments': comments,
        }
        return render(request, 'truck/details.html', context)


def edit_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'comment': comment,
            'form': CommentForm(instance=comment),
        }
        return render(request, 'truck/edit_comment.html', context)
    else:
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('details page', comment.truck_id)
        context = {
            'comment': comment,
            'form': form,
        }
        return render(request, 'truck/edit_comment.html', context)


def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'comment': comment,
        }
        return render(request, 'truck/delete_comment.html', context)
    else:
        comment.delete()
        return redirect('details page', comment.truck_id)


@login_required
def like_truck(request, pk):
    like = Like.objects.filter(owner_id=request.user.id, truck_id=pk).first()
    if like:
        like.delete()
    else:
        truck = Truck.objects.get(pk=pk)
        like = Like(truck=truck, owner=request.user)
        like.save()
    return redirect('details page', pk)


@login_required
def delete(request, pk):
    truck = Truck.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'truck': truck,
        }
        return render(request, 'truck/delete.html', context)
    else:
        if truck.image:
            truck.image.delete()
        truck.delete()
        return redirect('home page')
