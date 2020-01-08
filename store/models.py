# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.

class Serie(models.Model):
    serie = models.CharField(max_length=255)
    chaine = models.CharField(max_length=255)
