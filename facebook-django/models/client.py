#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
#

"""
This python module provides...

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import gettext as _
from django.db import models
from django.http import HttpRequest, HttpResponse
from ..signals import generate_longterm
from django.db.models import signals
from .facebook import GraphAPI, FACEBOOK_API_VERSIONS
import uuid
from enum import Enum

class FacebookClientManager(models.Manager):
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class FacebookClientType(models.Model):
    id = models.UUIDField(verbose_name=_("ID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    facebook_api_version = models.CharField(
        verbose_name=_("Facebook API Version"), max_length=5, default="2.12", choices=FACEBOOK_API_VERSIONS)
    facebook_longterm_access_token = models.CharField(
        verbose_name=_("Facebook Long Term Token"), max_length=100, default="")
    facebook_access_token = models.CharField(
        verbose_name=_("Facebook Access Token"), max_length=100, default="")
    facebook_token_secret = models.CharField(
        verbose_name=_("Facebook Token Secret"), max_length=100, default="")
    facebook_app_id = models.CharField(
        verbose_name=_("Facebook APP Id"), max_length=100, default="")
    facebook_page_id = models.CharField(
        verbose_name=_("Facebook Page ID"), unique=True, max_length=100, default="")
    facebook_user_id = models.CharField(
        verbose_name=_("Facebook User ID"), unique=True, max_length=100, default="")
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, verbose_name=_('Site'), blank=True)

    class Meta:
        abstract = True


class FacebookClientOption(FacebookClientType):
    objects = FacebookClientManager()

    class Meta:
        db_table = 'cpss_facebook_settings'
        verbose_name = _('CPSS Facebook Client Setting')
        verbose_name_plural = _('CPSS Facebook Client Settings')

    def __str__(self):
        str(self.facebook_token_secret)
        # return str(self.site.domain) + ": " + str(self.facebook_page_id)

    def generate_longterm(self):
        graph = GraphAPI(access_token=self.facebook_access_token, version=self.facebook_api_version)
        self.facebook_longterm_access_token = graph.longterm_access_token(self.facebook_app_id, self.facebook_token_secret)
        signals.post_save.disconnect(generate_longterm, sender=FacebookClientOption)
        self.save()
        signals.post_save.connect(generate_longterm, sender=FacebookClientOption)

    def post_link_to_page(self, message_content, link_content):
        graph = GraphAPI(app_secret=self.facebook_token_secret,
            access_token=self.facebook_access_token, version=self.facebook_api_version)

        id_result = graph.put_object(
            parent_object=self.facebook_page_id,
            connection_name="feed",
            message=message_content,
            link=link_content)

        return id_result

    def post_to_page(self, message_content):
        graph = GraphAPI(
            access_token=self.facebook_longterm_access_token, version=self.facebook_api_version)

        id_result = graph.put_object(
            parent_object=self.facebook_page_id,
            connection_name="feed",
            message=message_content)

        return id_result

    def get_page_events(self):
        graph = GraphAPI(
            access_token=self.facebook_longterm_access_token, version=self.facebook_api_version)

        id_result = graph.get_all_objects(
            parent_object=self.facebook_page_id,
            connection_name="events")

        return id_result

    def get_page_posts(self):
        graph = GraphAPI(
            access_token=self.facebook_longterm_access_token, version=self.facebook_api_version)

        id_result = graph.get_all_objects(
            parent_object=self.facebook_page_id,
            connection_name="posts")

        return id_result



signals.post_save.connect(generate_longterm, sender=FacebookClientOption)
