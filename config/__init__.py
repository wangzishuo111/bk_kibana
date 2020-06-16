# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['celery_app', 'RUN_VER', 'APP_CODE', 'SECRET_KEY', 'BK_URL', 'BASE_DIR']

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息

# SaaS运行版本，如非必要请勿修改
RUN_VER = 'open'
# SaaS应用ID
APP_CODE = 'bkkibana'
# SaaS安全密钥，注意请勿泄露该密钥
SECRET_KEY = '741f703b-55ec-4ace-bd5f-d1ec8b0b3045'
# 蓝鲸SaaS平台URL，例如 http://paas.bking.com
BK_URL = 'http://paas.growing.com' 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(
    __file__)))
