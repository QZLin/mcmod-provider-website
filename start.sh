#!/bin/bash
# debug
# ./manage.py runserver 192.168.2.223:8888

# echo $0 $1
rt=`pwd`
if [ "$1" == "debug" ]
then
	echo modp.debug

	screen -dmS modp
	screen -S modp -X stuff "cd $rt; ./manage.py runserver 192.168.2.223:8888\n"
else
	echo modp

	screen -dmS modp
	screen -S modp -X stuff "cd $rt; uwsgi --http :8888 --module mod_provider.wsgi\n"
fi
