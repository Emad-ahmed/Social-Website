from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from myapp.models import Post_Info, Image_Post, Profile_Post
from myapp.forms import EditProfileChange, PasswordChange
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            myallpost = Post_Info.objects.all().order_by('-id')[:5]
            myallImage = Image_Post.objects.all().order_by('-id')[:5]
            try:
                myimage = Profile_Post.objects.get(myid=id)
            except:
                myimage = None

            return render(request, 'index.html', {'user': myallpost, 'userimage': myallImage, 'pimage': myimage})
        else:
            return HttpResponseRedirect('/login')

    def post(self, request):
        mypost = request.POST.get('mypost')
        contact = Post_Info(myuser=request.user, post=mypost)
        contact.save()
        myallpost = Post_Info.objects.all().order_by('-id')[:5]
        return render(request, 'index.html', {'user': myallpost})


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.FILES['myfile']:
            fm = EditProfileChange(request.POST, instance=request.user)
            myfile = request.FILES['myfile']
            id = request.user.id
            mybestpic = Profile_Post(myid=id, image=myfile)
            mybestpic.save()
            if fm.is_valid():
                fm.save()
                messages.success(request, "Successfully Changed")

        else:
            fm = EditProfileChange(instance=request.user)
            return render(request, 'editprofile.html', {'form': fm})

        return render(request, 'editprofile.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login')


def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChange(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Successfully Changed Password')
                return HttpResponseRedirect('/login')
        else:
            fm = PasswordChange(user=request.user)
            return render(request, 'changepass.html', {'form': fm})
        return render(request, 'changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')
