#!/usr/bin/env python

import requests
import sys
from .query_json import API

class Pattern:
    def __init__(self, id):
        self.id = str(id)
        pat_dict = API().search_pattern(id)['pattern']
        self.free = pat_dict['free']
        self.name = pat_dict['name']
        self.downloadable = pat_dict['downloadable']
        self.weight = pat_dict['yarn_weight_description']
        self.currency = pat_dict['currency']
        self.price = pat_dict['price']
        self.categories = pat_dict['pattern_categories']
        self.attributes = pat_dict['pattern_attributes']
        self.type = pat_dict['pattern_type']
        self.notes = pat_dict['notes']
        self.craft = pat_dict['craft']
        self.photos = pat_dict['photos']
        if self.photos != []:
            self.thumbnail = self.photos[0]['thumbnail_url']
        self.sizes = pat_dict['pattern_needle_sizes']
        self.url = 'https://www.ravelry.com/patterns/library/' + self.id
        #print(self.notes)
    
    def quals(self, args = None):
        qual_dict = {}
        attribute_list = []
        for x in self.attributes:
            attribute_list.append(x['permalink'])
        qual_dict['attributes'] = attribute_list
        if 'weight' in args:
            qual_dict['weight'] = self.weight
        if 'categories' in args:
            category_list = []
            for x in self.categories:
                category_list.append(x['name'])
            qual_dict['categories'] = category_list
        return qual_dict
    



