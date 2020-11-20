import pandas as pd
from joblib import load

ext_model = load('extmodel.joblib')
est_model = load('estmodel.joblib')
agr_model = load('agrmodel.joblib')
csn_model = load('csnmodel.joblib')
opn_model = load('opnmodel.joblib')

ext_questions = {'EXT1' : "I am the life of the party.",              
                 'EXT2' : "I don't talk a lot.",
                 'EXT3' : "I feel comfortable around people.",
                 'EXT4' : "I keep in the background.",
                 'EXT5' : "I start conversations.",
                 'EXT6' : "I have little to say.",
                 'EXT7' : "I talk to a lot of different people at parties.",
                 'EXT8' : "I don't like to draw attention to myself.",
                 'EXT9' : "I don't mind being the center of attention.",
                 'EXT10' : "I am quiet around strangers."}

ext_ans = ['Introverted',
           'Somewhere in bewteen Introverted and Extraverted',
           'Extraverted']

est_questions = {'EST1'	: "I get stressed out easily.",
                 'EST2' : "I am relaxed most of the time.",
                 'EST3' : "I worry about things.",
                 'EST4' : "I seldom feel blue.",
                 'EST5' : "I am easily disturbed.",
                 'EST6' : "I get upset easily.",
                 'EST7' : "I change my mood a lot.",
                 'EST8' : "I have frequent mood swings.",
                 'EST9' : "I get irritated easily.",
                 'EST10' : "I often feel blue."}

est_ans = ['Calm/Tranquil',
           'Somewhere in bewteen Calm/Tranquil and Neurotic',
           'Neurotic']

agr_questions = {'AGR1' : "I feel little concern for others.",
                 'AGR2' : "I am interested in people.",
                 'AGR3' : "I insult people.",
                 'AGR4' : "I sympathize with others' feelings.",
                 'AGR5' : "I am not interested in other people's problems.",
                 'AGR6' : "I have a soft heart.",
                 'AGR7' : "I am not really interested in others.",
                 'AGR8' : "I take time out for others.",
                 'AGR9' : "I feel others' emotions.",
                 'AGR10' : "I make people feel at ease."}

agr_ans = ['Disagreeable',
           'Somewhere in bewteen Disagreeable and Agreeable',
           'Agreeable']

csn_questions = {'CSN1' : "I am always prepared.",
                 'CSN2' : "I leave my belongings around.",
                 'CSN3' : "I pay attention to details.",
                 'CSN4' : "I make a mess of things.",
                 'CSN5' : "I get chores done right away.",
                 'CSN6' : "I often forget to put things back in their proper place.",
                 'CSN7' : "I like order.",
                 'CSN8' : "I shirk my duties.",
                 'CSN9' : "I follow a schedule.",
                 'CSN10' : "I am exacting in my work."}

csn_ans = ['Casual',
           'Somewhere in bewteen Casual and Conscientious',
           'Conscientious']

opn_questions = {'OPN1' : "I have a rich vocabulary.",
                 'OPN2' : "I have difficulty understanding abstract ideas.",
                 'OPN3' : "I have a vivid imagination.",
                 'OPN4' : "I am not interested in abstract ideas.",
                 'OPN5' : "I have excellent ideas.",
                 'OPN6' : "I do not have a good imagination.",
                 'OPN7' : "I am quick to understand things.",
                 'OPN8' : "I use difficult words.",
                 'OPN9' : "I spend time reflecting on things.",
                 'OPN10' : "I am full of ideas."}

opn_ans = ['Closed Minded',
           'Somewhere in bewteen Closed Minded and Open Minded',
           'Open Minded']

questions_dict = {'EXT' : ext_questions,
                  'EST' : est_questions,
                  'AGR' : agr_questions,
                  'CSN' : csn_questions,
                  'OPN' : opn_questions}

ans_dict = {'EXT' : ext_ans,
            'EST' : est_ans,
            'AGR' : agr_ans,
            'CSN' : csn_ans,
            'OPN' : opn_ans}

model_dict = {'EXT' : ext_model,
              'EST' : est_model,
              'AGR' : agr_model,
              'CSN' : csn_model,
              'OPN' : opn_model}

def get_trait():
    print('Which trait would you like to predict?')
    print('For extraversion type: EXT')
    print('For neuroticism type: EST')
    print('For agreeableness type: AGR')
    print('For conscientiousness type: CSN')
    print('For openness type: OPN')

    question = input('Your answer here: ')

    while not(question.upper() in questions_dict):
        print()
        print('Please give a valid input')
        question = input('Your answer here: ')

    return question.upper()

def ask_questions(trait):
    X = pd.DataFrame({})
    values = ['1', '2', '3', '4', '5']
    print()
    print('For the following questions, please enter a whole number between ')
    print('1 and 5, 1 being Strongly Disagree and 5 being Strongly Agree')
    for i in questions_dict:
        if not(i == trait.upper()):
            for j in questions_dict[i]:
                
                question = input(questions_dict[i][j] + ' ')
                while not(question in values):
                    print()
                    print('Please enter a whole number between 1 and 5')
                    question = input(questions_dict[i][j] + ' ')
                    
                X[j] = [int(question)]

    return X

def predict_trait(trait, df):
    model = model_dict[trait]
    answer = model.predict(df)
    return answer

trait = get_trait()
X = ask_questions(trait)
prediction = predict_trait(trait, X)
answer = ans_dict[trait][prediction[0]]
print('We predict you are', answer)
