from PyQt5.QtWidgets import QApplication


from random import choice, shuffle
from time import sleep
app = QApplication([])

from m2 import *
from m3 import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
q1 = Question('У якому році винайли плутон?', '1930', '1929', '1932', '1927')
q2 = Question('У якому році плутон перестав бути планетою?', '2006', '2005', '2007', '2004')
q3 = Question('У якому році пала західна римська імперія?', '476', '474', '475', '473')
q4 = Question('У якому році Україна стала незалежною?', '1991', '1989', '1990', '1988')
q5 = Question('Скільки років сьогодні було б Тарасу Шевченку?', '209', '207', '210', '206')
q6 = Question('Коли відбувалось велике переселення народів?', '4-7ст', '4-6ст', '5-7ст','3-6ст')
q7 = Question('Коли хрестили київську Русь?', '988', '989', '987', '990')
q8 = Question('Коли помер Володимер Великий?', '1015', '1013', '1014', '1012')
q9 = Question('Коли князь Святослав став правителем?', '945', '943', '944', '942')
q10 = Question('Коли князь Ігор став правителем?', '912', '910', '911','909')


window.show()
app.exec_()
