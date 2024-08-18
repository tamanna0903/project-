import random
import re

class SupportBot:

    negative_responses = ("no", "NO")  
    exit_commands = ("quit", "exit", "bye", "abort")

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\s*product.*',
            'technical_support': r'.*technical.*support.*',
            'about_returns': r'.*\s*return policy.*',
            'general_query': r'.*how.*help.*'
        }

    def welcome(self):
        self.name = input("HELLO! WELCOME TO OUR CUSTOMER SUPPORT. WHAT IS YOUR NAME?\n")
        will_help = input(f"Hi {self.name}, how can I help you?\n").lower()
        if will_help in self.negative_responses:
            print("ALRIGHT, HAVE A GOOD DAY!")
            return
        self.chat()

    def exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("THANK YOU FOR REACHING US. HAVE A GOOD DAY!")
                return True
        return False

    def chat(self):
        reply = input("Please tell me, what do you want to know: ").lower()
        while not self.exit(reply):
            reply = input(self.replies(reply)).lower()  # Ensure case-insensitivity

    def replies(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            match = re.search(regex_pattern, reply)
            if match:
                if intent == 'ask_about_product':
                    return self.ask_about_product()
                elif intent == 'technical_support':
                    return self.technical_support()
                elif intent == 'about_returns':
                    return self.about_returns()
                elif intent == 'general_query':
                    return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = ("Our products are the best and also get excellent reviews.\n",
                     "You can find the products on our website.\n")
        return random.choice(responses)

    def technical_support(self):
        responses = ("You can visit our TECHNICAL SUPPORT site for more details.\n",
                     "Call on our TECHNICAL SUPPORT helpline number +1800 111 1111 222 for immediate help.")
        return random.choice(responses)

    def about_returns(self):
        responses = ("We have a 30-day return policy.\n",
                     "PLEASE CHECK WHETHER THE PRODUCT IS IN ITS ORIGINAL CONDITION OR NOT BEFORE APPLYING FOR THE POLICY!!\n")
        return random.choice(responses)

    def general_query(self):
        responses = ("How can I help you further?\n",
                     "Is there anything else you want to know?\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Sorry, I didn't understand. Can you type it again?\n",
                     "My apologies, can you give me more details?\n")
        return random.choice(responses)

# Create the bot instance and start the conversation
bot = SupportBot()
bot.welcome()
