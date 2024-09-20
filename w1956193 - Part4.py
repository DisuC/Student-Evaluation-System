#Author : Disadi Chanmini Gawasinghe Arachchi
#Author ID : 20221545
#Date : 2022/11/14
#SD1 : Coursework

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221545
# UoW ID : w1956193

# Date: 2022/12/14


#Part4
print('\nPart 4')



progress = 0
progressmoduletrailer= 0
exclude = 0
DonotProgressmoduleretriever = 0
progression_data = {}#creating an empty dictionary
close= True

def int_input(message, error_message,range_error_message):#defining a function
    while True:
        try:
            marks = int(input(message))
            while not int(marks) in range (0, 121, 20) :
                    print (range_error_message)#function call
                    marks = int(input(message))
                    
        except ValueError:
            print(error_message)#function call
            continue
        break
    return marks

while close:
    student_id = str(input("Enter student ID : "))
    Pass = int_input("Please enter your credits at pass : " ,"Integer required" , "Out of range")
    Defer = int_input("Please enter your credits at defer : ","Integer required" , "Out of range")
    Fail = int_input("Please enter your credits at fail : ","Integer required" , "Out of range")
    
    

    total = Pass + Defer + Fail
    if total == 120 :#check the total
        if Pass == 120 :
            print ("Progress")
            progress += 1
            progress_data=f"Progress , {Pass} , {Defer} , {Fail}"
            progression_data[student_id]=progress_data
            
            
              
        elif Pass == 100 :
            print ("Progress (module trailer)")
            progressmoduletrailer += 1
            trailer_data=f"Progress , {Pass} , {Defer} , {Fail}"
            progression_data[student_id]=trailer_data

            
        elif Fail == 120 or Fail == 100 or Fail == 80 :
            print ("Exclude")
            exclude =+ 1
            exclude_data=f"Progress , {Pass} , {Defer} , {Fail}"
            progression_data[student_id]=exclude_data
        else :
            print ("Do not Progress – module retriever")
            DonotProgressmoduleretriever += 1
            retriever_data=f"Progress , {Pass} , {Defer} , {Fail}"
            progression_data[student_id]=retriever_data
    else :
        print ("Total incorrect")

    while True:
        select=str(input(" \n Would you like to enter another data set? \nEnter'y'for yes or 'q' for quit : "))#asking to continue or quit the programe
        if select.lower () =='y':#lowercase-convert capital letters to simple letters
            print('\n')
            break
        elif select.lower () =="q":#lowercase-convert capital letters to simple letters
           print('------------------------------------------------------------\nHISTOGRAM')
           print("Progress", progress,":", progress *"*")
           print("progress(module trailer)",progressmoduletrailer,":",progressmoduletrailer*"*")
           print('Do not Progress – module retriever',DonotProgressmoduleretriever,":",DonotProgressmoduleretriever*"*")
           print("Excluded",exclude,":",exclude*"*")
           output = progress + progressmoduletrailer + DonotProgressmoduleretriever + exclude #addition of the total outcome
           print("\n",output ,"outcomes in total.")
           print("\n--------------------------------------------------------------------")
           for key,value in progression_data.items():
               print(key ," : ",value,end=" ")
           close=False
           break
        





         


        
    


    
