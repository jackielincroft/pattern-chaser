from pattern import Pattern

mega_scaling_dict = {'weight': 0.4, }

class Feelings:
    def __init__(self):
        self.settings = []
        self.prefs = {'attributes': {}, 'categories': {}, 'weights': {}}
        self.vote_counter = 0

    def update_prefs(self, pattern, hl):
        pattern_qualities = pattern.quals()
        attributes = pattern_qualities['attributes']
        categories = pattern_qualities['categories']
        weight = pattern_qualities['weight']
        for smol in attributes:
            if smol in self.prefs['attributes'].keys():
                self.prefs['attributes'][smol] += hl
            else:
                self.prefs['attributes'][smol] = hl
        for smol in categories:
            if smol in self.prefs['categories'].keys():
                self.prefs['categories'][smol] += hl
            else:
                self.prefs['categories'][smol] = hl
        if weight in self.prefs['weights'].keys():
            self.prefs['weights'][weight] += hl
        else:
            self.prefs['weights'][weight] = hl
    
    def update_counter(self):
        self.vote_counter += 1

    def scale_prefs(self):
        for weight in self.prefs['weights'].keys():
            self.prefs['weights'][weight] = mega_scaling_dict['weight'] * self.prefs['weights'][weight]
        for umbrella in ['attributes', 'categories']:
            for qual in self.prefs[umbrella].keys():
                if qual in mega_scaling_dict.keys():
                    self.prefs[umbrella][qual] = mega_scaling_dict[qual] * self.prefs[umbrella][qual]
                else:
                    self.prefs[umbrella][qual] = 0
                    #self.prefs[umbrella].pop(qual)
