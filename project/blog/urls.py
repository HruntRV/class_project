from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .import views
from .views import MyLogoutView


class MyLoginView:
    @classmethod
    def as_view(cls):
        pass


urlpatterns = [
    path('', views.index, name="main"),
    path("post/<str:name>/<int:id>/", views.post, name="post"),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contacts', views.contact, name='contacts'),
    path('category/<str:c>', views.category, name='category'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('login', LoginView.as_view(), name='blog_login'),
    # path('login', LoginView.as_view(), name='blog_login'),
    path('logout', MyLogoutView.as_view(), name='blog_logout'),
    # path('login', MyLoginView.as_view(), name='blog_login'),
    path('profile/', views.profile, name='profile')

]
