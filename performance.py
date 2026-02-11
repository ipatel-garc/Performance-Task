#performance task code

score=[]
Vocabulary= {
    "Eschew": ["Deliberately avoid using"],
    "Sonder": ["The profound, individual realization that everyone has a life as vivid and complex as your own."],
    "Hubris": ["Overbearing pride or self-confidence"],
    "Abstruse": ["Difficult to understand"],
    "Callous": ["Disregard for others"],
    "Ebullient": ["Full of energy, cheerful"],
    "Disparate": ["Of a distinct kind"],
    "Fractious": ["Inclined to make trouble; unruly"],
    "Kinetic": ["Relating or resulting from motion"],
    "Specious": ["Superficially plausible. but actually wrong; misleading in appearance"]
}

def vocab_quiz():
    question=input("Would you like to take a vocab quiz? Yes or No?: ")
    while question =="Yes":
        print("Here are the vocab terms, study if needed: ", list(Vocabulary.keys()) )
        question1 = print(input("Deliberately avoid u: sing"))
        if question1 == "Eschew":
            print("Correct")
            score.append(1)
            print(score)
        else:
            print("Incorrect")
    
    


vocab_quiz()