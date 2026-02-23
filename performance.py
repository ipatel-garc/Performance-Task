#performance task code

score=[]
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
question=input("Would you like to take a vocab quiz? Yes or No?: ")
def vocabquiz(vocab, definition):
        while question =="Yes":
            print("Here are the vocab terms, study if needed: ", list(Vocabulary.keys()) )
            question1 = input(f"What word means {definition}?:")
            if question1 == vocab:
                print("Correct")
                score.append("correct")
                return(score)
            else:
                print("Incorrect")
                score.append("incorrect")
                return(score)
    
    


vocabquiz("Sonder", "the profound, individual realization that everyone has a life as vivid and complex as your own.")
vocabquiz("Fractious", "Inclined to make trouble; unruly")
vocabquiz("Ebullient","full of energy; cheerful")
vocabquiz("Hubris","overbearing pride or self-confidence")
vocabquiz("Kinetic","relating or resulting from motion")
vocabquiz("Callous","disregard for others")
vocabquiz("Eschew","To deliberately avoid using")
vocabquiz("Specious","superficially plausible. but actually wrong; misleading in appearance")
vocabquiz("Abstruse","difficult to understand")
vocabquiz("Disparate","of a distinct kind")
