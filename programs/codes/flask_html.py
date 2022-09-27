from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = "Tim"
    favorite_food = ["Pizza", "Chicken Rise", "Eggs"]
    return render_template("index.html", Name=name, favorite_food=favorite_food)


@app.route('/api/<name>', methods=['GET'])
def page(name):
    return render_template("user.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)
