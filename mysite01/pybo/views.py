from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date') # create_date를 기준으로 역순정렬
    context = {'question_list': question_list} 

    # question_list의 data를 pybo/question_list.html 파일에 적용하여 html을 생성한 후 return(반드시 template 필요)
    return render(request, 'pybo/question_list.html', context) 
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    
    return render(request, 'pybo/question_detail.html', context) 