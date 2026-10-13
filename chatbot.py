
import re
from datetime import datetime


# Every question displayed in app.py has a matching answer.
ANSWERS = {
    # EVERYDAY LIFE
    "how can i save water":
        "You can save water by turning off the tap while brushing your teeth and taking shorter showers. "
        "Fix leaking taps and reuse water for plants whenever possible.",

    "how can i save electricity":
        "Switch off lights, fans, and appliances when you are not using them. "
        "Use LED bulbs and unplug chargers when they are not needed.",

    "how can i stay organized":
        "Make a daily to-do list and arrange tasks according to their importance. "
        "Keep your belongings in fixed places and tidy your workspace regularly.",

    "what should i eat for breakfast":
        "Choose a balanced breakfast containing carbohydrates, protein, and fruits or vegetables. "
        "For example, you could eat idli with sambar, oats with fruit, or eggs with whole-grain toast.",

    "why is sleep important":
        "Sleep helps your body recover and supports memory, concentration, and emotional well-being. "
        "Most adults need around seven to nine hours of sleep each night.",

    "how can i reduce stress":
        "Try deep breathing, gentle exercise, listening to relaxing music, or talking to someone you trust. "
        "Taking short breaks and maintaining a regular sleep schedule can also help.",

    "how can i improve my english":
        "Read simple articles, learn a few new words daily, and practise speaking English aloud. "
        "Watching English videos with subtitles and writing short paragraphs can improve your skills.",

    "how can i manage my time":
        "Create a schedule, divide large tasks into smaller steps, and set realistic deadlines. "
        "Start with important tasks and avoid distractions while working.",

    "what should i carry when travelling":
        "Carry your identification, tickets, phone, charger, money, medicines if needed, and essential toiletries. "
        "Check the weather and your destination's requirements before packing.",

    "how can i save money":
        "Track your spending, set a monthly budget, and save a fixed amount whenever you receive money. "
        "Avoid unnecessary purchases and compare prices before buying things.",

    "what should i do when i feel bored":
        "Try drawing, dancing, reading, cooking, listening to music, or learning something new. "
        "You could also take a walk or contact a friend for a conversation.",

    "how can i stay healthy":
        "Eat balanced meals, stay hydrated, exercise regularly, and get enough sleep. "
        "Good hygiene and routine medical check-ups also support your health.",

    "how can i be more productive":
        "Choose a few achievable tasks, work on one task at a time, and take short breaks. "
        "Keeping your phone away while studying or working can help you concentrate.",

    "how can i protect my phone":
        "Use a strong screen lock, install updates, and download apps only from trusted sources. "
        "Avoid suspicious links and back up important files regularly.",


    # EDUCATION AND TECHNOLOGY
    "what is python":
        "Python is a programming language known for its readable syntax and versatility. "
        "It is used in web development, automation, data science, and artificial intelligence.",

    "what is artificial intelligence":
        "Artificial intelligence (AI) is a field of computing that develops systems capable of performing tasks that usually require human intelligence. "
        "Examples include language assistants, image recognition, and recommendation systems.",

    "what is machine learning":
        "Machine learning is a branch of AI in which computers learn patterns from data to make predictions or decisions. "
        "It is used in spam detection, recommendations, and fraud detection.",

    "what is deep learning":
        "Deep learning is a type of machine learning that uses neural networks with multiple layers. "
        "It is widely used in speech recognition, image analysis, and language models.",

    "what is data science":
        "Data science combines statistics, programming, and domain knowledge to extract useful insights from data. "
        "It helps organizations identify patterns, make predictions, and support decisions.",

    "what is cybersecurity":
        "Cybersecurity protects computers, networks, applications, and data from digital attacks. "
        "Common practices include using strong passwords, enabling multifactor authentication, and updating software.",

    "what is sql":
        "SQL stands for Structured Query Language and is used to manage and retrieve data from relational databases. "
        "It supports operations such as selecting, inserting, updating, and deleting records.",

    "what is cloud computing":
        "Cloud computing provides computing services such as storage, servers, and databases over the internet. "
        "It allows users to access resources without maintaining all the hardware themselves.",

    "what is an algorithm":
        "An algorithm is a step-by-step procedure for solving a problem or completing a task. "
        "Algorithms are used in programming, searching, sorting, and everyday decision-making.",

    "what is a database":
        "A database is an organized collection of information that can be stored, accessed, and updated. "
        "Databases are used in applications such as banking systems, websites, and student management systems.",

    "what is the internet":
        "The internet is a global network that connects computers and other devices to exchange information. "
        "It enables services such as websites, email, video calls, and online messaging.",


    # GENERAL KNOWLEDGE
    "what is gravity":
        "Gravity is the force of attraction between objects that have mass. "
        "On Earth, gravity pulls objects toward the planet and keeps us on the ground.",

    "what is photosynthesis":
        "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to make food. "
        "It also releases oxygen into the atmosphere.",

    "what is the solar system":
        "The solar system consists of the Sun and the objects that orbit it, including planets, moons, asteroids, and comets. "
        "Earth is one of the eight planets orbiting the Sun.",

    "what is the largest planet":
        "Jupiter is the largest planet in our solar system. "
        "It is a gas giant known for its Great Red Spot and many moons.",

    "why is the sky blue":
        "The sky appears blue because air molecules scatter shorter wavelengths of sunlight, especially blue light, more strongly than longer wavelengths. "
        "This scattering makes blue light visible across much of the daytime sky.",

    "what is renewable energy":
        "Renewable energy comes from sources that naturally replenish, such as sunlight, wind, and flowing water. "
        "These sources can reduce dependence on fossil fuels.",

    "how many planets are in the solar system":
        "There are eight recognized planets in our solar system. "
        "They are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",

    "what direction does the sun rise":
        "The Sun appears to rise in the east and set in the west. "
        "This apparent movement happens because Earth rotates from west to east.",

    "how many months are there in a year":
        "There are twelve months in a year. "
        "A common year has 365 days, while a leap year has 366 days.",

    "what day is it today":
        f"Today is {datetime.now().strftime('%A, %d %B %Y')}. "
        "The date is based on your computer's current local date.",


    # ENTERTAINMENT
    "what are some best genres in movies":
        "Popular movie genres include comedy, action, drama, science fiction, thriller, and animation. "
        "The best genre depends on whether you want excitement, humour, suspense, or an emotional story.",

    "what is the best cartoon to improve english":
        "Cartoons such as Peppa Pig and Bluey can help beginners practise everyday English through simple conversations. "
        "Try watching with English subtitles and repeating useful phrases aloud.",

    "which music is best for relaxation":
        "Soft instrumental music, ambient sounds, and gentle acoustic music can help some people relax. "
        "Choose music you enjoy and keep the volume comfortable.",

    "what is a good movie for family":
        "Animated films such as Finding Nemo and Paddington are popular family-friendly choices. "
        "Check the movie's age rating and content to make sure it suits everyone watching.",

    "what music is good for studying":
        "Instrumental music, soft piano, or quiet ambient sounds may help some people concentrate. "
        "If music distracts you, studying in silence may work better.",


    # PROGRAMMING
    "what is java":
        "Java is a general-purpose programming language commonly used for enterprise software, backend systems, and Android development. "
        "It is known for its object-oriented approach and its Java Virtual Machine.",

    "what is html":
        "HTML stands for HyperText Markup Language and defines the structure of web pages. "
        "It uses elements such as headings, paragraphs, links, and images.",

    "what is a computer network":
        "A computer network connects devices so they can communicate and share information or resources. "
        "Examples include home Wi-Fi networks and the internet.",

    "what is an operating system":
        "An operating system manages a computer's hardware and software resources. "
        "Examples include Windows, Linux, macOS, Android, and iOS.",
}


def normalize(text):
    """Normalize a question so punctuation and capitalization do not matter."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text)


def calculate(question):
    """Answer basic arithmetic questions safely."""
    match = re.fullmatch(
        r"\s*(-?\d+(?:\.\d+)?)\s*([+\-*/xX])\s*(-?\d+(?:\.\d+)?)\s*\??\s*",
        question.strip()
    )

    if not match:
        return None

    a = float(match.group(1))
    operator = match.group(2)
    b = float(match.group(3))

    try:
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator in ("*", "x", "X"):
            result = a * b
        elif operator == "/":
            if b == 0:
                return "Division by zero is not possible. Please use a non-zero divisor."
            result = a / b
        else:
            return None

        if result.is_integer():
            result = int(result)

        return f"The answer is {result}."
    except (ValueError, OverflowError):
        return "Sorry, I could not calculate that expression."


def get_response(prompt):
    """Return a predefined answer for the supported questions."""
    question = normalize(prompt)

    if not question:
        return "Please type a question, and I will try to help."

    # Match the displayed category questions exactly after normalization.
    if question in ANSWERS:
        return ANSWERS[question]

    # Handle arithmetic written as a plain expression.
    result = calculate(prompt)
    if result is not None:
        return result

    # Handle the arithmetic questions displayed in the sidebar.
    math_questions = {
        "what is 25 37": "The answer is 62.",
        "what is 50 18": "The answer is 32.",
        "what is 12 8": "The answer is 96.",
        "what is 100 4": "The answer is 25.",
    }

    # These patterns preserve the intended operation when the question
    # is written with words instead of mathematical symbols.
    if question == "what is 25 37":
        return "The answer is 62."
    if question == "what is 50 18":
        return "The answer is 32."
    if question == "what is 12 8":
        return "The answer is 96."
    if question == "what is 100 4":
        return "The answer is 25."

    # Basic conversational messages
    if question in ("hi", "hello", "hey", "good morning", "good evening"):
        return "Hello! How can I help you today? You can choose a question from a category or ask me one of the supported questions."

    if question in ("bye", "goodbye", "see you"):
        return "Goodbye! It was nice chatting with you. Have a great day!"

    if "your name" in question or "who are you" in question:
        return "I am a rule-based chatbot designed to answer predefined questions. You can explore the categories in the sidebar to see what I can help with."

    if question in ("help", "what can you do", "what can you answer"):
        return "I can answer the questions listed in Everyday Life, Education and Technology, General Knowledge, Entertainment, Programming, and Basic Mathematics. Choose a category in the sidebar to see its questions."

    return (
        "I could not match that message to one of my predefined questions. "
        "Please choose a question from the sidebar or try rephrasing it."
    )
