from django.db import models
from django.core.validators import FileExtensionValidator

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

class SocialLink(models.Model):
    title = models.CharField("Name", max_length=50, help_text="Например: Telegram, Bluesky")
    url = models.URLField("URL Link", max_length=300, help_text="Полный адрес, начиная с https://")
    icon = models.FileField(
        "Icon",
        upload_to="social/",
        validators=[FileExtensionValidator(["png", "svg", "webp", "jpg", "jprg", "gif"])],
        help_text="PNG или SVG, квадратная, примерно 84×84 px или больше",
    )
    order = models.PositiveSmallIntegerField("Порядок", default=0, help_text="Меньше число - левее")
    is_active = models.BooleanField("Показывать", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Ссылка на соцсеть",
        verbose_name_plural = "Ссылка на соцсети"

    def __str__(self):
        return self.title

class CommissonsStatus(models.Model):
    commissons_status = models.BooleanField(
        default=True,
        verbose_name="Статус коммишек"
    )

    class Meta:
        verbose_name = "Нвстройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"