#!/bin/bash

cd src && ENVIRONMENT=development DB_ENVIRONMENT=development VERSION=dev python manage.py $@