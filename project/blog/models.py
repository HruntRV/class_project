from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to='user_avatar')
    avatar = models.URLField(default="https://uxwing.com/wp-content/themes/uxwing/download/peoples-avatars/user-profile-icon.png")
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    image = models.URLField(default="http://placehold.it/900x300")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class Comment(models.Model):
    user = models.TextField(max_length=20, verbose_name='Користувач')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    content = models.TextField(verbose_name='Коментар')
    post = models.ForeignKey(Post, max_length=30, verbose_name="Заголовок", on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"


class Subscribe(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')

    def __str__(self):
        return self.email
