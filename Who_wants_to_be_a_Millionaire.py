print("Welcome to the Quiz Game!")
print("This is a show for Being Millionaire by giving answer of the QUIZ.")

Questions=[["What is the language used for FB?","Python","Java","JS","c++",3],
           ["What is the national fruit of BD?","Jackfruit","Mango","Berry","Lichi",1],
           ["What is the language used for BD?","Bangla","English","Hindi","Urdu",1],
           ["What is the most used country for FB?","England","USA","India","Pakistan",3],
           ["What is the color of Sky?","Green","Blue","Black","Red",2],
           ["What is the capital of France?", "Berlin", "London", "Paris", "Madrid", 3],
           ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
           ["Who wrote the play 'Hamlet'?", "Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Mark Twain", 2],
           ["What is the boiling point of water at sea level?", "90°C", "100°C", "110°C", "120°C", 2],
           ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Helium", 3],
           ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Quartz", 3],
           ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Silver", "Osmium", 2],
           ["Who painted the Mona Lisa?", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet", 1],
           ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
           ["Which continent is known as the 'Dark Continent'?", "Asia", "Africa", "Australia", "Europe", 2]
] 


levels=[1000,2000,5000,10000,25000,50000,100000,150000,250000,500000,1000000,1500000,2500000,5000000,10000000]
milestones = {4: 25000, 9: 500000, 14: 1000000}
money=0
option = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


for i in range(0,len(Questions)):
    Question=Questions[i]
    print(f"\nQuestion for BDT.{levels[i]}")
    print(f"\n{Question[0]}")
    print(f"a. {Question[1]}     b. {Question[2]}      c. {Question[3]}     d. {Question[4]}") 
    
    try:
        reply=input("\nEnter the Answer[a/b/c/d]:").lower()
        selected_option = option[reply]

        if(selected_option==Question[5]):
            print(f"\nCorrect,You have won {levels[i]}")
            money=levels[i]
        else:
            print("\nWrong Answer!")
            money = 0
            for key in sorted(milestones.keys(), reverse=True):
                if i >= key:
                    money = milestones[key]
                    break
            break
 

    except ValueError:
        print("Invalid Input.")
        break

print(f"\nGame Over! You are taking home BDT {money}.")
