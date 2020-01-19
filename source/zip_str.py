# s = 'Forget  CVs..Save time . x x'
s = 'We test coders! Give us a try. afsf sfafs? asdADAD ADASD'
dot_i = []
excla_i = []
ques_i = []
splitter_list = []
dot_i = [i for i, ltr in enumerate(s) if ltr == '.']
excla_i = [i for i, ltr in enumerate(s) if ltr == '!']
ques_i = [i for i, ltr in enumerate(s) if ltr == '?']
splitter_list = dot_i + excla_i + ques_i
splitter_list.sort()
sentence_list = []
strt = 0
for index in splitter_list:
	sentence_list.append(s[strt:index])
	strt = index+1
sentence_list.append(s[strt:])
word_count_list = []
for sen in sentence_list:
	temp_sen = sen.split(' ')
	if "" in temp_sen:
		temp_sen.remove("")
	word_count_list.append(len(temp_sen))
print(max(word_count_list))