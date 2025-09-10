import random

questions = {
    "What is the capital of France?": {
        "options": ["A. Paris","B. London","C. Berlin","D. Madrid"],
        "answer": "A"
    },

    "Which programming language is this game written in?": {
        "options": ["A. Java","B. Python","C. C++","D. Ruby"],
        "answer": "B"
    },

    "Which module is used to generate random numbers?": {
        "options": ["A. sys", "B. random", "C. math", "D. os"],
        "answer": "B"
    },

    "Which data type is used to store key-value pairs?": {
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    }
}

def get_random_question():
    question = random.choice(list(questions.keys()))
    return question,questions[question]["options"],questions[question]["answer"]
