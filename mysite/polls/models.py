import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.urlresolvers import   reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
	content=RichTextUploadingField(blank=True)
	title=models.CharField(max_length=200,unique=True)
	pub_date=models.DateTimeField('date published', default=timezone.now)
	def __unicode__(self):
		return self.title
	def was_published_recently(self):
		now=timezone.now()
		return now - datetime.timedelta(days=1)  <= self.pub_date <=now
	was_published_recently.admin_order_field='pub_date'
	was_published_recently.boolean=True
	was_published_recently.short_description='Published recently?'
class Choice(models.Model):
	question=models.ForeignKey(Blog)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __unicode__(self):
		return  self.choice_text


    
    
    
