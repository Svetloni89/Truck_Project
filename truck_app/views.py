from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from truck_app.forms import TruckForm, CommentForm
from truck_app.models import Truck, Comment, Like
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin


class TrucksListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'trucks'
    ordering = 'make'
    model = Truck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'home page'
        return context


class TruckCreateView(LoginRequiredMixin, CreateView):
    template_name = 'truck/create.html'
    form_class = TruckForm
    model = Truck
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        truck = form.save(commit=False)
        truck.owner = self.request.user
        truck.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'create page'
        return context


class TruckEditView(LoginRequiredMixin, UpdateView):
    template_name = 'truck/edit.html'
    form_class = TruckForm
    model = Truck

    def get_success_url(self):
        url = reverse_lazy('details page', kwargs={'pk': self.object.id})
        return url


class DeleteTruckView(LoginRequiredMixin, DeleteView):
    template_name = 'truck/delete.html'
    model = Truck
    success_url = reverse_lazy('home page')


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


class CommentEditView(LoginRequiredMixin, UpdateView):
    template_name = 'truck/edit_comment.html'
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        url = reverse_lazy('details page', kwargs={'pk': self.object.truck_id})
        return url


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'truck/delete_comment.html'
    model = Comment

    def get_success_url(self):
        url = reverse_lazy('details page', kwargs={'pk': self.object.truck_id})
        return url


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
