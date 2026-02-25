#performance task code
import random
score=[]
wrong_answers=[]
Vocabulary = {
              "Eschew": ["To deliberately avoid using"],
              "Sonder": ["the profound, individual realization that everyone has a life as vivid and complex as your own."], 
              "Hubris": ["overbearing pride or self-confidence"],
              "Abstruse": ["difficult to understand"],
              "Callous": ["disregard for others"], 
              "Ebullient": ["full of energy, cheerful"], 
              "Disparate": ["of a distinct kind"], 
              "Fractious": ["Inclined to make trouble; unruly"], 
              "Kinetic": ["relating or resulting from motion"], 
              "Specious": ["superficially plausible. but actually wrong; misleading in appearance"]
}
name=input("What is your name?:")
question=input("Would you like to take a vocab quiz? Yes or No?: ")
def vocabquiz(vocab, definition):
        while question =="Yes":
            print("Here are the vocab terms, study if needed: ",list(Vocabulary.keys()))            
            question1 = input(f"What word means {definition}?:") 
            if question1 == vocab:
                print("Correct")
                score.append("correct")
                return(score)
            else:
                print("Incorrect")
                wrong_answers.append(vocab)
                return(wrong_answers)

    
def scores():
    results=input("Would you like to see your r?Yes or No:")
    if results== "Yes":
        result=len(score) * 10
        print(f"You got a {result}%!")
        print(wrong_answers)
    elif results=="No":
        print("Thank you for taking the test!")

vocabquiz("Sonder", "the profound, individual realization that everyone has a life as vivid and complex as your own.")
vocabquiz("Fractious", "Inclined to make trouble; unruly")
vocabquiz("Ebullient", "full of energy; cheerful")
vocabquiz("Hubris","overbearing pride or self-confidence")
vocabquiz("Kinetic","relating or resulting from motion")
vocabquiz("Callous","disregard for others")
vocabquiz("Eschew","To deliberately avoid using")
vocabquiz("Specious","superficially plausible. but actually wrong; misleading in appearance")
vocabquiz("Abstruse","difficult to understand")
vocabquiz("Disparate","of a distinct kind")
scores()

