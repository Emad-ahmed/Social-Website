from django.contrib import admin
from myapp.models.user_post import Post_Info
from myapp.models.user_image import Image_Post
from myapp.models.profileupdate import Profile_Post


# Register your models here.


@admin.register(Post_Info)
class PostInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'myuser', 'date']


@admin.register(Image_Post)
class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'myuser']


@admin.register(Profile_Post)
class ProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['id']
