import random

# Define responses
greeting_responses = ["Hello, sir.", "Greetings, user.", "Good day."]
goodbye_responses = ["Goodbye, sir.", "Farewell, user.", "Until next time."]
fallback_responses = ["I'm sorry, I cannot assist with that.", "I'm still learning, sir.", "I don't have information on that topic."]
app_responses = {
    "open": "Opening {}...",
    "close": "Closing {}...",
    "not_found": "I couldn't find that application."
}

# Basic conversation loop
def chat():
    print("J.A.R.V.I.S.: Good day, sir. How may I assist you?")
    while True:
        user_input = input("You: ").lower()
        if any(keyword in user_input for keyword in ["bye", "exit"]):
            print("J.A.R.V.I.S.:", random.choice(goodbye_responses))
            break
        elif "open" in user_input:
            app_name = extract_app_name(user_input)
            if app_name:
                open_app(app_name)
                print("J.A.R.V.I.S.:", app_responses["open"].format(app_name))
            else:
                print("J.A.R.V.I.S.:", app_responses["not_found"])
        elif "close" in user_input:
            app_name = extract_app_name(user_input)
            if app_name:
                close_app(app_name)
                print("J.A.R.V.I.S.:", app_responses["close"].format(app_name))
            else:
                print("J.A.R.V.I.S.:", app_responses["not_found"])
        else:
            response = generate_response(user_input)
            print("J.A.R.V.I.S.:", response)

# Extract the app name from the user input
def extract_app_name(input_text):
    app_name_keywords = ["open", "close"]
    for keyword in app_name_keywords:
        if keyword in input_text:
            app_name = input_text.split(keyword)[-1].strip()
            return app_name.capitalize()  # Convert to title case
    return None

# Open the selected app
def open_app(app_name):
    if app_name.lower() == "youtube":
        print("Opening YouTube...")  # Simulated opening YouTube
    else:
        # Handle other applications as needed
        pass

# Close the selected app
def close_app(app_name):
    # Handle closing an application
    pass

# Generate a response based on user input
def generate_response(input_text):
    if any(keyword in input_text for keyword in ["hi", "hello"]):
        return random.choice(greeting_responses)
    else:
        return random.choice(fallback_responses)

# Start the conversation
chat()