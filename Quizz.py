class Question:
    def __init__(self, prompt,answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are oranges?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"
    
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    
    
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
            
    print("You got: ", str(score), "Correct")
    
run_test(questions)