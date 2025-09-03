from django.shortcuts import render
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.TextField(blank=True, null=True)


class Meta:
    ordering = ['apellido', 'nombre']


def __str__(self):
    return f"{self.nombre} {self.apellido}".strip()




class Editorial(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=30, blank=True, null=True)


class Meta:
    ordering = ['nombre']


def __str__(self):
    return self.nombre
 

