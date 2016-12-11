from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    # return HttpResponse("Hello, world~!! nicekkong@gmail.com")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = '<br/> '.join([q.question_text for q in latest_question_list])
    # html = '<h1> Question List</h1>'
    # html += '<hr/>'
    # html += ('<b>%s</b>' % output)
    # return HttpResponse(html)
    ## template loader를 사용한 방법
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context))
    ## short-cut
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def index2(request):
    return HttpResponse("This is index2~!! index2 파일입니다")

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s" % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist!!!!!')
    # return render(request, 'polls/detail.html',
    #               {'question': question,
    #                'question_id':question_id})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',
                  {'question': question, 'question_id':question_id,
                   } )


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))