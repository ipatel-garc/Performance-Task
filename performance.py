#performance task code
import random
report=[]
score=[]
wrong_answers=[]
vocabulary = {
              "Eschew": ["To deliberately avoid using"],
              "Sonder": ["the profound, individual realization that everyone has a life as vivid and complex as your own"], 
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
print(f"Hi {name} here are the vocab terms, study if needed: ",list(vocabulary.keys())) 
question=input("Would you like to take a vocab quiz on these words? Yes or No?: ")
 
def vocabquiz(word, definition):
        while question =="Yes":        
            question1 = input(f"What word means {definition}?:") 
            if question1 == word:
                print("Correct")
                score.append("correct")
                return(score)
            else:
                print("Incorrect")
                wrong_answers.append(word)
                return(wrong_answers)
            
def randomizing():
     items = list(vocabulary.items())
     random.shuffle(items)
     for word, definition in items:
          vocabquiz(word, definition[0])


    
def scores():
    results=input("Would you like to see your report? Yes or No:")
    if results== "Yes": 
        final_grade = len(score) * 10
        report.append(f"Name: {name}")
        report.append(f"Score: {final_grade}%")
        report.append(f"Study these terms: {wrong_answers}")
        print("\n--- Report ---")
        for item in report:
             print(item)
    elif results=="No":
        print("Thank you for taking the test!")


randomizing()
scores()

