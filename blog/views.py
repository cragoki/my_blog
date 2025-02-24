from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from blog.forms import CommentForm
from blog.models import Post


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]  # Order By Date Descending
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


#def starting_page(request):
    #latest_posts = Post.objects.all().order_by("-date")[:3]  # - is desc
    #sorted_posts = sorted(all_posts, key=get_date)
    #latest_posts = sorted_posts[-3:]  # end of the list, move three left, to the end of the list
    #return render(request, "blog/index.html", {
        #"posts": latest_posts
    #})

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]  # Order By Date Descending
    context_object_name = "all_posts"


#def posts(request):
    #all_posts = Post.objects.all().order_by("-date")
    #return render(request, "blog/all-posts.html",
                  #{
                      #"all_posts": all_posts
                  #})

class PostDetailView(View):
    template_name = "blog/post-detail.html"

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        else:
            context = {
                "post": post,
                "post_tags": post.tags.all(),
                "comment_form": CommentForm()
            }
            return render(request, self.template_name, context)
#def post_detail(request, slug):
    #identified_post = get_object_or_404(Post, slug=slug)
    #return render(request, "blog/post-detail.html", {
        #"post": identified_post,
        #"post_tags": identified_post.tags.all()
    #})
