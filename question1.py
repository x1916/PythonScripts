## question1.py
##
## Name: Peter Byrne
## Programming for Investigators - Assignment 1
##
##

# define the lists.
gunners = ["ljungberg","pires","vieira","bergkamp","henri","wright","adams","overmars","campbell","kanu","petit","cole","anelka"]
newgunners = []
sliced = []

i = 0		# counter
z = 0		# counter2

#longest = 0
#shortest = 0


##### PART (A)

# print the number of items.

print("The gunners list has " +str(len(gunners)) +" items. \n")

##### PART (B) and PART (C)

# main while loop, to iterate through all elements of list. newgunners[]
# list is populated during this iteration for efficiency. the counter
# y is used to count the characters in each string element in the list.
# this y counter is reinitialised at the start of each iteration through
# the gunners[] list.

while i < len(gunners):

	y = 0
	
# loop for calculating length of each string element in gunners[] list.

	while y < len(gunners[i]):
		y = y + 1				# count the number of letters.
	
	print(gunners[i] +" has " +str(y) +" letters.")
	
	if len(gunners[i]) < 6:

		newgunners.append(str(gunners[i])) 	# if less than 6 characters then append to newlist.
	
	i = i + 1

# print newgunners list.

print("\nList elements less than 6 characters:" + str(newgunners))

# print the newgunners elements (entries less than 6 characters) using iteration.
# dont think this is necessary, and could save memory for z counter,  but i have included it anyway.

while z < len(newgunners):

	print (newgunners[z])
	z = z + 1

# reinitialise i counter, for use with next while loop for assignment.

i = 0

## second iteration of gunners[] list.

print("\nGreater than 8 characters:\n")


##### PART (D)

# while loop through gunners[] list, and if greater than 8 characters,
# print this list, minus the last character. using a new list called
# sliced[] to store characters in string and slice off last character.

while i < len(gunners):

	if len(gunners[i]) >= 8:
		sliced = gunners[i]
		print(sliced[:-1])

	i = i + 1
print		# blank line

##### PART (E).

# Print longest and shortest.
# loop through list and determine longest.

#for i in range(len(gunners)):
#	print(i)	# counter used for debugging.
#	if int(len(gunners[i])) > longest:
#		longest = len(gunners[i])


# loop through list and determine shortest, using longest as initial value.

#shortest = longest

#for i in range(len(gunners)):
#	if int(len(gunners[i])) < shortest:
#		shortest = len(gunners[i])		

#print("Longest entry is: " + str(longest) + " characters.")
#print("Shortest entry is: " + str(shortest) + " characters.")
#print("\n")

# now create a new list with the longest strings from gunners[] list.

#longList = []		# initialise an empty list to store longests.

#for i in range(len(gunners)):
#	if int(len(gunners[i])) == longest:
#		longList.append(gunners[i])

#print("The longest words are: " +", ".join(longList))

#shortList = []		# initialise an empty list to store shortests.

#for i in range(len(gunners)):
#	if int(len(gunners[i])) == shortest:
#		shortList.append(gunners[i])

#print("The shortest words are: " +", ".join(shortList))

## end.


########################################################################
# this method uses a python sort function, and should be more efficient
# for longer lists, as the list is sorted and iterations only take place
# until the boolean condition for 'loop' is false, ie. the next highest
# or next lowest element is no longer higher or lower.
#

# sort a list by length of string elements.

sortedGunners = sorted(gunners, key=len)

# set counter to start at the end of the sorted list.

i = len(sortedGunners) - 1 		# start at the end.

# boolean condition to loop/iterate the while loop. initialise to true.

loop = True

# Last element in sorted list will be the biggest, so set to first element in longList.

longList = [sortedGunners[i]]

# if previous element is >= to highest element, append to longList.
# if not, break out of loop.

while loop:
	if len(sortedGunners[i - 1]) >= len(sortedGunners[i]):
		longList.append(sortedGunners[i])
	else:
		loop = False
	
	i = i - 1


print("The longest words are: " +", ".join(longList))

## Shortest

i = 0				# Start at the start this time.

loop = True

shortList = [sortedGunners[i]] 		# First element in sorted list will be the shortest, so set to first element in shortlist.

# if next element is <= to shortest element, append to shortList.
# if not, break out of loop.

while loop:
	if len(sortedGunners[i + 1]) <= len(sortedGunners[i]):
		shortList.append(sortedGunners[i + 1])
	else:
		loop = False
	
	i = i + 1

print("The shortest words are: " +", ".join(shortList))

print("\nFINISHED!")
