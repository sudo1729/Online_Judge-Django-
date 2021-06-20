from django.db import models

class Compiler(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=10)
    code = models.TextField()
    language = models.CharField(max_length=10)
    customInput = models.TextField(blank=True)
    expectedOutput = models.TextField(blank=True)
    output = models.TextField(blank=True)
    verdict = models.CharField(max_length=10,blank=True)

    class Meta:
        ordering = ['created']