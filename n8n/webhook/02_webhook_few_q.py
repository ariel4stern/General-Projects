import requests

# Same code, different URL:
url = "http://localhost:5678/webhook/chat"

# Send multiple questions in a loop
questions = [
    "What is gradient descent?",
    "Explain attention mechanism in transformers.",
    "What is overfitting and how to prevent it?",
]
for q in questions:
    r = requests.post(url, json={"message": q})
    print(f"\nQ: {q}")
    print(f'A: {r.json()["response"]}')