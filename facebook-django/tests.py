#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
# 

"""
This python module provides the models for the video vault application.

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from django.test import TestCase
from django.test.client import RequestFactory
from .models.client import FacebookClientOption
from datetime import datetime
import os

FACEBOOK_ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN'] 
FACEBOOK_ACCESS_SECRET = os.environ['FACEBOOK_ACCESS_SECRET'] 
FACEBOOK_PAGE_ID = os.environ['FACEBOOK_PAGE_ID'] 
FACEBOOK_API_VERSION = os.environ['FACEBOOK_API_VERSION'] 
FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID'] 
CONTENT = "Testing django-cpss-facebook."
LINK_CONTENT = "https://github.com/xgdfalcon/django-cpss-facebook"
 

class FacebookDjangoTestCase(TestCase):
    def setUp(self):
        FacebookClientOption.objects.create(
            facebook_app_id=FACEBOOK_APP_ID,
            facebook_token_secret=FACEBOOK_ACCESS_SECRET,
            facebook_api_version=FACEBOOK_API_VERSION,
            facebook_access_token=FACEBOOK_ACCESS_TOKEN,
            facebook_page_id=FACEBOOK_PAGE_ID)

    def test_page_events(self):
        collection = FacebookClientOption.objects.get(facebook_page_id=FACEBOOK_PAGE_ID)
        result = collection.get_page_events()
        print(result)

    def test_post_status(self):
        collection = FacebookClientOption.objects.get(facebook_page_id=FACEBOOK_PAGE_ID)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        result = collection.post_to_page(dt_string + " - " + CONTENT)
        print(result)

    def test_post_link(self):
        collection = FacebookClientOption.objects.get(facebook_page_id=FACEBOOK_PAGE_ID)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        result = collection.post_link_to_page(dt_string + " - " + CONTENT, LINK_CONTENT)
        print(result)

    def test_get_page_posts(self):
        collection = FacebookClientOption.objects.get(facebook_page_id=FACEBOOK_PAGE_ID)
        result = collection.get_page_posts()
        print(result)