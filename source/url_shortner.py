# Shorter the big url
# Using Permutation, i.e. 62P8, 62P7, 62P6 ..., will going to get large number of combinations.

from secrets import choice
import string

# class URLShortner:
# 	def __init__():

def url_shortner(url, short_url_length=6):
	base62 = string.ascii_lowercase + string.ascii_uppercase + string.digits # 26, 26, 10
	new_url = ''.join(choice(base62) for ch in range(short_url_length))
	return new_url


print (url_shortner('count-sum-of-digits-in-numbers-from-1-to-n'))