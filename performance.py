#performance task code
import random #imported to use later in the code for randomizing
report=[]
score=[]

wrong_answers=[]
#lists created for later use in the program. score list created to have the ability to generate a score, wrong_answers list created to store the wrong answers which will show in the report

vocabulary = {
              "Eschew": ["constantly avoid using"],
              "Sonder": ["the realization a person has that their life is as complicated as theirs"], 
              "Hubris": ["to have an ego; self-confident"],
              "Abstruse": ["hard to understand"],
              "Callous": ["to not think about other people"], 
              "Ebullient": ["full of energy"], 
              "Disparate": ["of a different type"], 
              "Fractious": ["having a tendency to make trouble"], 
              "Kinetic": ["relates to motion"], 
              "Specious": ["an argument that looks right but is meant to mislead"]
}
#dictionary of words and definitions used in the program. Words found using a mix of Google and prior already known words, definitions paraphrased through understanding of definitions from google

name=input("What is your name?:")
print(f"Hi {name} here are the vocab terms, study if needed: ",list(vocabulary.keys())) #used to print all the vocab words in the dictionary
question=input("Would you like to take a vocab quiz on these words? Yes or No?: ")

def vocabquiz(word, definition): #first function used for the program. This is where the user will answer questions. The function stores the amount that are correct and the ones that the user had gotten wrong. 
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
            
def randomizing(): #this function is used to randomize the definitions given for each question. the random.shuffle rearranges the items so they are not in a certain order. This function also calls the other function within it 
     items = list(vocabulary.items())
     random.shuffle(items)
     for word, definition in items:
          vocabquiz(word, definition[0])

randomizing() #calls the function above and is what causes the questions to be asked due to it calling the other function
    
def scores(): # function that allows the person to see their score. 
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



scores()

