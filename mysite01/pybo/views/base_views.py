from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

def index(request):
    page = request.GET.get('page', 1) # Page
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date') # create_date를 기준으로 역순정렬
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # search title
            Q(content__icontains=kw) | # search content
            Q(answer__content__icontains=kw) | # search answer contents
            Q(author__username__icontains=kw) | # search question writer
            Q(answer__author__username__icontains=kw) # search answer writer
        ).distinct()
    paginator = Paginator(question_list, 10) # show 10 per page
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}

    # question_list의 data를 pybo/question_list.html 파일에 적용하여 html을 생성한 후 return(반드시 template 필요)
    return render(request, 'pybo/question_list.html', context) 

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    
    return render(request, 'pybo/question_detail.html', context) 