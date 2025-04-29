# AI Customer Service Agent

## Features

- Greet the user
- Answer 5 FAQs
- Provide basic order status (mocked)
- Collect customer contact info (name + email)
- Escalate to human for unknown questions
- Handle small talk ("Hi", "Thank you", "Bye")
- Provide feedback option
- Clean, simple UI

## Setup Instructions

1. Install requirements:
    ```
    pip install flask transformers
    ```

2. Run the app:
    ```
    python app.py
    ```

3. Open your browser at `http://127.0.0.1:5000/`.

## Assumptions

- Contact info is inferred from phrases like: "My name is John and my email is john@example.com".
- Order status is mocked with a single order ID.
