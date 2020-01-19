watch_count=524288;
file_path=/proc/sys/fs/inotify/max_user_watches

if [ -f "$file_path" ]
then
	echo "$watch_count" > "$file_path"
fi

