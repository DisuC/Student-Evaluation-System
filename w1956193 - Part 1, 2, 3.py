#Author : Disadi Chanmini Gawasinghe Arachchi
#Author ID : 20221545
#Date : 2022/11/14
#SD1 : Coursework

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221545
# UoW ID : w1956193
 
# Date: 2022/12/14


#Part1
#A&B&C&D


progress = 0
progressmoduletrailer= 0
exclude = 0
DonotProgressmoduleretriever = 0
close= True
data_list1 = []
data_list2 = []
data_list3 = []
data_list4 = []

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
    Pass = int_input("Please enter your credits at pass : " ,"Integer required" , "Out of range")
    Defer = int_input("Please enter your credits at defer : ","Integer required" , "Out of range")
    Fail = int_input("Please enter your credits at fail : ","Integer required" , "Out of range")

    

    total = Pass + Defer + Fail
    if total == 120 :#check the total
        if Pass == 120 :
            print ("Progress")
            progress += 1
            progress_data=f"Progress , {Pass} , {Defer} , {Fail}"
            data_list1.append(progress_data)#add values at the end of the list
              
        elif Pass == 100 :
            print ("Progress (module trailer)")
            progressmoduletrailer += 1
            trailer_data=f"Progress (module trailer) , {Pass} , {Defer} , {Fail}"
            data_list2.append(trailer_data)#add values at the end of the list
            
        elif Fail == 120 or Fail == 100 or Fail == 80 :
            print ("Exclude")
            exclude += 1
            exclude_data=f"Exclude , {Pass} , {Defer} , {Fail}"
            data_list3.append(exclude_data)#add values at the end of the list
            
        else :
            print ("Do not Progress – module retriever")
            DonotProgressmoduleretriever += 1
            retriever_data=f"Do not Progress – module retriever , {Pass} , {Defer} , {Fail}"
            data_list4.append(retriever_data)#add values at the end of the list
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
           print("Trailer",progressmoduletrailer,":",progressmoduletrailer*"*")
           print('Retriever',DonotProgressmoduleretriever,":",DonotProgressmoduleretriever*"*")
           print("Excluded",exclude,":",exclude*"*")
           output = progress + progressmoduletrailer + DonotProgressmoduleretriever + exclude #addition of the total outcome
           print("\n",output ,"outcomes in total.")
           print("\n--------------------------------------------------------------------")
           close=False
           break



#Part2
print('\nPart 2')
for pro_data in data_list1:
    print(pro_data)

for trai_data in data_list2:
    print(trai_data)

for ex_data in data_list3:
    print(ex_data)

for ret_data in data_list4:
    print(ret_data)



print("\n--------------------------------------------------------------------")
#Part3
print('\nPart 3')


file = open("text.txt", "w") #write to the file - overwriting
for pro_data in data_list1:
    text_pro=str(pro_data)+("\n")
    file.write(text_pro)

for trai_data in data_list2:
    text_trai=str(trai_data)+("\n")
    file.write(text_trai)
    
for ex_data in data_list3:
    text_ex=str(trai_data)+("\n")
    file.write(pro_data)

for ret_data in data_list4:
    text_ret=str(trai_data)+("\n")
    file.write(pro_data)
file.close()

file = open("text.txt", "r") #read the file 
print(file.read())
file.close()


print("\n--------------------------------------------------------------------")










         


        
    


    
