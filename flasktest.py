from flask import Flask, render_template, url_for
import pattern_class
import random

app = Flask(__name__, template_folder = 'html_templates')

@app.route('/')
def home():
    pat = pattern_class.Pattern(random.randint(1,1000000))
    if pat.free == True:
        return render_template("linked_image.html", thumbnail = pat.thumbnail, url = pat.url, name = pat.name, notes = pat.notes, price = "This pattern is free!", craft = pat.craft['name'], weight = pat.weight, downloadable = pat.downloadable)
    else:
        return render_template("linked_image.html", thumbnail = pat.thumbnail, url = pat.url, name = pat.name, notes = pat.notes, price = str(pat.price)+' '+pat.currency, craft = pat.craft['name'], weight = pat.weight, downloadable = pat.downloadable)

if __name__ == '__main__':
    app.run()