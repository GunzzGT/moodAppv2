from djongo import models


class ArrayFiller(models.Model):
    pertanyaan = models.CharField(primary_key=True, max_length=200)
    jawaban = models.CharField(max_length=200)
    deskripsi = models.CharField(max_length=200)

    class Meta:
        managed = False


class QuestionListTemplate(models.Model):
    question_id = models.CharField(primary_key=True, max_length=20)
    status = models.CharField(max_length=20, default='Active')
    title = models.CharField(max_length=200)
    subtitle = models.ArrayField(model_container=ArrayFiller, default=[])


class QuestionListUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20, editable=False)
    question_set = models.ArrayField(model_container=QuestionListTemplate, default=[])
