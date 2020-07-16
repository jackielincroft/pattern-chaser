import pattern_class
import query_json

list_of_pats = [pattern_class.Pattern(x['id']) for x in query_json.search("/patterns/search.json?query="+craft+','+weight)['patterns']]

print(list_of_pats[100].name)