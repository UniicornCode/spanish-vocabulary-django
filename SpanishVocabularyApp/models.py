from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/city_images/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Category(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to="images/category_images/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Word(models.Model):
    spanish = models.CharField(max_length=50)
    macedonian = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.spanish

    def get_word(self):
        return {'spanish': self.spanish,
                'macedonian': self.macedonian,
                'category': self.category}
