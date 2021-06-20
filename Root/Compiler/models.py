from django.db import models

class Compiler(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=10)
    code = models.TextField()
    language = models.CharField(max_length=10)
    customInput = models.TextField()
    expectedOuput = models.TextField()
    output = models.TextField()
    verdict = models.CharField(max_length=10)

    class Meta:
        ordering = ['created']