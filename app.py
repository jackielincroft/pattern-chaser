from flask import Flask, render_template, url_for, request
from pattern import Pattern
from feelings import Feelings
from api import API
import random

app = Flask(__name__, template_folder = 'templates')

# Global and Local Variables: -------------------------------------------------
user = Feelings()
setting_options = ['craft','weight', 'yardage', 'free', 'online', 'pc']
other_settings = ['weight','yardage','pc']
NUM_VOTES = 5

# Home Page: --------------------------------------------------------
@app.route('/')
def home():
    return render_template('home.html')

# Preferences Page: -------------------------------------------------
@app.route('/preferences')
def preferences():
    user = Feelings()
    return render_template('preferences_child.html')

# Functions used to generate an API query based on user preferences
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


# Voting Page: ------------------------------------------------------
@app.route('/vote', methods=["POST"])
def vote():
    user.vote_counter += 1

    # initial case: user has not voted yet
    if user.vote_counter <= 1:
        next_page = '/vote'
        user.presets_query = generate_query(settings())
    # general case: continue voting
    elif user.vote_counter >= 2 and user.vote_counter < NUM_VOTES:
        if request.form['votebtn'] == "love":
            hl = 1
        elif request.form['votebtn'] == "hate":
            hl = -1
        else:
            hl = 0
        user.update_prefs(Pattern(request.form['id']), hl)
        next_page = '/vote'
    # final case: go to results page
    elif user.vote_counter >= NUM_VOTES:
        next_page = '/results'
    
    # get pattern and figure out price
    pat = Pattern(random.choice(API().list_of_ids_random_pg(user.presets_query)))
    if pat.free == True:
        price_text = "This pattern is free!"
    else:
        try:
            price_text = str(pat.price)+' '+pat.currency
        except:
            price_text = 'No price listed.'

    return render_template("vote_child.html", pattern=pat, action=next_page, feels=user.prefs)

# Results Page: -----------------------------------------------------
@app.route('/results', methods=["POST"])
def results():
    # best_pats is a dictionary, where the keys are patterns and the values are likeability scores
    best_pats = {}
    
    # Get a random sample of 50 eligible patterns
    eligible_pats_ids = API().list_of_ids_random_pg(user.presets_query)
    random_sample_ids = random.sample(eligible_pats_ids, 50)

    # Go through the random sample, and find the top 5 that the user is most likely to enjoy
    for pat_id in random_sample_ids:
        pat = Pattern(pat_id)
        score = float(pat.likeability_score(user.prefs))
  
        # add first 5 scores regardless
        if len(best_pats) < 5: 
            best_pats[pat] = score
        # after first 5, only replace patterns with better ones (higher scores)
        else:
            least_best = min(best_pats.items(), key=lambda x: x[1])
            if score > least_best[1]:
                best_pats.pop(least_best[0])
                best_pats[pat] = score # add this pattern and its score

        # sort final top five
        best_pats_sorted = dict(sorted(best_pats.items(), key=lambda x: x[1], reverse=True))
 
    return render_template("results_child.html", patterns=best_pats_sorted)


if __name__ == '__main__':
    app.run()
