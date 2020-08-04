from pattern_class import Pattern

important_things = ['categories', 'weight']

class Feelings:
    def __init__(self):
        self.settings = []
        self.prefs = {}

    def update_prefs(self, Pattern, hl):
        pattern_qualities = Pattern.quals()
        attributes = pattern_qualities['attributes']
        categories = positive_qualities['categories']
        weight = positive_qualities['weight']
        for umbrella in [categories, attributes]:
            for smol in umbrella:
                if smol in self.prefs.keys():
                    self.prefs[smol] += hl
                else:
                    self.prefs[smol] = hl
        if weight in self.prefs.keys():
            self.prefs[x] += hl
        else:
            self.prefs[x] = hl
    

