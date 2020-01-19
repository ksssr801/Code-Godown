import math

global added_num
added_num = 0
def add_digit(num):
    global added_num
    f = 0
    new_l = map(int, map(str, str(num)))
    new_num = sum(new_l)
    num_len = len(str(new_num))
    if num_len == 1:
        added_num = new_num
    else:
        add_digit(new_num)

def is_prime(a):
    f = 0;
    sq_rt = int(math.sqrt(a))
    if a<2:
        return False
    else:
        for i in xrange(2, sq_rt+1):
            if a%i == 0:
                f=1
                break
    if f==0:
        return True
    else:
        return False


add_digit(12)
print added_num
print is_prime(added_num)
