def displayPage(num):
	print pages[num] # display page text
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
	while newChoicePage > i:
		newChoicePage = input("...leads to page #: ")
	if newChoicePage == i:
		addPage()
	choices.append([pageNum, newChoiceText, newChoicePage-1])

def addPage():
	newPageText = raw_input("New page: ")
	
def main():
	pageNum = 0
	while True:
		currChoices=displayPage(pageNum)
		yourChoice=99
		while yourChoice > len(currChoices):
			yourChoice=input("Choose now! ")
		if yourChoice==0:
			addChoice(pageNum)
		else:
			pageNum=currChoices[yourChoice-1]

f = open("pages.dat") # read pages
pages = f.readlines()
f.close()
f = open("choices.dat") # read choices
choices = f.readlines()
f.close()
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

main()