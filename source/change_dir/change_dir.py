import os

# directory name should be given for the current working directory level
def change_dir(complete_path_or_dir_name):
	cwd = os.getcwd()
	root_dir = cwd[:cwd.rfind('/')+1]
	if '/' in complete_path_or_dir_name:
		os.chdir(complete_path_or_dir_name)
	else:
		os.chdir(root_dir + '%s' % dir_name)
	changed_cwd = os.getcwd()
	# Checking if file is getting created at new changed directory.
	f = open('new_file.txt', 'w')
	f.write('This is my code.')
	f.close()

	print('cwd=>',cwd)
	print('changed_cwd=>',changed_cwd)

# insert a correct absolute path , e.g :- /home/asish/Desktop/mediff_coding_challenge/A
change_dir('/home/asish/Desktop/mediff_coding_challenge/A')
