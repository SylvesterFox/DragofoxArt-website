from django.db import models

class Artwork(models.Model):
    title = models.CharField("Name", max_length=400)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Image", upload_to="arts/%Y/%m")
    created = models.DateField("Created", auto_now_add=True)
    is_nsfw  =  models.BooleanField("Nsfw", default=False)
    is_published = models.BooleanField("Push", default=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Арт"
        verbose_name_plural = "Арты"

    def __str__(self):
        return self.title
