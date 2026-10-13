# Rule-Based Chatbot

A Python chatbot with a Streamlit chat interface. It uses predefined rules to answer selected questions about greetings, general knowledge, education, entertainment, dates, and basic arithmetic.

> **Project type:** Rule-based chatbot, not a generative AI assistant.

## Features

- Interactive chat interface with message history
- Category-wise suggested questions in the sidebar
- Predefined responses organized by category
- Support for suggested questions and manually entered queries
- Basic arithmetic with `+`, `-`, `*`, and `/`
- Date response, help command, and fallback response
- Handles empty input and division by zero
- Create new conversations and revisit previous chats
- Persistent conversation history using SQLite
- Conversation titles and message history management
- Option to clear messages from the current conversation
- Unit tests for key behaviours

## Project Structure

```text
Rule-Based-Chatbot/
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_chatbot.py
```

## Setup (Python 3.10+)

Create a virtual environment (optional) using Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run the Web App

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Run Tests

```powershell
python -m unittest discover -s tests
```

## Example Prompts

The sidebar organizes suggested questions into categories to make it easier to interact with the chatbot.

- **Greetings:** `hello`
- **General Knowledge:** `what is gravity`
- **Education & Technology:** `what is Python`
- **Entertainment:** `tell me a joke`
- **Basic Arithmetic:** `what is 25 + 37`
- **Date:** `what day is it today`
- **Help:** `help`

Users can select a suggested question from the relevant category or enter their own query through the chat interface.

*Note: Example prompts should match the questions and categories defined in `chatbot.py` and displayed in the application.*

## How It Works

1. Normalize user input to lowercase and consistent whitespace.
2. Check exit and help commands.
3. Detect basic arithmetic using a regular expression.
4. Check date-related questions and predefined response categories.
5. Return a matching response or a fallback response if no rule matches.
6. Display responses in the Streamlit chat interface and maintain conversation history.

## Persistent Conversation History

The application uses SQLite to store conversations and messages locally. Users can start new conversations, revisit previous chats, and manage or clear messages in the current conversation. Conversation data persists across application restarts.

## Limitations

- Only supported questions and predefined phrases are answered, except calculator matching.
- The chatbot does not learn from conversations or generate new knowledge.
- Arithmetic is limited to whole numbers and basic operators.
- The date response uses the computer's local date.

## Future Improvements

- Add more intents and phrase variations.
- Move responses to a JSON knowledge base.
- Expand tests and deploy the application publicly.

**Technologies:** Python, Streamlit, SQLite, Regular Expressions.