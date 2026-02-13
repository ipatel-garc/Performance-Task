#performance task code

score=[]
Vocabulary = {"Eschew", "Sonder", "Hubris", "Abstruse", "Callous", "Ebullient", "Disparate", "Fractious", "Kinetic", "Specious"}
Definition = ["To deliberately avoid using", "the profound, individual realization that everyone has a life as vivid and complex as your own.", "overbearing pride or self-confidence", "difficult to understand", "disregard for others", "full of energy, cheerful", "of a distinct kind", "Inclined to make trouble; unruly", "relating or resulting from motion", "superficially plausible. but actually wrong; misleading in appearance"]



for define, vocab in zip(Vocabulary, Definition):
    question=input("Would you like to take a vocab quiz? Yes or No?: ")
    while question =="Yes":
            # print("Here are the vocab terms, study if needed: ", list(Vocabulary.keys()) )
        question1 = input(f"What word means {Definition}:")
        if question1 == word:
            print("Correct")
            score.append(1)
            print(score)
        else:
            print("Incorrect")
    
    


vocab_quiz("Eschew", "To deliberately avoid using")
