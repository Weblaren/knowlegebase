# from django.shortcuts import render
from django.views.generic import TemplateView 
# # Create your views here.
class QuestionView(TemplateView):
    template_name="stack exchange.html"


class AboutView(TemplateView):
    template_name="index.html"