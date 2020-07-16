#!/usr/bin/env python

import requests
import sys

def search(query):

   #if len(args) == 0:
    #   return 1
   username = "read-c241f228d7e954631e800f3c75ca5921"
   password = "u1PGZ8ZDPbxbogPDfSWoj+Rbbtg1twYZ+UiCoFuB"
   api = 'https://api.ravelry.com' + query
   r = requests.get(api, auth=(username, password)) 
   #print(type(r.json()['patterns'][0]))   #use this and next line for query searches
   #print(r.json()['patterns'][0])          
   return r.json()

#if __name__ == '__main__':
 #   sys.exit(main(sys.argv[1:]))
