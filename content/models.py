from django.db import models



class TechStack(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Tags(models.Model):
    tag = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.tag

class Questions(models.Model):
    Question = models.CharField(max_length=10000)
    techstack = models.ManyToManyField(TechStack)
    tags = models.ManyToManyField(Tags)
    Options = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Questions")
        verbose_name_plural = ("Questionss")

    def __str__(self):
        return self.name




class Content(models.Model):
    title = models.CharField(max_length=100)
    techstack = models.ManyToManyField(TechStack )
    content = models.TextField(null=False , blank=False)
    points = models.IntegerField(null=False , blank=False)
    Tags = models.ManyToManyField(Tags)
    Related_Questions = models.ManyToManyField(Questions)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Content")
        verbose_name_plural = ("Contents")

    def __str__(self):
        return self.title
