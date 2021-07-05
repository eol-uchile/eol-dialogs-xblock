#!/bin/dash

pip install -e /openedx/requirements/eoldialogs

cd /openedx/requirements/eoldialogs
cp /openedx/edx-platform/setup.cfg .
mkdir test_root
cd test_root/
ln -s /openedx/staticfiles .

cd /openedx/requirements/eoldialogs

DJANGO_SETTINGS_MODULE=lms.envs.test EDXAPP_TEST_MONGO_HOST=mongodb pytest eoldialogs/tests.py

rm -rf test_root
