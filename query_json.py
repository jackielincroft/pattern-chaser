#!/usr/bin/env python

import requests
import sys

def main(args=None):

   if len(args) == 0:
       return 1
   username = "read-c241f228d7e954631e800f3c75ca5921"
   password = "u1PGZ8ZDPbxbogPDfSWoj+Rbbtg1twYZ+UiCoFuB"
   api = 'https://api.ravelry.com' + args[0]
   r = requests.get(api, auth=(username, password)) 
   print(type(r.json()['patterns'][0]))
   print(r.json()['patterns'][0])
   return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
