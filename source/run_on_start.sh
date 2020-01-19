echo "Starting some apps..."
#google-chrome --no-sandbox
echo -n "Do you want to open pycharm (y/n)?"
read res_pycharm
if echo "$res_pycharm" | grep -iq "^y" ;then
	echo "Opening PyCharm..." 
	/opt/my_apps/pycharm-community-2019.1.3/bin/pycharm.sh
fi

