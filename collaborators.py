import urllib
import feedparser
from name_normal import normalize_name

"""Returns an author's collaborators in a set"""
def returnCollaborators(author):

	# Base api query url
	base_url = 'http://export.arxiv.org/api/query?';

	# Search parameters
	search_query = 'au:%s' % author # searchs for articles authored by nebreda
	start = 0                   # retreive all results (with a maximum of 1000)
	max_results = 1000

	query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                         start,
                                                         max_results)

	# perform a GET request using the base_url and query
	response = urllib.urlopen(base_url+query).read()

	# parse the response using feedparser
	feed = feedparser.parse(response)

	# set to store the collaborators
	collaborators = set()

	# Run through each entry, and add collaborator to the set
	for entry in feed.entries:

		for person in entry.authors:

			surname = person.name.split(" ")[-1]
			collaborators.add(normalize_name(surname))

	collaborators.discard(author)
	return collaborators



    	
 
print(returnCollaborators('Nebreda'))
