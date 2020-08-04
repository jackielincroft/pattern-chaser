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
   
   def list_of_ids(self, query):
      pat_list = self.search(query)['patterns']
      id_list = []
      for x in pat_list:
         id_list.append(x['id'])
      return id_list

   def num_pages(self, query):
      paginator = self.search(query)['paginator']
      return paginator['page_count']

x = API().num_pages('/patterns/search.json?availability=ravelry%2Bfree&craft=knitting&photo=yes&sort=best&page_size=1000')
print(x)

#craft = 'crochet'
#weight = 'cobweb'
#list_of_pats = [pattern_class.Pattern(x['id']) for x in search("/patterns/search.json?query="+craft+','+weight)['patterns']]
#print(search("/patterns/search.json?query="+craft+','+weight)['paginator'])
#for x in list_of_pats:
 #   print(x.name)