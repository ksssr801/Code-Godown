import os

file_path = '/root/.aws/'
if not os.path.exists(file_path):
	os.makedirs(file_path)

make_cred_file = os.path.join(file_path, 'credentials')
make_config_file = os.path.join(file_path, 'config')

# writing credentials file
cred_file = open(make_cred_file, 'w')
to_cred_file = '[default]\naws_access_key_id = AKIAJN7ZHSRXBAHD4DMQ\naws_secret_access_key = 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'
cred_file.write(to_cred_file)
cred_file.close()

# writing config file
config_file = open(make_config_file, 'w')
to_config_file = '[default]\noutput = json\nregion = ap-south-1'
config_file.write(to_config_file)
config_file.close()

