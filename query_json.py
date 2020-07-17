#!/usr/bin/env python
import requests
import sys

class API:
   def __init__(self, username="read-c241f228d7e954631e800f3c75ca5921", password="u1PGZ8ZDPbxbogPDfSWoj+Rbbtg1twYZ+UiCoFuB", url='https://api.ravelry.com'):
      self.username = username
      self.password = password
      self.url = url

   def search(self, query):
      r = requests.get(self.url + query, auth=(self.username, self.password))
      return r.json()
   
   def search_pattern(self, id):
      r = requests.get(self.url + '/patterns/' + str(id) + '.json', auth=(self.username, self.password))
      return r.json()


#craft = 'crochet'
#weight = 'cobweb'
#list_of_pats = [pattern_class.Pattern(x['id']) for x in search("/patterns/search.json?query="+craft+','+weight)['patterns']]
#print(search("/patterns/search.json?query="+craft+','+weight)['paginator'])
#for x in list_of_pats:
 #   print(x.name)