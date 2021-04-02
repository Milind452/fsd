import urllib.request
import urllib.parse


def readText(path):
	with open(path, 'r') as quotes:
		contents = quotes.read()
		return contents

def checkProfanity(text):
	text = urllib.parse.quote(text)
	url = "http://www.wdylike.appspot.com/?q=" + text
	connection = urllib.request.urlopen(url)
	response = connection.read()
	connection.close()
	return response


if __name__ == '__main__':
	path = '/home/milind/Documents/fsd/profanity-check/movie_quotes.txt'
	contents = readText(path)
	response = checkProfanity(contents)
	print(response)