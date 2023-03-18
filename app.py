import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    city = request.form["city"]
    num_places = request.form["num_places"]
    num_days = request.form["num_days"]
    num_persons = request.form["num_persons"]
    budget = request.form["budget"]

    prompt = f"Suggest a plan for a trip to {city} in saudi arabia for {num_persons} people for {num_days} days. whith a budget is {budget} and I want to visit {num_places} places. and give a brief description of each, and how much i expect to spend in each place based on my budget"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    result = response.choices[0].text

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)