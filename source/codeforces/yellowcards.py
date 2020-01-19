team1 = int(input())
team2 = int(input())
yc1 = int(input())
yc2 = int(input())
total_yc = int(input())

min_count = 0
max_count = 0

total_yc_t1 = team1*yc1
total_yc_t2 = team2*yc2

if yc2 > yc1:
	rem_yc_prod_min = total_yc - total_yc_t2
	min_count = team2 + (team1 - (total_yc_t1 - rem_yc_prod_min))
else:
	rem_yc_prod_min = total_yc - total_yc_t1
	min_count = team1 + (team2 - (total_yc_t2 - rem_yc_prod_min))

if team1 > team2:
	rem_yc_prod_max = total_yc - total_yc_t1
	max_count = team1 + (rem_yc_prod_max // yc2)
else:#
	rem_yc_prod_max = total_yc - total_yc_t2
	max_count = team2 + (rem_yc_prod_max // yc1)

print (min_count, max_count)