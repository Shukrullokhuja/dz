from django.db import models

# Create your models here.
class Check(models.Model):
    name=models.CharField(max_length=50)
    count=models.PositiveIntegerField(default=0)
    price=models.PositiveIntegerField(default=0)
    Itogo=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"Название:{self.name} \n Количество{self.count}\n Цена{self.price}\n Итого{self.Itogo}"



class tabels(models.Model):
    num_of_table=models.PositiveIntegerField(default=0)
    aktivnost=models.CharField(max_length=50)
    count_of_guests=models.PositiveIntegerField(default=0)
    chet=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Номер стола {self.num_of_table}, активность стола {self.aktivnost}, количество стола {self.count_of_guests}, Счет {self.chet}"



class Cofe(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class cold_drinks(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Название {self.name}, Цена {self.price}"




