import random 

CategoriesList = [
    "General", 
    "Math", 
    "Science", 
    "History", 
    "Geography",
    "Sports", 
    "Entertainment", 
    "Art", 
    "Celebrities", 
    "Animals", 
    "Vehicles",
    "Comics", 
    "Gadgets", 
    "Japanese Anime", 
    "Cartoon and Animations"
]

QuestionList = [
    { 
        "category": "General",
        "question": "What is the capital of India?",
        "answers": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "correct_answer": "New Delhi"
    },
    {
        "category": "Math",
        "question": "What is the square root of 100?",
        "answers": ["10", "20", "30", "40"],
        "correct_answer": "10"
    },
    {
        "category": "Science",
        "question": "What is the chemical formula of water?",
        "answers": ["H2O", "H2O2", "H2O3", "H2O4"],
        "correct_answer": "H2O"
    },
    {
        "category": "History",
        "question": "Who was the first president of the United States?",
        "answers": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"],
        "correct_answer": "George Washington"
    },
    {
        "category": "Geography",
        "question": "What is the capital of France?",
        "answers": ["Paris", "Lyon", "Marseille", "Toulouse"],
        "correct_answer": "Paris"
    },
    {
        "category": "Sports",
        "question": "What is the name of the trophy awarded to the winner of the English Premier League?",
        "answers": ["The Premier League Trophy", "The FA Cup", "The Community Shield", "The EFL Cup"],
        "correct_answer": "The Premier League Trophy"
    },
    {
        "category": "Entertainment",
        "question": "What is the name of the main character in the video game series 'The Legend of Zelda'?",
        "answers": ["Link", "Zelda", "Ganondorf", "Sheik"],
        "correct_answer": "Link"
    },
    {
        "category": "Art",
        "question": "What is the name of the artist who painted the Mona Lisa?",
        "answers": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "category": "Celebrities",
        "question": "What is the name of the actor who plays the character 'Tony Stark' in the Marvel Cinematic Universe?",
        "answers": ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Mark Ruffalo"],
        "correct_answer": "Robert Downey Jr."
    },
    {
        "category": "Animals",
        "question": "What is the name of the largest land animal in the world?",
        "answers": ["Elephant", "Giraffe", "Hippopotamus", "Blue Whale"],
        "correct_answer": "Blue Whale"
    },
    {
        "category": "Vehicles",
        "question": "What is the name of the car company that makes the 'Model S'?",
        "answers": ["Tesla", "Ford", "Toyota", "Honda"],
        "correct_answer": "Tesla"
    },
    {
        "category": "Comics",
        "question": "What is the name of the superhero who is a member of the Justice League?",
        "answers": ["Batman", "SuperMan", "Wonderwoman", "Flash"],
        "correct_answer": "SuperMan"
    },
    {
        "category": "Gadgets",
        "question": "What is the name of the company that makes the 'iPhone'?",
        "answers": ["Apple", "Samsung", "Google", "Microsoft"],
        "correct_answer": "Apple"
    },
    {
        "category": "Japanese Anime",
        "question": "What is the name of the main character in the anime series 'Naruto'?",
        "answers": ["Naruto", "Sasuke", "Sakura", "Kakashi"],
        "correct_answer": "Naruto"
    },
    {
        "category": "Cartoon and Animations",
        "question": "What is the name of the main character in the cartoon series 'SpongeBob SquarePants'?",
        "answers": ["SpongeBob SquarePants", "Patrick Star", "Squidward Tentacles", "Mr. Krabs"],
        "correct_answer": "SpongeBob SquarePants"
    }
]

class Questions: 
    def __init__(self, category, question, answers, correct_answer):
        self.category = category
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def get_category(self):
        random.shuffle(CategoriesList)
        return CategoriesList[:3]
    
    def get_question(self, category):
        for question in QuestionList:
            if question["category"] == category:
                return question["question"]

    def get_answers(self, category):
        for question in QuestionList:
            if question["category"] == category:
                return question["answers"]
    
    def get_correct_answer(self, category):
        # get the correct_answer 
        for question in QuestionList:
            if question["category"] == category:
                return question["correct_answer"]



