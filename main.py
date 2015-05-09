import json
import itertools
from operator import itemgetter
import numpy

with open('data.json') as f:
    data = json.loads(f.read())

print len(data)
 # new variable dept to iterate through depts 
 # to find out what their names are and how
 # many of them there are
depts = []

# for loop below takes all Department variables
#and put them to a list depts
for i in data:
	depts.append(i["Department"])
print len(depts)

#function below removes duplicate entries in Depts list
#leaving only unique depts in that list

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

new_depts = uniq(depts)

print len(new_depts)

sorted_data = sorted(data, key=itemgetter("Department"))

data_cleared = {}
for key, group in itertools.groupby(sorted_data, lambda item: item["Department"]):
	data_cleared[key] = [item for item in group]
# data_cleared is a dict in which every key is a unique department  
# name, and value is a list of dicts of all individuals who work in that department



def getMeanHighest(stream):
	total = 0
	highest = []
	for x in stream:
		rate = float(x["Rate"].replace("$", "").replace(",", ""))
		highest.append(rate)
		total = total + rate
	people = len(stream)
	mean = total / people
	real_highest = max(highest)
	return [mean, real_highest]

supernewdata = []

for key, value in data_cleared.iteritems():
	mean_highest = getMeanHighest(value)
	newshit = {"name":key,"y":mean_highest[0],"x":mean_highest[1]}
	supernewdata.append(newshit)


with open('result.json', 'w') as fp:
    json.dump(supernewdata, fp)







# a = []

# a = data_cleared['Geography']

# # print [a]
# print a[0]

# for x in a:
# 	int_rate = float(x["Rate"].replace("$", "").replace(",", ""))
# 	print x["Rate"]

# a_rates = []

# for i in a:
# 	a_rates.append(i["Rate"])
# print a_rates

# print numpy.mean(a['Rate'])

# with open('result.json', 'w') as fp:
#     json.dump(data_cleared, fp)




# for x in data:
# 	if x["Department"] == "Geography":
# 		int_rate = float(x["Rate"].replace("$", "").replace(",", ""))
# 		if int_rate > 1000.00:

# 			print x["Name"], x["Rate"], int_rate
	
