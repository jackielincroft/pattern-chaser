from flask import Flask, render_template, url_for
import pattern_class

app = Flask(__name__, template_folder = 'html_templates')

@app.route('/')
def home():
    pat = pattern_class.Pattern(456643)
    return render_template("linked_image.html", thumbnail = pat.thumbnail, url = pat.url, name = pat.name)

if __name__ == '__main__':
    app.run()