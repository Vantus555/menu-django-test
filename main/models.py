from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent_item = models.ForeignKey(
        "MenuItem", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
