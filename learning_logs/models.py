from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField('主题', max_length=200)
    date_added = models.DateTimeField('修改时间', auto_now_add=True)
    owner = models.ForeignKey(User, verbose_name='拥有者',
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学习到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, verbose_name='主题', on_delete=models.CASCADE)
    text = models.TextField('条目')
    date_added = models.DateTimeField('修改时间', auto_now_add=True)

    class Meta:
        verbose_name = '条目'
        verbose_name_plural = verbose_name

    def __str__(self):
        """返回模型的字符串表示"""
        return f'{self.text[:50]}...'