from django.shortcuts import render

from django.views.generic import TemplateView

from app.filters import ResultFilter
from app.models import Category, Question, Result
from app.servieces import check_answer


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        cd['categories'] = Category.objects.all()
        return cd


def question_list(request , slug):
    category = Category.objects.get(slug=slug)
    questions = Question.objects.filter(category=category)


    if request.method == 'POST':
        context = check_answer(request , questions , category)
        return render(request , template_name='app/result.html' , context=context)

    context = {
        'questions':questions ,
        'category':category
    }
    return render(request , template_name='app/question_list.html' , context=context)

def result_list(request):
    filter = ResultFilter(request.GET , queryset=Result.objects.all())

    context = {
        'filter':filter
    }

    return render(request , template_name='app/result_list.html' , context=context)