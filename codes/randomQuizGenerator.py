#! python3

'''randomQuizGenerator.py - Creates quizzes with questions and answers in
random order, along with the answer key.'''

import random, os, pprint

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
            'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan':'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
path = 'H:\\python\\files\\Quiz'
os.chdir(path)

for quizNum in range(35):

    quizFile = open(os.path.join(path,'capitalquiz_%s.txt' %(quizNum+1)),'w')
    answerKeyFile = open(os.path.join(path,'capitalquiz_Answers_%s.txt' %(quizNum+1)),'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' '*20 + 'State Capitals Quiz (Form %s)' %(quizNum+1) + '\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question in range(50):

        quizFile.write('%s. What is the Capital of %s?\n' %( question+1, states[question]))

        correctAnswer = capitals[states[question]]
        allAnswers = list(capitals.values())
        del allAnswers[allAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(allAnswers,3)
        allOptions = wrongAnswers + [correctAnswer]
        random.shuffle(allOptions)

        for i in range(4):
            quizFile.write('    (%s) %s\n' %('abcd'[i], allOptions[i]))

        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' %(question+1, 'abcd'[allOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()
    
    
                                 
