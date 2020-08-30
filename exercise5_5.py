print(">> Programe Change Number to text <<")
number = input("Enter interger number : ")
print("Number : ",number)
Lnum = len(number)
textb = ['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ']
i = 0
text = " "
while i < Lnum :
        
    if number[i]== "0" :
        text += textb[0]
    elif number[i]== "1" :
        text += textb[1]
    elif number[i]== "2" :
        text += textb[2]
    elif number[i]== "3" :
        text += textb[3]
    elif number[i]== "4" :
        text += textb[4]
    elif number[i]== "5" :
        text += textb[5]
    elif number[i]== "6" :
        text += textb[6]
    elif number[i]== "7" :
        text += textb[7]
    elif number[i]== "8" :
        text += textb[8]
    elif number[i]== "9" :
        text += textb[9]
        
    i+=1
        
print("Text :",text)
print("Exit Program")
