# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

class TodoItem(TimeStampedModel, StatusModel):
    STATUS = Choices('open', 'cancelled', 'failed', 'complete')

    title = models.CharField(max_length=128)

    start = models.DateTimeField(blank=True, null=True)
    due = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)

    order = models.BigIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order', )
