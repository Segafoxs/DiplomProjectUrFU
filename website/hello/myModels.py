from django.db import models

# Create your models here.

class Work(models.Model):
    name: str
    dateStart: str
    timeStart: str
    dateEnd: str
    timeEnd: str

class Worker(models.Model):

    #Разряд работника
    discharge: str | None = None

    def __init__(self, name, postemploee):
        self.name = name
        self.postemploee = postemploee


class Manager(Worker):
    pass


class Executor(Worker):
    pass

class Director(Worker):
    pass


class Permit():
    #номер наряда будет равен id в базе данных
    dateDelivery: str
    timeDelivery: str
    conditions: str


class ShiftManager(Worker):
   pass