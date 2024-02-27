from difflib import SequenceMatcher
import difflib
import time
import os
from datetime import date

today = date.today()

Additions = open("EnglishWords.txt" , "a")


lengthwords, addedwords, incorrect, wordsadded, wordschanged, correct = 0, 0, 0, 0, 0, 0

# creating a list of words in the file
with open("EnglishWords.txt", "r") as f:
     words = f.read()
englishwords= words.splitlines()




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



        # this block list up the words in the sentence andd bring them in the condition to be compared
        j = 0
        for j in range(len(wordslist)):
             if wordslist[j] in englishwords:
        		    correct += 1
        		    #this block deals with all the correct words and icrement correct words
        		 
             elif wordslist[j] not in englishwords:
                    #this block deals with incorrect word and informs the user about incorrect word
                    print("\n\n word ( " + wordslist[j] + " ) is incorrect ")
                    incorrect += 1
                    menu_word = input("\n\n Option 1 : Ignore the incorrect word \n Option 2 : Mark the word \n Option 3 : Add word to the dictionary \n Option 4 : Veiw the suggestion list \n\n Please entre Your desired Option  ")

                    if menu_word == str(1):
                        print("leaving the word as it is")
                        #this block just ignore the incorrect but increment incorrect words
                        break

                    elif menu_word ==str(2):
                        # this will simply add question marks before and after the incorrect word
                        print ("\n\n ??? " + wordslist[j] + " ??? ")
                        break




                    elif menu_word == str(3):
                        #this block adds the incorrect word to the dictionary
                        print ("\n\nThe Word is Successfully added to the dictionary-file EnglishWords.txt")
                        correct += 1
                        incorrect -= 1
                        wordsadded += 1
                        Additions = open("EnglishWords.txt" , "a")
                        Additions.write(f'\n{wordslist[j]}')
                        break



                    elif menu_word == str(4):
                        #this block provides all the suggestions 
                        print ("\n\n Here are all the possible solutions ")
                        suggestion = difflib.get_close_matches(wordslist[j],englishwords)
                        for x in suggestion:
                            print("  Suggestion number " + str(x+1) + " : " + suggestion[x])
                        menu3 = input (" Option 1 : Choose one of the suggestions \n Option 2 : Reject the suggestions and return \n\n")    
                        while True:
                            if (menu3 == str(1)):
                                y = input("\n\n Please entre the suggestion number :")
                                wordslist[j] = suggestion[y-1]
                                print("Word Updated Successfully")
                                break

                            elif (menu3 == str(2)):
                                print("")
                                break
                            else:
                                print ("invalid option")
                            
                    else:
                        print (" \n\nOoops! invalid Option ")    
        


        if correct == lenthwords:
             print("\n Hurray your Sentence has no spelling error, it looks like you are a Pro ")
             #verification if all the words are correctly spelt
        return (wordslist)                
 



start = time.time()



while True :
    #this block will start the program and present the menu , based on the user inputs it will call the functions
    menu= input (" \n Option 1 : Spell check a sentence. \n Option 2 : Spell check a fil \n Option 3 : Quit the Program \n\n Please entre your desired Option : ")

    if menu == str(1):
        #sentence entry point 

        sentence =input ("\n Please entre Your Sentence : \n ")
        spellcheck(sentence)
        break

    elif menu == str(2):
        # file input program

        while True:
            file =input ("\n Please entre the name of the file with extension( .txt ) : \n ")
            if os.path.isfile(file):
                 print("")
                 f = open (f'{file}',"r")
                 content = f.read()
                 spellcheck(content)




            else:
                    #this block deals with invalid file input
                    print ("\n Ooops! This is an invalid file ")
                    menu2 = input("\n Option 1 : Re-entre the file-name for Spell Check \n Option 2 : Return to the main menu\n ")
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


end = time.time()




print (f'\n\n Total Number of Words in the sentence  : {lengthwords}') 
print (f' Words Spelt Correctly : {correct}')
print (f' Incorrectly Spelt Words : {incorrect}')
print (f' Number of Words added to the Dictionary : {wordsadded}')
print (f' Number of Words Changed {wordschanged}')
print (f' Start time was : {start} \n Date is : {today}')
print (f' Elapse time : {end-start}')