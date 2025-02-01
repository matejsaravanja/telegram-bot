# Bot Response System

A neutral and helpful bot that acknowledges user input and invites further interaction.

## Features
1. **Neutral Responses**: Predefined list of open-ended responses.
2. **Keyword Detection**: Detects specific keywords like "bot", "hi", "hello", etc.
3. **Fallback Mechanism**: Handles ambiguous or unsupported inputs gracefully.
4. **Dynamic Responses**: Allows adding new responses or updating the fallback message.
5. **Logging**: Logs all interactions to `logs/bot_logs.log`.

## How to Run
1. Clone this repository.
2. Navigate to the project directory:
   ```bash
   cd bot_response_system
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```
4. Interact with the bot in the terminal. Type "exit" to end the conversation.

## Example
```
Bot: Hi! I'm your assistant. Type 'exit' to end the conversation.
You: Hello bot
Bot: Greetings! Feel free to ask me anything.
You: What’s the weather today?
Bot: I’m sorry, I didn’t quite understand that. Could you please rephrase or provide more details?
You: Exit
Bot: Goodbye! Have a great day.
```

## Customization
- Add new responses using the `add_response` method.
- Update the fallback response using the `update_fallback_response` method.