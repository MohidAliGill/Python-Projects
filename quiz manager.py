from random import random

class Question:
    def __init__(self):
        self.question = ""
        self.answer = ""

    def Input(self):
        self.question = input("Enter your question:  ")
        self.answer = input("Enter answer:  ")

    def CheckAnswer(self, answer):
        if self.answer == answer:
            return True
        else:
            return False
        
    def PresentQuestion(self):
        print("Q) " + self.question)
        
        
class MathQuestion(Question):
    def __init__(self):
        Question.__init__(self)
        
class TextQuestion(Question):
    def __init__(self):
        Question.__init__(self)
                    
class BooleanQuestion(Question):
    def __init__(self):
        Question.__init__(self)

    def PresentQuestion(self):
        print("Q) " + self.question + "  [True / False]")
        

class ChoiceQuestion(Question):
    def __init__(self):
        Question.__init__(self)
        self.choices = {}
        
    def Input(self):
        Question.Input(self);
        a = input("Enter choice A: ")
        b = input("Enter choice B: ")
        c = input("Enter choice C: ")
        d = input("Enter choice D: ")
        self.choices = {"A":a, "B":b, "C":c, "D":d}
        
    def PresentQuestion(self):
        Question.PresentQuestion(self)
        print("  A.  " + self.choices["A"])
        print("  B.  " + self.choices["B"])
        print("  C.  " + self.choices["C"])
        print("  D.  " + self.choices["D"])        


class QuestionBank:
    def __init__(self):
        self.bank = []

    def AddQuestion(self, question):
        self.bank.append(question)

    def GetRandomQuestion(self):
        n = int(random() * len(self.bank))
        return self.bank[n]


class Quiz:
    MAX_QUESTIONS = 5
    def __init__(self, qbank):
        self.bank = qbank
        self.correctAnswers = 0
        self.wrongAnswers = 0

    def PrintReportCard(self):
        c = self.correctAnswers
        w = self.wrongAnswers
        print("Congratulations, you've finished the quiz")
        print("Correct: " + str(c))
        print("Wrong  : " + str(w))
        print("Score percentage: " + str(c/(c+w)*100) + "%")        

    def Run(self):
        for i in range(Quiz.MAX_QUESTIONS):
            q = self.bank.GetRandomQuestion()
            q.PresentQuestion()
            answer = input("Your answer:  ")
            if q.CheckAnswer(answer) == True:
                self.correctAnswers += 1
            else:
                self.wrongAnswers += 1


class QuizManager:
    def __init__(self):
        self.questionbank = QuestionBank()
        self.quiz = Quiz(self.questionbank)

    def PrintMainMenu(self):
        print("Choose option:")
        print("1. Create a Quiz")
        print("2. Run Quiz")

    def PrintCreationMenu(self):
        print("Quiz creation mode. Select the type of question you want to create:")
        print("1.  Math Question")
        print("2.  Text Question")
        print("3.  Boolean Question")
        print("4.  Choice Question")
        print("5.  Go back to Main Menu")


    def Run(self):
        finished = False
        
        while not finished:
        
            self.PrintMainMenu()
            choice = input()
        
            if choice == "1":
                creationModeDone = False
                while not creationModeDone:
                    self.PrintCreationMenu()
                    choice = input()
                    if choice == "1":
                        q = MathQuestion()
                        q.Input()
                        self.questionbank.AddQuestion(q)
                    elif choice == "2":
                        q = TextQuestion()
                        q.Input()
                        self.questionbank.AddQuestion(q)
                    elif choice == "3":
                        q = BooleanQuestion()
                        q.Input()
                        self.questionbank.AddQuestion(q)
                    elif choice == "4":
                        q = ChoiceQuestion()
                        q.Input()
                        self.questionbank.AddQuestion(q)
                    elif choice == "5":
                        creationModeDone = True
                
            elif choice == "2":
                self.quiz.Run()
                self.quiz.PrintReportCard()
                
                finished = True
        
        
manager = QuizManager()
manager.Run()        
        
        
        
        
        
##########################        
#    TESTING
##########################

##########################################
# mq = MathQuestion()
# mq.Input()
# mq.PresentQuestion()
# print("2 + 2 == 4", mq.CheckAnswer("4"))
# print("2 + 2 == 2", mq.CheckAnswer("2"))
# print("2 + 2 == 5", mq.CheckAnswer("5"))
##########################################

##########################################
# tq = TextQuestion()
# tq.Input()
# tq.PresentQuestion()
# print("My name is == fakhir", tq.CheckAnswer("fakhir"))
# print("My name is == ali", tq.CheckAnswer("ali"))
# print("My name is == khan", tq.CheckAnswer("khan"))
##########################################

##########################################
# bq = BooleanQuestion()
# bq.Input()
# bq.PresentQuestion()
# print("Are you a Student? == T", bq.CheckAnswer("T"))
# print("Are you a Student? == F", bq.CheckAnswer("F"))
##########################################

##########################################
# q = ChoiceQuestion()
# q.Input()
# q.PresentQuestion()
# print("What's the capital of Pakistan? == Lahore", q.CheckAnswer("Lahore"))
# print("What's the capital of Pakistan? == Karachi", q.CheckAnswer("Karachi"))
# print("What's the capital of Pakistan? == Islamabad", q.CheckAnswer("Islamabad"))
# print("What's the capital of Pakistan? == Peshawar", q.CheckAnswer("Peshawar"))
##########################################

##########################################
# quizbank = QuestionBank();
# quizbank.AddQuestion(mq);
# quizbank.AddQuestion(tq);
# quizbank.AddQuestion(bq);
# print(len(quizbank.bank))

# q = quizbank.GetRandomQuestion()
# q.PresentQuestion()
##########################################

        
        

