from django.contrib import admin
from base.models import MockSet, Company, Question, TestCase

admin.site.register(MockSet)
admin.site.register(Company)
admin.site.register(Question)
admin.site.register(TestCase)

# Register your models here.
