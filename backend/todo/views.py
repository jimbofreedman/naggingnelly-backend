# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import TodoItem

def index(request):
    context = {
        "items": TodoItem.objects.filter(status=TodoItem.STATUS.open)
    }

    return render(request, "todo/index.html", context)


def complete(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.status = TodoItem.STATUS.complete
    item.save()

    return index(request)

