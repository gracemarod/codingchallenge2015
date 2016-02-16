############################################################################
# Author: Grace M. Rodriguez Gomez\
# Codetrotters Challenge
# 02/15/2016
# Description: Given an input of an integer from 0 to 999,999,9999
# the script proceeds to translate it into words depending on its units.
############################################################################

#List of the numbers words depending on units.
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = [ "ten" ,"eleven" ,"twelve", "thirteen" , "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tenths = [ "ten","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def int_to_words(num):
	hundreds = ""
	thousands = ""
	millions = ""
	finalString = ""
	count = 0

	#Iterate through the srping in reversed, this is done so the hundreds can be gotten first, the thousands
	#second and the millions last 
	for i in reversed(num):
		count += 1
		#The number is seperated to three parts each containing three digits each.
		if count <= 3:
			hundreds += i
		elif count >3 and count <=6:
			thousands += i
		elif count > 6: 
			millions += i

	#Each part is reversed
	hundreds = hundreds[::-1]
	thousands = thousands[::-1]
	millions = millions[::-1]
	
	#Depending if there are millions or thousands, enter the getWords function 
	if len(millions) > 0:
		#Add the resulting string from getWords and saved the corresponding words according to its units
		finalString += getWords(millions) + " million "
	if len(thousands) > 0:
		finalString += getWords(thousands) + " thousand "
	
	hStr = getWords(hundreds)
	
	finalString += hStr

	print finalString


def getWords(wordParts):
#This function is going to convert the segregated parts of the input number to words. 
#Each part has a maximum of 3 digits and a minimum of 1.

	numWords = ""

	#If the length of the word part is only one, then it's just one unit, and it will be 
	#search in the list of ones.
	if len(wordParts) == 1:
		numWords += ones[int(wordParts[0])-1]

	#If the length of the word is two, then it will search either in the teens list if its
	#first digit is 1 or in the tenths list if the first digit is bigger than 1.   
	elif len(wordParts) == 2:
		if int(wordParts[0]) == 1:
			numWords += teens[int(wordParts[1])]
		elif int(wordParts[0]) >= 2 and int(wordParts[1]) == 0:
			numWords += tenths[int(wordParts[0])-1]
		elif int(wordParts[0]) >= 2 and int(wordParts[1]) > 0: 
			numWords += tenths[int(wordParts[0])-1] + "-" + ones[int(wordParts[1])-1]
	
	#If the length of the word is three, then there are a couple of cases than can happen.
	elif len(wordParts) == 3:
		#If the first digit is not 0, look for the digit in the ones list and add a "hundred" 
		if int(wordParts[0]) != 0:
			numWords = ones[int(wordParts[0])%10-1] + " hundred "
		#Second digit is 1, look for the digit in teens list
		if int(wordParts[1]) == 1:
			numWords += teens[int(wordParts[2])]
		#Second digit is bigger than on, look in tenth list
		elif int(wordParts[1]) >= 2 and int(wordParts[2]) == 0:
			numWords += tenths[int(wordParts[1])-1]
		#If the third digit isn't cero, add a "-" and the corresponding word for the ones list
		elif int(wordParts[1]) >= 2 and int(wordParts[2]) > 0: 
			numWords += tenths[int(wordParts[1])-1] + "-" + ones[int(wordParts[2])-1]
		#If 2nd digit is 0 and the 3rd >= 1, add the corresponding word 
		elif int(wordParts[1]) == 0 and int(wordParts[2]) >= 1:
			numWords += ones[int(wordParts[2])-1]
	return numWords
	
def main():
	#Get input. Make sure it's an integer and in the accepted range.
	while True:
		try:
			num = int(raw_input("Please choose a number from 0 to 999999999 without comas. "))		
			if (num > 999999999):
				print "Number exceeds limits, please put a number from 0 to 999,999,999. "
				num = int(raw_input(""))
			if num == 0:
				print "zero"
			else:
				int_to_words(str(num))
				command = raw_input("Would you like to convert another integer? y/n  ")
				if command == "n":
					break	
		except ValueError:
			print "Oops! Input should be an integer. Try again."			


if __name__ == "__main__":
    main()