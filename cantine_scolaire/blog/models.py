from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    date_de_publication = models.DateTimeField(auto_now=True)
    accroche = models.CharField(max_length=200)
    texte = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def publish(self):
        self.date_de_creation = timezone.now()
        self.save()

    def __str__(self):
        return self.titre


    class Meta : 
        permissions = (
                ("supprimer_post", "description supprimer un post"),
                ("dashboard_admin", "accès django administrateur"),
                ("modifier_post", "modifier un post"),
                ("ajouter_post", "ajouter un post"),
            )



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    auteur = models.CharField(max_length=200)
    texte = models.TextField()
    date_de_creation = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.texte


    class Meta : 
        permissions = (
                ("ajouter_comment", "ajouter un commentaire"),
                ("supprimer_comment", "supprimer un commentaire"),
            )