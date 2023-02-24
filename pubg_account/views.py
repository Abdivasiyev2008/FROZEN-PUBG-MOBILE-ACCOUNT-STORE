from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.shortcuts import render


class DonateAccountListView(ListView):
    model = DonateAccount
    template_name = 'pubg/donate/list.html'

    paginate_by = 30

class DonateAccountDetailView(DetailView):
    model = DonateAccount
    template_name = 'pubg/donate/detail.html'

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content = request.POST.get('content'), 
            author = self.request.user, blogpost_connected = self.get_object()
        )
        new_comment.save()
        
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(DonateAccountDetailView, self).get_context_data(*args, **kwargs)
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(
            blogpost_connected = self.get_object()).order_by('-date_posted')
        
        data['comments'] = comments_connected
        
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance = self.request.user)
        
        context.update(data)
        return context

class DonateAccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DonateAccount
    form_class = DonateAccountForm
  
    template_name = 'pubg/donate/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DonateAccountDeleteView(DeleteView):
    model = DonateAccount
    template_name = 'pubg/donate/delete.html'
    success_url = reverse_lazy('pubg-account-list')


class DonateAccountCreateView(LoginRequiredMixin, CreateView):
    model = DonateAccount
    form_class = DonateAccountForm
    template_name = 'pubg/donate/new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

