from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_de_création = models.DateTimeField(auto_now_add=True)
    date_de_publication = models.DateTimeField(auto_now=True)
    accroche = models.CharField(max_length=200, default=True)
    texte = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def publish(self):
        self.date_de_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.titre


    class Meta : 
        permissions = (
                ("supprimer_post", "description supprimer un post"),
                ("dashboard_admin", "accès django administrateur"),
            )