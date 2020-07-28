from .pattern_class import Pattern

important_things = ['categories', 'weight']

class Feelings:
    def __init__(self):
        self.settings = []
        self.freedoms = ['categories', 'weight']
        self.prefs = {}

    def update_prefs(self, Pattern, hl):
        positive_qualities = Pattern.quals(self.freedoms)
        attributes = positive_qualities['attributes']
        for x in attributes:
            if x in self.prefs.keys():
                self.prefs[x] += hl
            else:
                self.prefs[x] = hl
        if 'categories' in self.freedoms:
            categories = positive_qualities['categories']
            for x in categories:
                if x in self.prefs.keys():
                    self.prefs[x] += hl
                else:
                    self.prefs[x] = hl
        if 'weight' in self.freedoms:
            weight = positive_qualities['weight']
            if weight in self.prefs.keys():
                self.prefs[x] += hl
            else:
                self.prefs[x] = hl

