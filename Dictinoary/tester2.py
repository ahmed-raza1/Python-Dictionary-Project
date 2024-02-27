from difflib import SequenceMatcher
import difflib



Additions = open("EnglishWords.txt" , "a")


lengthwords, addedwords, incorrect, wordsadded, wordschanged, correct = 0, 0, 0, 0, 0, 0


def stripper(sentence):
	# this function will remove all the puctuation marks and numbers form the sentence
  punctuations = '''!()-[]{};:'"1234567890,<>./?@#$%^&*_~'''
  my_str = sentence
  no_punct = ""
  for char in my_str:
      if char not in punctuations:
            no_punct = no_punct + char
  return no_punct


def spellcheck (sentence):
	global lenthwords
	global addedwords
	global incorrect
	global wordsadded
	global wordschanged
	global correct

	# creating a list of words in the file
	with open("EnglishWords.txt", "r") as f:
		words = f.read()
	englishwords= words.splitlines()

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
         			print("\n\n word ( " + wordslist[j] + " ) is incorrect ")
         			incorrect += 1
         			menu_word = input("\n\n Option 1 : Ignore the incorrect word \n Option 2 : Mark the word \n Option 3 : Add word to the dictionary \n Option 4 : Veiw the suggestion list \n\n Please entre Your desired Option  ")
         			
         			if menu_word == str(1):
         				print ("\n\n Leaving the word as it is ")
         				# this choice will siply ignore the incorrect word but it will increment on incorrect words

         			elif menu_word ==str(2):
         				print ("\n\n ??? " + wordslist[j] + " ??? ")




         			elif menu_word == str(3):
         				print ("\n\nThe Word is Successfully added to the dictionary-file EnglishWords.txt")
         				correct += 1
         				incorrect -= 1
         				wordsadded += 1 

         			elif menu_word == str(4):
         				print ("\n\n Here are all the possible solutions ")
         				suggestion = difflib.get_close_matches(wordslist[j],englishwords)
         				print (suggestion)
         				

         			else:
         				print (" \n\nOoops! invalid Option ")    					


         				



	return ( wordslist, lenthwords)


print("\n\n" + str(spellcheck("My45456 NAME Python's 123*#$%^&*  hoT")))
print(correct)

print (f'\n\n Total Number of Words in the sentence  : {lenthwords}') 
print (f' Words Spelt Correctly : {correct}')
print (f' Incorrectly Spelt Words : {incorrect}')
print (f' Number of Words added to the Dictionary : {wordsadded}')
print (f' Number of Words Changed {wordschanged}')