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
from  .models import  Choice,Blog
 
# Create your views here.
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_blog_list'
	
	def get_queryset(self):
		"""Return the last five published blog.(not including those set to  bo published in the future)."""
		return  Blog.objects.filter(
			pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
	model=Blog
	template_name='polls/detail.html'
	def get_queryset(self):
		"""
		Excludes any blogs that aren't published yet.
		"""
		return Blog.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model=Blog
	template_name='polls/results.html'	
	
def vote(request,blog_id):
	p=get_object_or_404(Blog,pk=blog_id)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		#Redisplay the blog voting form.
		return render(request,'polls/detail.html',{
			'blog':p,
			'error_message':"You didn't seletc a choice.",
		})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing
		#with POST data. This prevents data from being posted twice if a 
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results',args=(p.blog_id,)))


class BlogCreate(CreateView):
	model=Blog
	fields=['title','content']
	template_name='polls/addblog.html'
	def get_success_url(self):
		return reverse('polls:detail',args=(self.object.id,))

class BlogUpdate(UpdateView):
	model=Blog
	fields=['title','content']
	template_name='polls/update.html'
	def get_success_url(self):
		return reverse('polls:detail',args=(self.object.id,))


