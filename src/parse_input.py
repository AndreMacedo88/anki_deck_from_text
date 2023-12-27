
def question_answer_split(line):
    line = line.lstrip("- ")
    answer, question = line.split(" = ")
    return question, answer

def to_dict(input):
    cards_details = dict()
    with open(input) as FileObj:
        for line in FileObj:
           question, answer = question_answer_split(line) 
           cards_details[question] = answer
    return cards_details