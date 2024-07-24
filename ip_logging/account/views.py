from django.views import View
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm


class Home(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "home.html")


class Login(View):
    form = LoginForm
    template = "login.html"

    def get(self, request):
        return render(request, self.template, {"form": self.form})

    def post(self, request):

        form = self.form(request.POST)

        if form.is_valid():

            user = form.cleaned_data["user"]
            login(request, user)
            return redirect("home")

        return render(request, self.template, {"form": form})


class Logout(View):
    def get(self, request):

        logout(request)
        return redirect("login")
