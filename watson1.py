print('')
print('Say hello to the ultimate jeopardy player.', 
	'Enter any jeopardy "answer" to see his response. Enter "exit" to exit the program.')
print('')

def remove_common(string):
	common = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'for', 'at']
	words = string.lower().split()
	without_common = words[:]

	for word_i in without_common:
		if word_i in common:
			without_common.remove(word_i)

	return without_common


def check_for_overlap_of_strings(string1, string2):
	if string2.split()[0:2] == ['List', 'of']:
		return False

	words1 = remove_common(string1)
	words2 = remove_common(string2)

	for word_j in words1:
		if word_j in words2:
			words2.remove(word_j)

	return words2

q = input("Jeopardy Answer: ")
while q!='exit':
	import json
	import urllib.request, urllib.parse

	def showsome(searchfor):
	  query = urllib.parse.urlencode({'q': searchfor + ' site:Wikipedia.org'})
	  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	  search_response = urllib.request.urlopen(url)
	  search_results = search_response.read().decode("utf8")
	  results = json.loads(search_results)
	  data = results['responseData']
	  hits = data['results']

	  i = 0
	  answer = q
	  while not check_for_overlap_of_strings(q, answer):
	  	first = hits[i]
	  	answer = first['titleNoFormatting'].replace('- Wikipedia, the free encyclopedia', '')
	  	i+=1

	  print('What is', answer)

	showsome(q)

	print('')
	q = input("Jeopardy Answer: ")
