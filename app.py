from flask import Flask, render_template, url_for, request
from pattern_class import Pattern
from feelings import Feelings
import random

app = Flask(__name__, template_folder = 'templates')
important_things = ['categories', 'weight']
user = Feelings()
setting_options = ['craft','weight', 'yardage', 'free', 'online', 'pc']
other_settings = ['weight','yardage','pc']

def settings():
    user_settings_dict = {}
    for x in setting_options:
        if request.form[x] != 'empty':
            user_settings_dict[x] = request.form[x]
    return user_settings_dict
def generate_query(settings_dict):
    query = 'craft='+request.form['craft']
    if 'free' in settings_dict.keys():
        if 'online' in settings_dict.keys():
            query = query + '&availability=free%7Conline%7Cravelry%2B-discontinued'
        else:
            query = query + '&availability=free%2B-discontinued'
    else:
        query = query + 'availability=&%2B-discontinued'
    for x in other_settings:
        if x in settings_dict.keys():
            query = query + '&' + x +'='+ request.form[x]
    return query


@app.route('/')
def home():
    return render_template('settings.html')

@app.route('/vote', methods=["POST"])
def button_function():
    try:
        if request.form['votebtn'] == "love":
            hl = 1
        elif request.form['votebtn'] == "hate":
            hl = -1
        else:
            hl = 0
        user.update_prefs(Pattern(request.form['id']), hl)
    finally:
        pat = Pattern(random.randint(1,1000000))
        try:
            if pat.free == True:
                price_text = "This pattern is free!"
            else:
                price_text = str(pat.price)+' '+pat.currency
        except:
            price_text = 'No price listed.'
        return render_template("linked_image.html", id_num = int(pat.id), thumbnail = pat.thumbnail, url = pat.url, name = pat.name, notes = pat.notes, 
                price = price_text, craft = pat.craft['name'], weight = pat.weight, downloadable = pat.downloadable, feels = generate_query(settings()))

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