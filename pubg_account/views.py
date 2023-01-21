from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth import get_user_model

class PubgAccountListView(ListView):
    model = PubgAccount
    template_name = 'pubg/list.html'

class PubgAccountDetailView(DetailView):
    model = PubgAccount
    template_name = 'pubg/detail.html'

    def post(self, request, *args, **kwargs):
        new_comment = CommentBlog(content = request.POST.get('content'), 
            author = self.request.user, blogpost_connected = self.get_object()
        )
        new_comment.save()
        
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PubgAccountDetailView, self).get_context_data(*args, **kwargs)
        data = super().get_context_data(**kwargs)

        comments_connected = CommentBlog.objects.filter(
            blogpost_connected = self.get_object()).order_by('-date_posted')
        
        data['comments'] = comments_connected
        
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance = self.request.user)
        
        context.update(data)
        return context

class PubgAccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PubgAccount
    form_class = PubgAccountForm
  
    template_name = 'pubg/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PubgAccountDeleteView(DeleteView):
    model = PubgAccount
    template_name = 'pubg/delete.html'
    success_url = reverse_lazy('pubg-account-list')


class PubgAccountCreateView(LoginRequiredMixin, CreateView):
    model = PubgAccount
    form_class = PubgAccountForm
    template_name = 'pubg/new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)