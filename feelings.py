from pattern_class import Pattern

important_things = ['categories', 'weight']

class Feelings:
    def __init__(self):
        self.settings = []
        self.prefs = {}
        self.vote_counter = 0

    def update_prefs(self, Pattern, hl):
        pattern_qualities = Pattern.quals()
        attributes = pattern_qualities['attributes']
        categories = pattern_qualities['categories']
        weight = pattern_qualities['weight']
        for umbrella in [categories, attributes]:
            for smol in umbrella:
                if smol in self.prefs.keys():
                    self.prefs[smol] += hl
                else:
                    self.prefs[smol] = hl
        if weight in self.prefs.keys():
            self.prefs[weight] += hl
        else:
            self.prefs[weight] = hl
    
    def update_counter(self):
        self.vote_counter += 1
    

