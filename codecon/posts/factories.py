from django.db.models import Q

from posts.models import Post, Like

from comments.models import Comment

import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension


class PostFactory:

    def list(self, user, page_type):
        posts = Post.objects.all()
        owners = [user]
        if page_type == "stream":
            for item in user.followed.all():
                owners.append(item.follower)

        posts = posts.filter(owner__in=owners)
        for post in posts:
            comments = Comment.objects.filter(commented_post=post)
            for item in comments:
                if item.owner == user:
                    item.is_owner = True
                else:
                    item.is_owner = False
            post.all_comments = comments
            post.all_likes = Like.objects.filter(liked_post=post)
            post.content =  markdown.markdown(post.content,
                         extensions=[GithubFlavoredMarkdownExtension()])

        return posts

    def list_profile(self, user):
        posts = Post.objects.filter(owner=user)

        for post in posts:
            comments = Comment.objects.filter(commented_post=post)
            for item in comments:
                if item.owner == user:
                    item.is_owner = True
                else:
                    item.is_owner = False
            post.all_comments = comments
            post.all_likes = Like.objects.filter(liked_post=post)

        return posts

    def detail(self, pk):
        post = Post.objects.get(pk=pk)
        post.all_comments = Comment.objects.filter(commented_post=post)
        post.all_likes = Like.objects.filter(liked_post=post)

        return post


post_factory = PostFactory()
