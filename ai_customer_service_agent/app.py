from flask import Flask, render_template, request, session
from transformers import pipeline

app = Flask(__name__)
app.secret_key = 'secret123'  # Needed for session

# Chatbot model (BlenderBot)
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

# Rule-based FAQ and order status logic
faq_responses = {
    "what are your hours?": "We're open 9am–5pm, Monday to Friday.",
    "how can i return an item?": "You can return any item within 30 days of purchase with a receipt.",
    "how do i contact support?": "You can contact support at support@example.com.",
    "do you ship internationally?": "Yes, we ship to most countries worldwide.",
    "what payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and Apple Pay."
}

def chat_with_model(prompt):
    prompt_lower = prompt.lower()

    # Small talk
    if prompt_lower in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"
    elif prompt_lower in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    elif prompt_lower in ["thank you", "thanks"]:
        return "You're welcome! Let me know if there's anything else I can help with."

    # FAQ
    if prompt_lower in faq_responses:
        return faq_responses[prompt_lower]

    # Order status
    if "order" in prompt_lower and "status" in prompt_lower:
        return "Your order #12345 is currently being processed and will arrive by May 3."

    # Contact collection
    if "my name is" in prompt_lower and "@" in prompt_lower:
        session["contact"] = prompt
        return "Thank you! We've saved your contact info."

    # Feedback
    if prompt_lower in ["yes", "no"] and session.get("feedback_requested"):
        session.pop("feedback_requested", None)
        return "Thanks for your feedback!"

    # Request feedback
    if "helpful" in prompt_lower:
        session["feedback_requested"] = True
        return "Was this conversation helpful? Please reply 'yes' or 'no'."

    # Fallback
    return "I'm not sure how to help with that. Let me connect you to a human agent."

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
