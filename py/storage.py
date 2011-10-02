"""
echo AWS_ACCESS_KEY_ID=xxxxxxxxxxxxx >> .env
echo AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxx >> .env
echo AWS_STORAGE_BUCKET_NAME=xxxxxxxxxxxxx >> .env
heroku config:add AWS_ACCESS_KEY_ID=xxxxxxxxxxxxx 
heroku config:add AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxx
heroku config:add AWS_STORAGE_BUCKET_NAME=xxxxxxxxxxxxx

"""

import os
from copy import copy

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

STATICFILES_STORAGE = COMPRESS_STORAGE = 'storage_backends.CachedS3BotoStorage'
STATIC_URL = "http://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
COMPRESS_URL = copy(STATIC_URL)
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"