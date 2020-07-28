from .pattern_class import Pattern

important_things = ['categories', 'weight']

class Feelings:
    def __init__(self):
        self.settings = []
        self.freedoms = [x in important_things if x not in self.settings]
        self.prefs = {}
        
    def update_prefs_love(self, Pattern):
        positive_qualities = Pattern.quals(self.freedoms)
        attributes = positive_qualities['attributes']
        for x in attributes:
            if x in self.prefs.keys():
                self.prefs[x] += 1
            else:
                self.prefs[x] = 1
        if 'categories' in self.freedoms:
            categories = positive_qualities['categories']
                for x in categories:
                    if x in self.prefs.keys():
                        self.prefs[x] += 1
                    else:
                        self.prefs[x] = 1
        if 'weight' in self.freedoms:
            weight = positive_qualities['weight']
                if weight in self.prefs.keys():
                    self.prefs[x] += 1
                else:
                    self.prefs[x] = 1

