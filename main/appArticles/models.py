from djongo import models

class Articles(models.Model):
    _id = models.CharField(primary_key=True, max_length=20)
    article_id = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    status = models.CharField(max_length=20)