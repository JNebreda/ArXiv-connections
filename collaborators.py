"""Returns an author's collaborators in a set"""
import urllib
import feedparser
from name_normal import normalize_name

def fetchCollaborators(author):

  # Base api query url
  base_url = 'http://export.arxiv.org/api/query?';

  # Search parameters
  searchTerm = "\""+author+"\"" 
  search_query = 'au:%s' % searchTerm # search for articles authored by nebreda
  start = 0                   # retreive all results (with a maximum of 1000)
  max_results = 300

  query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                         start,
                                                         max_results)

  # perform a GET request using the base_url and query
  response = urllib.urlopen(base_url+query).read()

  # parse the response using feedparser
  feed = feedparser.parse(response)

  # set to store the collaborators
  collaborators = set()  

  print(len(feed['entries']))
  if len(feed['entries']) < max_results:

    # Run through each entry, and add collaborator to the set
    for entry in feed.entries:

      for person in entry.authors:

        # surname = person.name.split(" ")[-1]
        surname = normalize_name(person.name)
        if surname:
          collaborators.add(surname)

    collaborators.discard(author)
  return collaborators


class authorTree():

  def __init__(self, rootObj=None):
    self.root = rootObj
    self.children = {}

  def addCollaborator(self, name):
    self.children[name] = authorTree(name)

  def addAllCollaborators(self):
    col = fetchCollaborators(self.root)
    for person in col:
      self.addCollaborator(person)

  def addNlevels(self,N):
    self.addAllCollaborators()
    for child in self.getCollaborators():
      print('------'+child)
      childTree = authorTree(child)
      childTree.addAllCollaborators()
      self.children[child] = childTree
      print(childTree.getCollaborators())


  def getCollaborators(self):
    return self.children.keys()
    	
  
myTree = authorTree("J Nebreda")
myTree.addNlevels(1)
#myTree.addAllCollaborators()
#print(myTree.getCollaborators())
#print(myTree.children["Elvira"].getCollaborators())
