from django.contrib import admin

# Register your models here.
from django.contrib import admin
from  .models import  Choice,Blog
class ChoiceInline(admin.TabularInline):
  model=Choice
  extra=3  
  
class BlogAdmin(admin.ModelAdmin):
  fieldsets=[
    (None,      {'fields':['title']}),
    ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    (None,       {'fields':['content']}),
   ]
  inlines=[ChoiceInline]
  list_display=('title','pub_date','was_published_recently')
  list_filter=['pub_date']
  search_fields=['title']
admin.site.register(Blog,BlogAdmin) 
admin.site.register(Choice)
