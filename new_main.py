import json
import itertools
from operator import itemgetter
import math

with open('data.json') as f:
    data = json.loads(f.read())

sorted_data = sorted(data, key=itemgetter("Department"))

data_cleared = {}
for key, group in itertools.groupby(sorted_data, lambda item: item["Department"]):
	data_cleared[key] = [item for item in group]

def getMeanHighest(stream):
	total = 0
	salaries = []
	for x in stream:
		rate = float(x["Rate"].replace("$", "").replace(",", ""))
		if rate > 1000.00:
			salaries.append(rate)
			total = total + rate
	people = len(stream)
	mean = total / people
	try:
		real_highest = max(salaries)
		return [mean, real_highest]
	except ValueError:
		return False

supernewdata = []

for key, value in data_cleared.iteritems():
	mean_highest = getMeanHighest(value)
	if mean_highest is not False:
		export_dict = {"name":key,"y":int(mean_highest[0]),"x":int(mean_highest[1])}
		supernewdata.append(export_dict)


with open('result.json', 'w') as fp:
    json.dump(supernewdata, fp)