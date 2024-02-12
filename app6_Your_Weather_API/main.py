from flask import Flask, render_template

app = Flask(__name__)


# now we need to connect html pages with that website object

# always give another / after a path

# for home page
@app.route("/")
def home():
    return render_template("home.html")  # to render html document whenever user visits website url "/home"


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": 23}  # to render html document whenever user visits website url "/home"


# but for that we need that html file in templates folder

if __name__ == "__main__":
    app.run(debug=True)
