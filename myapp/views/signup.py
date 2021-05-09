from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from myapp.forms import SignForm
from django.contrib import messages


class SignView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            fm = SignForm()
            return render(request, 'signup.html', {'form': fm})
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        fm = SignForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Successfully Added')

        return render(request, 'signup.html', {'form': fm})
