from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load a free chatbot model (BlenderBot)
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

def chat_with_model(prompt):
    response = chatbot(prompt, max_length=100, do_sample=True)
    return response[0]["generated_text"].strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_text = request.form["msg"]
    response = chat_with_model(user_text)
    return response

if __name__ == "__main__":
    app.run(debug=True)
