from difflib import SequenceMatcher
import difflib
import time
import os
from datetime import date




#objective 1   done
#objective 2   done
#objective 3   done
#objective 4   done
#objective 5   done
#objective 6   done
#objective 7   done
#objective 8   done 
#objective 9   done 
#objective 10  done
#objective 11  done
#objective 12  oops 
#objective 13  done

today = date.today()


Additions = open("EnglishWords.txt" , "a")


lengthwords, addedwords, incorrect, wordsadded, wordschanged, correct = 0, 0, 0, 0, 0, 0

# creating a list of words in the file
with open("EnglishWords.txt", "r") as f:
     words = f.read()
englishwords= words.splitlines()


def file_generator(list):
    correctfile = input ("\n\n Please write the name of the file in which you want to save your outcomes :  ")
    file_create = open (f'{correctfile}.txt', "a")
    for x in range(len(list)):
        file_create.write(list[x]+ " ")
    file_create.write("\n\n\n Total numer of words added : " + str(addedwords))
    file_create.write("\n Number of correct words :" + str(correct))
    file_create.write("\n Number of incorrect words : " + str(incorrect))
    file_create.write("\n Number of words Added : " + str(wordsadded))
    file_create.write("\n Words Chenged : " + str(wordschanged))
    file_create.close()


def stripper(sentence):
    # this function will remove all the puctuation marks and numbers form the sentence
    #it will be accessed by the spellcheck function 
    punctuations = '''!()-[]{};:'"1234567890,<>./?@#$%^&*_~'''
    my_str = sentence
    no_punct = ""
    for char in my_str:
      if char not in punctuations:
            no_punct = no_punct + char
    return no_punct




def spellcheck (sentence):
        #this is the main spelling checker program
        global wordslist
        global lengthwords
        global addedwords
        global incorrect
        global wordsadded
        global wordschanged
        global correct



        sentence = stripper(sentence)
        sentence = sentence.casefold()
        wordslist = sentence.split()
        lenthwords= len(wordslist)


        j = 0
        # this block list up the words in the sentence andd bring them in the condition to be compared
        while j<lenthwords:
                 if wordslist[j] in englishwords:
            		    correct += 1
            		    #this block deals with all the correct words and icrement correct words
            		 
                 elif wordslist[j] not in englishwords:
                        #this block deals with incorrect word and informs the user about incorrect word
                        print("\n\n word ( " + wordslist[j] + " ) is incorrect ")
                        incorrect += 1
                        menu_word = input("\n\n Option 1 : Ignore the incorrect word \n Option 2 : Mark the word \n Option 3 : Add word to the dictionary \n Option 4 : Veiw the suggestion list \n\n Please entre Your desired Option  ")

                        if menu_word == str(1):
                            print("\n leaving the word as it is")
                            #this block just ignore the incorrect but increment incorrect words
                            print ("\n Redirecting....")
                            time.sleep(3)
                            

                        elif menu_word ==str(2):
                            # this will simply add question marks before and after the incorrect word
                            print ("\n\n ??? " + wordslist[j] + " ??? ")
                            wordslist[j] = (f' ??? {wordslist[j]} ???')
                            




                        elif menu_word == str(3):
                            #this block adds the incorrect word to the dictionary
                            print ("\n\nThe Word is Successfully added to the dictionary-file EnglishWords.txt")
                            correct += 1
                            incorrect -= 1
                            wordsadded += 1
                            Additions = open("EnglishWords.txt" , "a")
                            Additions.write(f'\n{wordslist[j]}')
                            



                        elif menu_word == str(4):
                            #this block provides all the suggestions 
                            print ("\n\n Here are all the possible solutions ")
                            suggestion = difflib.get_close_matches(wordslist[j],englishwords)
                            x = 0
                            for x in range(len(suggestion)):
                                print("  Suggestion number "  +  str(x)  + " : " + str(suggestion[x]))
                            menu3 = input ("\n Option 1 : Choose one of the suggestions \n Option 2 : Reject the suggestions and return \n\n ")    
                            while True:
                                if (menu3 == str(1)):
                                    y = int(input("\n\n Please entre the suggestion number :"))
                                    if y > (len(suggestion)-1):
                                        print("You have chosen an invalid option please try Again") 
                                        break
                                    wordslist[j] = suggestion[y]
                                    print(" Word Updated Successfully")
                                    wordschanged += 1
                                    break
                                    

                                elif (menu3 == str(2)):
                                    print("")
                                    continue
                                else:
                                    print ("invalid option")
                                    break
                                
                        else:
                            print (" \n\nOoops! invalid Option ")
                            break    
                 j += 1


        if correct == lenthwords:
             print("\n Hurray your Sentence has no spelling error, it looks like you are a Pro ")
             print( "\n Your sentence was :" + str(sentence))
             #verification if all the words are correctly spelt     
        

        return (wordslist)                
 





start = time.time()

print("\n\n Welcome to the Spell Checker")

while True :

    #this block will start the program and present the menu , based on the user inputs it will call the functions
    menu= input (" \n Option 1 : Spell check a sentence. \n Option 2 : Spell check a file \n Option 3 : Quit the Program \n\n Please entre your desired Option : ")

    if menu == str(1):
        #sentence entry point 

        sentence =input ("\n Please entre Your Sentence : \n\n ")
        filing = file_generator (spellcheck(sentence))
        break

    elif menu == str(2):
        # file input program

        while True:
            file =input ("\n Please entre the name of the file with extension( .txt ) :   ")
            if os.path.isfile(file):
                 print("")
                 f = open (f'{file}',"r")
                 content = f.read()
                 print("\n Checking .........")
                 time.sleep(2)
                 filing = file_generator (spellcheck(content))
                 break




            else:
                    #this block deals with invalid file input
                    print ("\n Ooops! This is an invalid file ")
                    menu2 = input("\n Option 1 : Re-entre the file-name for Spell Check \n Option 2 : Return to the main menu\n\n Please choose one : ")
                    if menu2 == str(1):
                         print("")
                    elif menu2 == str(2):
                         print("\n\n Loading........")
                         time.sleep(3)
                         break
                    else:
                         print ("\n\n Invalid Option , Re-entre file name : ")
                         time.sleep(1)        
                    


    elif menu ==str(3):
        #quit the program
        break

    else:
        print ("\n Oooops! Invalid Option\n Entre Again ")
        time.sleep(2)



f.close()
Additions.close()


end = time.time()


print ("\n Have a look a your spell check Statistics >>>")
print (f'\n Total Number of Words in the sentence  : {lengthwords}') 
print (f' Words Spelt Correctly : {correct}')
print (f' Incorrectly Spelt Words : {incorrect}')
print (f' Number of Words added to the Dictionary : {wordsadded}')
print (f' Number of Words Changed {wordschanged}')
print (f' Start time was : {start} \n Date is : {today}')
print (f' Elapse time : {end-start}')