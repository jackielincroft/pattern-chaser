from flask import Flask, render_template, url_for, request
from pattern_class import Pattern
from feelings import Feelings
from query_json import API
import random

app = Flask(__name__, template_folder = 'templates')
important_things = ['categories', 'weight']
user = Feelings()
setting_options = ['craft','weight', 'yardage', 'free', 'online', 'pc']
other_settings = ['weight','yardage','pc']
NUM_VOTES = 3

def settings():
    user_settings_dict = {}
    for x in setting_options:
        if request.form[x] != 'empty':
            user_settings_dict[x] = request.form[x]
    return user_settings_dict
def generate_query(settings_dict):
    query = '/patterns/search.json?craft='+request.form['craft']+'&photo=yes'
    if 'free' in settings_dict.keys():
        if 'online' in settings_dict.keys():
            query = query + '&availability=free%7Conline%7Cravelry%2B-discontinued'
        else:
            query = query + '&availability=free%2B-discontinued'
    else:
        query = query + '&availability=%2B-discontinued'
    for x in other_settings:
        if x in settings_dict.keys():
            query = query + '&' + x +'='+ request.form[x]
    query = query + '&page_size=100'
    return query


@app.route('/')
def home():
    user = Feelings()
    return render_template('preferences.html')

@app.route('/vote', methods=["POST"])
def button_function():
    user.update_counter()
    print(user.vote_counter)

    # initial case: user has not voted yet
    if user.vote_counter <= 1:
        next_page = '/vote'
        user_presets=generate_query(settings())
    # general case: continue voting
    elif user.vote_counter >= 2 and user.vote_counter < NUM_VOTES + 1:
        if request.form['votebtn'] == "love":
            hl = 1
        elif request.form['votebtn'] == "hate":
            hl = -1
        else:
            hl = 0
        user.update_prefs(Pattern(request.form['id']), hl)
        next_page = '/vote'
        user_presets=request.form['user_presets']
    # final case: go to results page
    elif user.vote_counter >= NUM_VOTES + 1:
        next_page = '/results'
        user_presets=request.form['user_presets']
    
    # get pattern and figure out price
    pat = Pattern(random.choice(API().list_of_ids(user_presets)))
    if pat.free == True:
        price_text = "This pattern is free!"
    else:
        try:
            price_text = str(pat.price)+' '+pat.currency
        except:
            price_text = 'No price listed.'

    return render_template("vote.html", pattern=pat, 
            user_presets = user_presets, action = next_page, feels=user.prefs)

@app.route('/results', methods=["POST"])
def results():
    # TODO: change placeholder code once we actually have an algorithm to determine recommended patterns
    pats = []
    pat1 = Pattern(random.choice(API().list_of_ids('/patterns/search.json?craft=knitting&photo=yes')))
    pat2 = Pattern(random.choice(API().list_of_ids('/patterns/search.json?craft=knitting&photo=yes')))
    pat3 = Pattern(random.choice(API().list_of_ids('/patterns/search.json?craft=knitting&photo=yes')))
    pats.append(pat1)
    pats.append(pat2)
    pats.append(pat3)
    return render_template("results.html", patterns=pats)


if __name__ == '__main__':
    app.run()

#emergency code
'''pat = Pattern(random.randint(1,1000000))
if pat.free == True:
    price_text = "This pattern is free!"
else:
    price_text = str(pat.price)+' '+pat.currency
return render_template("linked_image.html", id_num = int(pat.id), thumbnail = pat.thumbnail, url = pat.url, name = pat.name, notes = pat.notes, 
    price = price_text, craft = pat.craft['name'], weight = pat.weight, downloadable = pat.downloadable)'''