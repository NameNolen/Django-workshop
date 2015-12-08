#from django.http import Http404
#from django.shortcuts import render
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from django.template import RequestContext,loader
#from django.shortcuts import render
from  .models import  Choice,Question
 
# Create your views here.
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'
	
	def get_queryset(self):
		"""Return the last five published question.(not including those set to  bo published in the future)."""
		return Question.objects.filter(
			pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())
class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'	
	
def vote(request,question_id):
	p=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		#Redisplay the question voting form.
		return render(request,'polls/detail.html',{
			'question':p,
			'error_message':"You didn't seletc a choice.",
		})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing
		#with POST data. This prevents data from being posted twice if a 
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))


class QuestionCreate(CreateView):
	model=Question
	fields=['question_text','content']
	template_name='polls/addquestion.html'
	def get_success_url(self):
		return reverse('polls:index')

class QuestionUpdate(UpdateView):
	model=Question
	fields=['content']
	template_name='polls/addquestion.html'
	

