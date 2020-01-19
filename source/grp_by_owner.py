
def grp_by_owner(d={}):
	new_d = {}

	for k, v in d.items():
		new_l = []
		if v not in new_d.keys():
			new_l.append(k)
			new_d.update({v: new_l})
		else:
			edit_l = new_d.get(v)
			edit_l.append(k)
			new_d.update({v: edit_l})
	return new_d

d = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
print(grp_by_owner(d))

