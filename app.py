from flask import Flask, render_template, url_for, request
from .pattern_class import Pattern
from .feelings import Feelings
import random

app = Flask(__name__, template_folder = 'templates')
important_things = ['categories', 'weight']
user = Feelings()

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
        if pat.free == True:
            price_text = "This pattern is free!"
        else:
            price_text = str(pat.price)+' '+pat.currency
        return render_template("linked_image.html", id_num = int(pat.id), thumbnail = pat.thumbnail, url = pat.url, name = pat.name, notes = pat.notes, 
                price = price_text, craft = pat.craft['name'], weight = pat.weight, downloadable = pat.downloadable, feels = user.prefs)

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