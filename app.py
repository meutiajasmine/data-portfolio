from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Show the portfolio homepage."""
    return render_template("index.html")


if __name__ == "__main__":
    # Debug mode is useful locally. Turn it off in production.
    app.run(debug=True)
