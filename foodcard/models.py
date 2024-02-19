from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Receipt(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    cooking_time = models.TimeField()
    image = models.ImageField(upload_to='recipe_images/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Instructions(models.Model):
    name = models.CharField(max_length=100)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
