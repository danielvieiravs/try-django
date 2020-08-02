import random

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        num_1 = random.randint(0, 1000000)
        num_2 = random.randint(0, 1000000)
        num_3 = random.randint(0, 1000000)
        some_list = [num_1, num_2, num_3]

        context = {
            "bool_item": True,
            "num": num_1,
            "some_list": some_list}

        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
