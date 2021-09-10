from django.urls import include, path
from . import views

urlpatterns=[
    # path("", views.starting_page, name="start"),
    path("", views.StartPageView.as_view(), name="start"),
    path("posts", views.PostsView.as_view(), name="posts"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(), name="post_detail"),
    # path("read-later",views.ReadLaterView.as_view(), name="read-later")
]