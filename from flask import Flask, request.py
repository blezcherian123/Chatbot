from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse

# Set your API keys
openai.api_key = "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"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+15707838058"  # Twilio Sandbox Number

app = Flask(__name__)

# Function to send input to GPT-3.5 and get a response
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# WhatsApp Webhook Route
@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    user_input = request.form["Body"]
    response = chat_with_gpt(user_input)

    twilio_response = MessagingResponse()
    twilio_response.message(response)

    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=True)
