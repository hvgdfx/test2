from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible # 当你想支持python2版本的时候才需要这个装饰器
class Question(models.Model):
    # ...
    def __str__(self):   # 在python2版本中使用的是__unique__
        return self.question_text

@python_2_unicode_compatible 
class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
