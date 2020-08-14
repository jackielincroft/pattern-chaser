from pattern import Pattern

mega_scaling_dict = {'weight': 0.4, }

class Feelings:
    def __init__(self):
        self.settings = []
        self.prefs = {'attributes': {}, 'categories': {}, 'weights': {}}
        self.vote_counter = 0
        self.presets_query = '/patterns/search.json'

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

    def scale_prefs(self):
        copy_prefs = self.prefs
        for weight in copy_prefs['weights'].keys():
            copy_prefs['weights'][weight] = mega_scaling_dict['weight'] * copy_prefs['weights'][weight]
        for umbrella in ['attributes', 'categories']:
            for qual in copy_prefs[umbrella].keys():
                if qual in mega_scaling_dict.keys():
                    copy_prefs[umbrella][qual] = mega_scaling_dict[qual] * copy_prefs[umbrella][qual]
                else:
                    # TODO: once mega scaling dict is complete, replace this (for now, just weight everything 0.2)
                    # copy_prefs[umbrella][qual] = 0
                    copy_prefs[umbrella][qual] = 0.2 * copy_prefs[umbrella][qual]
        return copy_prefs
