#!/usr/bin/env python

import requests
import sys

class Pattern:
    def __init__(self, id):
        id = str(id)
        username = "read-c241f228d7e954631e800f3c75ca5921"
        password = "u1PGZ8ZDPbxbogPDfSWoj+Rbbtg1twYZ+UiCoFuB"
        api = 'https://api.ravelry.com/patterns/' + id + '.json'
        r = requests.get(api, auth=(username, password)) 
        pat_dict = r.json()['pattern']
        self.free = pat_dict['free']
        self.name = pat_dict['name']
        self.downloadble = pat_dict['downloadable']
        self.weight = pat_dict['yarn_weight_description']
        self.currency = pat_dict['currency']
        self.price = pat_dict['price']
        self.catagories = pat_dict['pattern_categories']
        self.attributes = pat_dict['pattern_attributes']
        self.type = pat_dict['pattern_type']
        self.notes = pat_dict['notes']
        self.craft = pat_dict['craft']
        self.photos = pat_dict['photos']
        self.thumbnail = self.photos[0]['thumbnail_url']
        print(self.notes)
        #print(r.json()['pattern'])
