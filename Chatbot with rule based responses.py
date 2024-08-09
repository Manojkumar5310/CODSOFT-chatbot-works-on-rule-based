import time
def ask_question(question):
    print("Chatbot:", question)
    time.sleep(1)
def user_reply():
    user_input = input("You: ")
    return user_input
while True:
    question = "What's your favorite food?"
    ask_question(question)
    user_response = user_reply()
    print("Chatbot: That's interesting. Do you enjoy cooking it yourself?")
    user_response = user_reply()
    print("Chatbot: Great! Now, tell me, what's your favorite book or author?")
    user_response = user_reply()
    print("Chatbot: Thanks for sharing. Is there any place you'd like to visit someday?")
    user_response = user_reply()
    print("Chatbot: I hope you get to visit there someday! Is there anything else on your mind?")
    ask_question("Do you want to continue? (yes/no)")
    user_response = user_reply()
    if user_response.lower() != "yes":
        print("Chatbot: Okay, goodbye!")
        break
