from django.db import models


class Quiz(models.Model):
    category = models.ForeignKey(
        "Categoryes",
        to_field="title",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    question = models.TextField(verbose_name="Вопрос")
    question_id = models.IntegerField(verbose_name="ID вопроса", unique=True)
    airdate = models.DateTimeField(verbose_name="Дата вопроса")
    answer = models.CharField(verbose_name="Ответ")
    value = models.IntegerField(verbose_name="Очки", null=True, blank=True)

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["category"]


class Categoryes(models.Model):
    title = models.CharField(verbose_name="Категории", unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
