#!/usr/bin/env python

import requests
import sys
from api import API

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
            self.thumbnail = self.photos[0]['medium_url']
        self.sizes = pat_dict['pattern_needle_sizes']
        self.url = 'https://www.ravelry.com/patterns/library/' + self.id
        #print(self.notes)
    
    def quals(self):
        '''returns a dictionary of the qualities we care about for a given pattern of the form
        {attributes: list_of_attributes, weight: weight, category: list_of_categories}'''
        qual_dict = {}
        attribute_list = []
        category_list = []
        for x in self.attributes:
            attribute_list.append(x['permalink'])
        qual_dict['attributes'] = attribute_list
        qual_dict['weight'] = self.weight
        for x in self.categories:
            category_list.append(x['name'])
        qual_dict['categories'] = category_list
        return qual_dict

    def likeability_score(self, feels_dict):
        quals = self.quals()
        hearts_score = 0
        for umbrella in ['attributes', 'categories']:
            for smol in quals[umbrella]:
                if smol in feels_dict[umbrella].keys():
                    hearts_score += feels_dict[umbrella][smol]
        if quals['weight'] in feels_dict['weights']:
            hearts_score += feels_dict['weights'][quals['weight']]
        return hearts_score