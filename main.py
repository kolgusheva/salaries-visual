import json
import itertools
from operator import itemgetter

with open('data.json') as f:
    data = json.loads(f.read())

print len(data)

# depts = []

# for i in data:
# 	depts.append(i["Department"])
# print len(depts)

# def uniq(input):
#   output = []
#   for x in input:
#     if x not in output:
#       output.append(x)
#   return output

# new_depts = uniq(depts)

# print len(new_depts)

sorted_data = sorted(data, key=itemgetter("Department"))

data_cleared = {}
for key, group in itertools.groupby(sorted_data, lambda item: item["Department"]):
	data_cleared[key] = [item for item in group]
# COMMENT: data_cleared is a dict in which every key is a unique department  
#  name and value is a list of all people who work in that department
print len(data_cleared['Geography'])




# for x in data:
# 	if x["Department"] == "Geography":
# 		int_rate = float(x["Rate"].replace("$", "").replace(",", ""))
# 		if int_rate > 1000.00:

# 			print x["Name"], x["Rate"], int_rate
	
