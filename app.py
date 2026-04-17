from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# =========================
# STEP 2: HOMEPAGE ROUTE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# STEP 3: PLACEHOLDER ROUTES (NOT IMPLEMENTED YET)
# =========================

@app.route("/predict")
def predict():
    return "Prediction page will be built in next step."


@app.route("/search_predict")
def search_predict():
    return "Search prediction will be built in next step."


@app.route("/compare")
def compare():
    return "Comparison page will be built later."


@app.route("/visualize")
def visualize():
    return "Visualization page will be built later."


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)