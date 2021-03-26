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
    print('clock is Started')
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
         "who is the president of india?\n(a)pranab Mukherjee\n(b)Narendra Modi\n(c)Ran Nath Kovind\n(d)Amit Shah\n",
         "National Flower of India?\n(a) Rose\n(b)lilly\n(c)palas\n(d)lotus\n",
         "Who owns Fifa 2018?\n(a) Russia\n(b)france\n(c)Germny\n(d)South Africa\n",
         "Ranking of India in medical care?\n(a) One\n(b)two\n(c)Three\n(D)Eight\n",
         "Ranking of India in hunger Index?\n(a)94\n(b)117\n(c)87\n(d)24\n"
    
    ]
    
    questions = [
         Question(question_prompts[0], "c"),
         Question(question_prompts[1], "d"),
         Question(question_prompts[2], "b"),
         Question(question_prompts[3], "a"),
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
    print(f'{p2} \nAnd! Timeout')
#i tried to best what i know. but i think i learn if i got a propper guidence.