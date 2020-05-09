import os
from collections import OrderedDict
import json

# file_path = os.getcwd() + '/' + 'some_file.dat'
# # print file_path
# key = 'a'
# value = '2'

# if not os.path.exists(file_path):
# 	# print 'file not present.'
# 	event_dict = OrderedDict()
# 	event_dict.update({key: value})
# 	f = open('some_file.dat', 'w')
# 	f.write('%s' % event_dict)
# 	f.close()
# else:
# 	# print 'file present.'
# 	f = open('some_file.dat')
# 	event_dict = eval(f.read())
# 	# print event_dict
# 	event_dict.update({key: value})
# 	f1 = open('some_file.dat', 'w')
# 	f1.write('%s' % event_dict)
# 	f1.close()
# 	f.close()

data = {'action': 'create', 'type': 'EVENT'}

print (json.dumps(data))
