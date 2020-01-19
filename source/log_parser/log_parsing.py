
f1 = open("main_debug.log","r")
file1 = open("warning.txt",'a')
file1.write('---------------WARNING-------------------\n')
for line in f1:
    find_warning = line.find('WARNING')
    if find_warning != -1:
        split_with_warning = line.split('WARNING')[1]
        file1.write(split_with_warning)
file1.close()
f1.close()




f2=open("main_debug.log","r")
file2 = open("errors.txt",'a')
file2.write('-----------------ERROR--------------------\n')
for line in f2:
    find_error = line.find('ERROR')
    if find_error != -1:
        split_with_error = line.split('ERROR')[1]
        file2.write(split_with_error)
file2.close()
f2.close()



# f2 = open("main_debug.log","r")
#     for line in f:
#         find = line.find(str2)
#         if find != -1:
#             print(line.split(str2)[1])


# for i in file:
#     file1.write()

# file2 = open("errors.txt",a)



# def warning(str1):
#     f1 = open("main_debug.log","r")
#     for line in f:
#         find = line.find(str1)
#         if find != -1:
#             print(line.split(str1)[1])


# def errors(str2):
#     f2 = open("main_debug.log","r")
#     for line in f:
#         find = line.find(str2)
#         if find != -1:
#             print(line.split(str2)[1])


# str1 = warning('WARNING')
# str2 = errors('ERROR')




