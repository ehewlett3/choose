import textwrap

def displayPage(num):
	for line in textwrap.wrap(pages[num]): # display page text
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

# START PROGRAM
# initialize data - read from files or create empty variables

try:
	f = open("pages.dat") # read pages
	pages = f.readlines()
	f.close()
except IOError:
	pages = []
try:
	f = open("choices.dat") # read choices
	choices = f.readlines()
	f.close()
except IOError:
	choices = []
i = 0 # strip newlines from pages
for page in pages:
	if page[len(page)-1]=="\n":
		pages[i] = page[:len(page)-1]
	i+=1
i=0 # strip newlines from choices and explode
for choice in choices:
	if choice[len(choice)-1]=="\n": # strip newlines
		choices[i] = choice[:len(choice)-1]
	choices[i] = choices[i].split('|') # explode
	j=0 # turn number strings into integers
	for item in choices[i]:
		if item.isdigit():
			choices[i][j] = int(item)
		j+=1
	i+=1

history = []
print
main()