#!/bin/sh

INSTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# echo $INSTDIR # /sattu/project/blogger_zone/source
SOURCEDIR="$(dirname "$INSTDIR")"
# echo $SOURCEDIR # /sattu/project/blogger_zone

cd $SOURCEDIR
source BloggerAppEnv/bin/activate
cd $INSTDIR
start()
{
python3 manage.py runserver 0.0.0.0:9000
}
start
