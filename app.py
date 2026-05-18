from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

chatbot = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        result = chatbot(
            question,
            max_length=150,
            do_sample=True,
            temperature=0.7
        )

        answer = result[0]["generated_text"]

    return render_template(
        "index.html",
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)
