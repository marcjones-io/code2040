#marc kaivon jones
#code2040 fellowship program technical assessment

import json, urllib2, datetime

get_data = {'token' : '77628cdf2967e05ee008559b25e7d010'}

def request(url, data):
	request = urllib2.Request(url)
	request.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(request, json.dumps(data))
	return response.read()

def step1(): #registration
	registration_url = 'http://challenge.code2040.org/api/register'
	registration_data = {'token': '77628cdf2967e05ee008559b25e7d010', 'github': 'https://github.com/marcjones-io/code2040.git'}
	response = request(registration_url,registration_data)
	print response

def step2(): #reverse string
	reverse_url = 'http://challenge.code2040.org/api/reverse'
	string_to_reverse = request(reverse_url, get_data)

	reversed_string = string_to_reverse[::-1]

	validate_url = 'http://challenge.code2040.org/api/reverse/validate'
	validate_data = {'token' : '77628cdf2967e05ee008559b25e7d010', 'string':reversed_string}
	response = request(validate_url, validate_data)
	print response

def step3(): #needle in haystack
	needle_url = 'http://challenge.code2040.org/api/haystack'
	dataset = request(needle_url, get_data)

	needle = dataset[10 : dataset.find(",\"h")-len(dataset)]
	haystack = dataset[dataset.find(":[")+2:len(dataset)-2].split(',')

	validate_url = 'http://challenge.code2040.org/api/haystack/validate'
	validate_data = {'token' : '77628cdf2967e05ee008559b25e7d010', 'needle':haystack.index(needle)}
	response = request(validate_url, validate_data)
	print response

def step4(): #prefix
	prefix_url = 'http://challenge.code2040.org/api/prefix'
	dataset = request(prefix_url, get_data)

	prefix = dataset[10 : dataset.find(",\"a")-len(dataset)].strip("\"")
	array = dataset[dataset.find(":[")+2:len(dataset)-2].split(',')

	array = [i.strip("\"") for i in array]
	array = [i for i in array if i.find(prefix)]

	validate_url = 'http://challenge.code2040.org/api/prefix/validate'
	validate_data = {'token' : '77628cdf2967e05ee008559b25e7d010', 'array':	array}
	response = request(validate_url, validate_data)
	print response

def step5(): #dating game
	dating_url = 'http://challenge.code2040.org/api/dating'
	dataset = request(dating_url, get_data)

	datestamp = dataset[14 : dataset.find("Z")-len(dataset)].strip("\"")
	interval = dataset[dataset.find("l\":")+3:-1]

	formatting = "%Y-%m-%d %H:%M:%S"
	datestamp = datetime.datetime.strptime(datestamp[:10]+" "+datestamp[11:21], formatting)
	newdate = datestamp + datetime.timedelta(seconds = int(interval))
	newdate = newdate.isoformat()+'Z'

	validate_url = 'http://challenge.code2040.org/api/dating/validate'
	validate_data = {'token' : '77628cdf2967e05ee008559b25e7d010', 'datestamp' : newdate}
	response = request(validate_url, validate_data)
	print response


step1()
step2()
step3()
step4()
step5()