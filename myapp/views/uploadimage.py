from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from myapp.forms import Upload_Image
from myapp.models.user_image import Image_Post


class UploadView(View):
    def get(self, request):
        fm = Upload_Image()
        return render(request, 'upload.html', {'form': fm})

    def post(self, request):
        fm = Upload_Image(request.POST, request.FILES)
        if fm.is_valid():
            mainuser = request.user
            title = fm.cleaned_data['title']
            image = fm.cleaned_data['image']
            contact = Image_Post(myuser=mainuser, title=title, image=image)
            contact.save()

        return render(request, 'upload.html', {'form': fm})
