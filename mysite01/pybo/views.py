from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    page = request.GET.get('page', 1) # Page
    question_list = Question.objects.order_by('-create_date') # create_date를 기준으로 역순정렬
    paginator = Paginator(question_list, 10) # show 10 per page
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj} 

    # question_list의 data를 pybo/question_list.html 파일에 적용하여 html을 생성한 후 return(반드시 template 필요)
    return render(request, 'pybo/question_list.html', context) 
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    
    return render(request, 'pybo/question_detail.html', context) 

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # store login account as author
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        # return HttpResponseNotAllowed('Only Post is possible.')
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): # if form is valid
            question = form.save(commit=False) # return question object temporarily
            question.author = request.user # store login account as author
            question.create_date = timezone.now() # set create timestamp for store
            question.save() # store data
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)