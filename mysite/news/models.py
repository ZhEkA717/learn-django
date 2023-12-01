from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date of updated')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='is Published')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']
        


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Name of category')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
    
    
# for el in range(5, 10):
#     News.objects.create(title='news '+str(el), content = 'Content of news ' + str(el))

# News.objects.all()
# News.objects.get(pk=7)
#news4 = News.object.get(pk=4)
# news4.title = 'News 4 is updated'
# news4.delete()

# from .models import news
# import random

# for item in news:   
#     item.category_id = random.randint(1,4)
#     item.save()

