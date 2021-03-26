import time
from itertools import count
from multiprocessing import Process
#Game_level=input("Enter Game level. Easy\t,Medium\t,Hard")
#if Game_level==Easy:
#    open Question.
#elif Game_level==Medium:
#    open Question2
#elif Game_level==Hard:
#    open Question3
def inc_forever():
    print('Times Started')
    while True:
        time.sleep(1)

def return_zero():
    print('Game will start in 2 sec')
    return 0
if __name__ == '__main__':
    # counter is an infinite iterator
    counter = count(0)
    p1 = Process(target=inc_forever, name='Process_inc_forever')
    p2 = Process(target=return_zero, name='Process_return_zero')
    p1.start()
    p2.start()
    p1.join(timeout=2)
    p2.join(timeout=2)
    p1.terminate()
    p2.terminate()
    class Question:
         def __init__(self, prompt, answer):
              self.prompt = prompt
              self.answer = answer
    
    question_prompts = [
         "What color are apples?\n(a) Red/Green\n(b)Orange\n(c)white\n(d)Pink\n",
         "What color are bananas?\n(a) Red/Green\n(b)Yellow\n(c)orange\n(d)Blue\n",
         "What color are sky?\n(a) black\n(b)blue\n(c)Orange\n(d)Pink\n",
         "What color are Water?\n(a) Grey\n(b)color_less\n(c)Yellow\n(D)red\n",
         "what is the color of cucumber?\n(a)Green\n(b)white\n(c)(Red)\n(d)Yellow\n"
    
    ]
    
    questions = [
         Question(question_prompts[0], "a"),
         Question(question_prompts[1], "b"),
         Question(question_prompts[2], "b"),
         Question(question_prompts[3], "b"),
         Question(question_prompts[4], "a"),
    
    ]
    
    def run_quiz(questions):
         score = 0
         for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
         print("you got", score, "out of", len(questions))
         if score==1:
             print("Your status of score is Poor")
         elif score==2:
             print(" your status of score is Bad")
         elif score==3:
             print("your status of score is good")
         elif score==4:
             print("youe status of score is Strong")
         elif score==5:
             print("wow ! very strong")
    run_quiz(questions)
if p2.exitcode == 0:
    print(f'{p2} \noops! Timeout')
#i tried to best what i know. but i think i learn if i got a propper guidence.