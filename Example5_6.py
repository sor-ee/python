Done = True
Count = 0
while Done:
    Score = input(f"Enter score value  #{Count+1} : ")
    if Score != "-1":
        Mark = float(Score)
        if Mark >=0 and Mark <= 100 :
            Grade = ""
            if Mark >= 80:
                Grade = "A"
            elif Mark >= 70:
                Grade = "B"
            elif Mark >= 60:
                Grade = "C"
            elif Mark >= 50:
                Grade = "D"
            else:
                Grade = "F"
                Count+=1
            print(f"Score is {Mark} , get {Grade}")
        else:
            print("Score out of range , input again.")
    elif Score == "-1":
        Done = False
        
print("Exit program")
    
