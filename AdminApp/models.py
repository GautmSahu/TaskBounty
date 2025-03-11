from django.db import models

class App(models.Model):
    CATEGORY_CHOICES = (('Entertainment','Entertainment'),('Social','Social'))
    SUB_CATEGORY_CHOICES = (('Videos','Videos'),('Engagement','Engagement'))

    name = models.CharField(max_length=100)
    link = models.TextField()
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=40, choices=SUB_CATEGORY_CHOICES)
    logo = models.ImageField(upload_to="logo/")
    points = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),  # Composite Index on id
        ]
