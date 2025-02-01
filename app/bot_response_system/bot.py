import random
import logging
from datetime import datetime
import os

class BotResponseSystem:
    """
    A neutral and helpful bot response system to acknowledge user input and invite further interaction.
    """

    def __init__(self):
        # Define a list of neutral, generic responses
        self.responses = [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Greetings! Feel free to ask me anything.",
            "I'm here to help! How can I assist you?"
        ]
        # Define a fallback response for ambiguous or unsupported inputs
        self.fallback_response = "I’m sorry, I didn’t quite understand that. Could you please rephrase or provide more details?"
        # Configure logging
        self._setup_logging()

    def _setup_logging(self):
        """Configures logging to a file in the 'logs' directory."""
        if not os.path.exists("logs"):
            os.makedirs("logs")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filename="logs/bot_logs.log",
            filemode="a"
        )

    def _contains_keyword(self, user_input):
        """
        Checks if the user input contains predefined keywords.
        :param user_input: The input provided by the user (string)
        :return: True if a keyword is found, otherwise False (bool)
        """
        keywords = ["bot", "hi", "hello", "hey", "greetings"]
        return any(keyword in user_input for keyword in keywords)

    def get_response(self, user_input):
        """
        Generates a response based on the user's input.
        :param user_input: The input provided by the user (string)
        :return: A neutral or fallback response (string)
        """
        try:
            # Sanitize and convert input to lowercase for case-insensitive matching
            user_input = user_input.strip().lower()

            if self._contains_keyword(user_input):
                # Return a random neutral response
                return random.choice(self.responses)
            else:
                # Fallback for ambiguous or unsupported inputs
                return self.fallback_response
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "An error occurred while processing your request. Please try again."

    def add_response(self, new_response):
        """
        Adds a new response to the bot's list of neutral responses.
        :param new_response: The new response to add (string)
        """
        if new_response not in self.responses:
            self.responses.append(new_response)
            logging.info(f"Added new response: {new_response}")

    def update_fallback_response(self, new_fallback):
        """
        Updates the bot's fallback response.
        :param new_fallback: The new fallback response (string)
        """
        self.fallback_response = new_fallback
        logging.info(f"Updated fallback response to: {new_fallback}")

    def run(self):
        """
        Runs the bot in a simple loop for interaction.
        """
        print("Bot: Hi! I'm your assistant. Type 'exit' to end the conversation.")
        while True:
            try:
                user_input = input("You: ")
                if user_input.strip().lower() == "exit":
                    print("Bot: Goodbye! Have a great day.")
                    break
                response = self.get_response(user_input)
                print(f"Bot: {response}")
            except KeyboardInterrupt:
                print("\nBot: Goodbye! Have a great day.")
                break
            except Exception as e:
                logging.error(f"Unexpected error during interaction: {e}")
                print("Bot: An unexpected error occurred. Please try again.")


# Main execution
if __name__ == "__main__":
    bot = BotResponseSystem()
    bot.run()