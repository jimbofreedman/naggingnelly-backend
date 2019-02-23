# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices
from recurrence.fields import RecurrenceField
from django.utils import timezone


class Context(TimeStampedModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class TodoItem(TimeStampedModel, StatusModel):
    STATUS = Choices('open', 'cancelled', 'failed', 'complete')

    title = models.CharField(max_length=128)

    start = models.DateTimeField(blank=True, null=True)
    due = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)

    order = models.BigIntegerField()

    recurrence = RecurrenceField(blank=True, null=True)


    contexts = models.ManyToManyField(Context)

    def save(self, *args, **kwargs):
        # If we have just been completed
        if self.status != self.STATUS.open and self.completed is None:
            # Make an TodoRecurrenceLog object for this TodoItem,
            # and reset it with new start/due
            if self.recurrence is not None and len(self.recurrence.rrules) > 0 and self.start:
                self.recurrence.dtstart = datetime.combine(self.due.date(), datetime.min.time())

                recurrence_log = TodoRecurrenceLog.objects.create(
                    item=self,
                    status=self.status,
                    start=self.start,
                    due=self.due
                )
                recurrence_log.save()
                recur_date = self.recurrence.after(self.start, inc=False)

                if recur_date is not None:
                    self.start = datetime.combine(recur_date, self.start.time())
                    self.due = datetime.combine(recur_date, self.due.time()) if self.due else None
                    self.status = self.STATUS.open
                else:
                    self.completed = timezone.now()
            else:
                self.completed = timezone.now()

        super(TodoItem , self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order', )


class TodoRecurrenceLog(TimeStampedModel, StatusModel):
    STATUS = TodoItem.STATUS
    
    item = models.ForeignKey(TodoItem, on_delete=models.CASCADE)

    start = models.DateTimeField(null=True, blank=True)
    due = models.DateTimeField(null=True, blank=True)
