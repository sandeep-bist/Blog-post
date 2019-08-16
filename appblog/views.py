from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Post


# def authors(request):
#     context={'users': User.objects.all()}
#     return render(request,'appblog/base.html',context)

# def search(request):
#     queryset=Post.objects.all()
#     query= request.GET.get('q')
#     if query:
#         queryset= queryset.filter(title__icontains=query)
#     context= { "queryset":queryset }
#     return render(request,'appblog/home.html',context)
def searchposts(request):
    results=Post.objects.all()
    if request.method == 'GET':
        query= request.GET.get('q')

        if query is not None:
            results= Post.objects.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(author__first_name__icontains=query)|
                Q(author__last_name__icontains=query)
            ).distinct()

    paginator = Paginator(results, 3) 
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context={'results': results,'object_list':queryset}
    return render(request, 'appblog/search.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'appblog/home.html' #django expected template-- <app_name>/<model_name>_<viewtype>
    context_object_name = 'posts' #if we will not mention it then the default name in template is  'object_list'
    paginate_by =3

    def get_queryset(self):
        return Post.objects.order_by('-date_posted')

    #def get_queryset(self):
        #return Post.objects.all()
    #two ways to execute listview either by mention "model=model_name" or by
    #defining function get_queryset--get the easyone.. :-)


class UserPostListView(ListView):
    model = Post
    template_name = 'appblog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        # print(user)
        return Post.objects.filter(author=user).order_by('date_posted')

    #context_object_name = 'posts' #if we will not mention it then the default name in template is  'object_list'



class PostDetailView(DetailView):
    model = Post




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content','images']



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content','images']



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user ==  post.author:
            return True
        return False

# def about(request):
#     return render(request,'appblog/about.html',{'title':"About"})
#       <a class="nav-item nav-link " href="{%url 'blog-about'%} ">About</a>
