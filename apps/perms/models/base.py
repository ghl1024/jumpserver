# -*- coding: utf-8 -*-
#

import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from common.utils import date_expired_default


class BasePermission(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    users = models.ManyToManyField('users.User', blank=True,
                                   verbose_name=_("User"))
    user_groups = models.ManyToManyField('users.UserGroup', blank=True,
                                         verbose_name=_("User group"))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    date_start = models.DateTimeField(default=timezone.now, db_index=True,
                                      verbose_name=_("Date start"))
    date_expired = models.DateTimeField(default=date_expired_default,
                                        db_index=True,
                                        verbose_name=_('Date expired'))
    created_by = models.CharField(max_length=128, blank=True,
                                  verbose_name=_('Created by'))
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name=_('Date created'))
    comment = models.TextField(verbose_name=_('Comment'), blank=True)

    class Meta:
        abstract = True
