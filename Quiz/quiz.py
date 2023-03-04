# write a program that loops through the questions and adds 1 to the score of the player answers correctly
# add 0 if they answer incorrectly
# print the score with a message of your choice at the end
# you may also print a different message based on how well the user did

QUESTIONS_AND_ANSWERS = dict(questions=["Who founded python? ",
                                        "What is the shortened version of 'boolean' in python? ",
                                        "What is 23+71? ",
                                        "When was Python created? ",
                                        "To assign a variable, do we use = or ==? "
                                        ],
                             answers=["Guido van Rossum",
                                      "bool",
                                      "94",
                                      "1991",
                                      "="])


def get_input(text):
    return input(text)


def play_game(input_data):
    score = 0
    for question in input_data['questions']:
        response = get_input(question)
        if response == input_data['answers'][input_data['questions'].index(question)]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    return score


