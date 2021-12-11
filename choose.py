print
print "Choose NOW!"
print
print 'A "Choose Your Own Adventure"-style storyteller and story creation tool.'
print
print "Created and made freely available under the GPL by Edward Hewlett"
print "with help (and with thanks due to) the students of TLA CompuTech 2013"
print

# IMPORT modules

import textwrap # import textwrap module so we can properly wrap long lines of text

# DEFINE functions

def displayPage(num):
    for line in textwrap.wrap(pages[num]): # display page text
        if line[len(line) - 3: len(line)] == "END":
            print line[0: len(line) - 3]
            return 'endingprogram'
        else:
            print line
    currChoices = []
    
    i=0 # display choices
    j=0
    for choice in choices:
            if choice[0]==num:
                print j+1, choice[1]
                j+=1
                currChoices.append(choice[2])
            i+=1
    return currChoices

def addChoice(pageNum):
    newChoiceText = raw_input("New choice: ")
    i=0 # display pages
    for page in pages:
            print i+1, page
            i+=1
    newChoicePage = 9999
    print str(i+1)+" ADD NEW PAGE"
    while newChoicePage > i+1:
            try:
                    newChoicePage = input("...leads to page #: ")
            except:
                    newChoicePage = 9999
    if newChoicePage == i+1:
            addPage(i+1)
    choices.append([pageNum, newChoiceText, newChoicePage-1])
    f=open("choices.dat","a")
    f.write(str(pageNum)+"|"+newChoiceText+"|"+str(newChoicePage-1)+"\n")
    f.close()

def addPage(newPageNum):
	newPageText = raw_input("New page: ")
	pages.append(newPageText)
	f=open("pages.dat","a")
	f.write(newPageText+"\n")
	f.close()

def main():
    pageNum = 0
    while True:
        if pageNum > len(pages) or pages == []:
                addPage(len(pages))
        currChoices=displayPage(pageNum)
        yourChoice=99
        if currChoices == 'endingprogram':
            userInput = raw_input("Do you want to play again? (Y/N) ")
            userInput = userInput.lower()
            if userInput.startswith('y'):
                print
                main()
            else:
                break
        else:
            while yourChoice > len(currChoices):
                try:
                    yourChoice=input("Choose now! ")
                except:
                    yourChoice=99
            print
            if yourChoice==0: # secret add choice option
                addChoice(pageNum)
            elif yourChoice==-1: # secret go back option
                if history == []:
                    pageNum = 0
                else:
                    pageNum=history.pop()
            elif currChoices[yourChoice-1] >= len(pages): # if page doesn't exist...
                addPage(len(pages))
            else:
                history.append(pageNum)
                pageNum=currChoices[yourChoice-1]

# INITIALIZE data - read from files and/or create empty variables

''' PAGES.DAT file

Contains the story's text, organized in "pages" 
- one page-text per list item, starting with list-item # (page #) 0
- ending pages are indicated by finishing the page text with the word "END"

'''

# read pages from text-file "pages.dat", one page per line, stored in list "pages"
try:
        f = open("pages.dat") # open file to read data
        pages = f.readlines() # one page per line, stored in list "pages"
        f.close() # close file
except IOError: # if attempt to open/find/read file failed...
        pages = [] # ...start with empty list (no pages)

# strip newlines from pages
i = 0 # initialize counter variable "i" (start counting at zero!)
for page in pages: # go through "pages" list, storing each page-text in "page"
	# note: modifying pages list directly so that multiple changes don't get lost...
	pages[i]=pages[i].replace('\r','') # replace any Windows new-line characters with ''
	pages[i]=pages[i].replace('\n','') # replace any standard new-line chars with ''
	i+=1 # next page

# read choices from text-file "choices.dat", each line structured as follows:
# 0 [page where choice appears] | go north [choice text] | 1 [page to which choice leads]
try:
        f = open("choices.dat") # open file to read data
        choices = f.readlines() # one choice data-set per line stored in list "choices"
        f.close() # close file
except IOError: # if attempt to open/find/read file failed...
        choices = [] # ...start with empty list (no choices)

# strip newlines from choices and explode data
i=0 # set main list index counter to zero (start at beginning of list of choices)
for choice in choices: # go through list of choice data-sets
        choices[i] = choices[i].split('|') # separate data-set (divider=|) into sub-list 
        j=0 # initialize sub-list counter
        for item in choices[i]: # go through each item in the choice data-set
				choices[i][j]=choices[i][j].replace('\r','') # remove Windows new-lines
				choices[i][j]=choices[i][j].replace('\n','') # remove std new-line chars
				if choices[i][j].isdigit(): # if choice item is a number...
					choices[i][j] = int(choices[i][j]) # ...convert string to integer
				j+=1 # increment sub-list counter
        i+=1 # increment main-list counter

history = [] # start with no page-view history
print

# START MAIN PROGRAM

main()

