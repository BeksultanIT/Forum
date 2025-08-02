from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel


class Comment(BaseCreateUpdateModel):
    forum = models.ForeignKey('webapp.Forum',related_name='comments', on_delete=models.CASCADE,
                                verbose_name='Форум')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.SET_DEFAULT, default=1,
                               verbose_name="Автор")

    def __str__(self):
        return self.text[:20]

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"

    def get_absolute_url(self):
        return reverse("webapp:index")