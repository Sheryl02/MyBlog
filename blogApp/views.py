from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,  Category, Comment
from .forms import editForm, addCommentForm, addPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def index(request):
#     return render(request, 'blogApp/base.html')

class home(ListView):
    model = Post
    template_name = 'blogApp/home.html'
    ordering = ['-created_on']
    paginate_by = 5
    def get_context_data(self, *args, **kwargs):
        category_menu =  Category.objects.all()
        context = super(home, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class post_detail(DetailView):
    model = Post
    template_name = 'blogApp/post_detail.html'
    ordering = ['-created_on']

    def get_context_data(self, *args, **kwargs):
        category_menu =  Category.objects.all()
        context = super(post_detail, self).get_context_data(*args, **kwargs)
        post_data = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_data.total_likes()
        liked = False
        if post_data.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["category_menu"] = category_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class addComment(CreateView):
    model = Comment
    form_class = addCommentForm
    template_name = 'blogApp/add_comment.html'
    # fields='__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    # success_url = reverse_lazy('home')
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk':self.kwargs['pk']})

def likePost(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('like_post'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

def categoryView(request, category):
    posts=Post.objects.filter(category__name__contains=category)
    return render(request, 'blogApp/category_posts.html', {'category':category, 'posts':posts})

class create_post(CreateView):
    model = Post
    form_class = addPostForm
    template_name = 'blogApp/add_post.html'
    # fields = ['title','body']
    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super().form_valid(form_class)

class post_update(UpdateView):
    model = Post
    form_class = editForm
    template_name = 'blogApp/update_post.html'
    # fields = ['title','author','body','category']


class delete_post(DeleteView):
    model = Post
    template_name = 'blogApp/delete_post.html'
    success_url = reverse_lazy('home')

# Create your views here.
