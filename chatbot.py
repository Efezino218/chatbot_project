import random
import json
import os

from error_handling import ErrorHandler


class Chatbot:
    def __init__(self):
        self.responses = self.load_responses()

    def load_responses(self):
        # Get the directory path of the current Python script
        script_dir = os.path.dirname(__file__)
        # Construct the full path to the responses.json file
        file_path = os.path.join(script_dir, "responses.json")

        with open(file_path, "r") as file:
            return json.load(file)

    def greet(self):
        print("Chatbot: " + random.choice(self.responses["greetings"]))

    def respond_to_response(self, user_input):
        if "fine" in user_input and "thank you" in user_input:
            print("Chatbot: That's fine, thank you!")
        elif "how about you" in user_input or "and you" in user_input:
            print("Chatbot: Am fine too, thanks for asking!")
        elif "it's been a while" in user_input or "longest time" in user_input:
            print("Chatbot: Yeah, all good. It's nice to chat with you again!")
        elif "how are you" in user_input:
            print("Chatbot: Fine thank you!")
        else:
            print("Chatbot: " + random.choice(self.responses["responses_neutral"]))

    def ask_how_are_you(self):
        print("Chatbot: " + random.choice(self.responses["how_are_you"]))

    def respond_to_feeling(self, user_input):
        if "fine" in user_input or "good" in user_input or "great" in user_input:
            print("Chatbot: " + random.choice(self.responses["responses_fine"]))
        elif "not good" in user_input or "bad" in user_input:
            print("Chatbot: " + random.choice(self.responses["responses_not_so_good"]))
        else:
            self.respond_to_response(user_input)

    def engage_in_conversation(self):
        self.greet()
        while True:
            try:
                user_input = input("You: ").lower()
                if user_input == "exit":
                    print("Chatbot: " + random.choice(self.responses["farewell"]))
                    break
                elif any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
                    self.ask_how_are_you()
                else:
                    self.respond_to_feeling(user_input)
            except Exception as e:
                ErrorHandler.handle_error()


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.engage_in_conversation()
