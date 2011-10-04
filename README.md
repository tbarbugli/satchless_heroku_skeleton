Basic structure for a django app using satchless on Heroku + S3

At this present satchless is part of the repo and kinda sucks...

Still to figure out why -e git+git://.....#egg=egg-name does not work (for me?) on Heroku
and no, Heroku does not handle submodules :(

I suggest you to have a link to virtualenv (you use it, right !?) bin folder inside base project folder.

- virtualenv environment --no-site-packages
- heroku create --stack cedar
- ... setup heroku steps ...
- set your AWS credentials
    - echo AWS_ACCESS_KEY_ID=xxxxxxxxxxxxx >> .env
    - echo AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxx >> .env
    - echo AWS_STORAGE_BUCKET_NAME=xxxxxxxxxxxxx >> .env
    - heroku config:add AWS_ACCESS_KEY_ID=xxxxxxxxxxxxx 
    - heroku config:add AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxx
    - heroku config:add AWS_STORAGE_BUCKET_NAME=xxxxxxxxxxxxx
- python py/manage.py collectstatic