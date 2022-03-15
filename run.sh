#!/bin/bash
# debug
# ./manage.py runserver 192.168.2.223:8888

# echo $0 $1
rt=`pwd`
if [ "$1" == "debug" ]
then
	cd $rt
	./manage.py runserver 192.168.2.223:8888
else
	uwsgi --http :8888 --module mod_provider.wsgi
fi
