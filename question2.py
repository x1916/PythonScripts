## question 2
##
##

# open the files. w+ creates for r/w if they dont exist.

myFile = open("report.txt", "w+")
newFile = open("newreport.txt", "w+")

# get input and write it to a line in the file.
myFile.write(raw_input("Please input a sentence: ")+"\n")


# Set file position back to the start of the file.
myFile.seek(0,0)

# Write the lines from myFile into newFile.
newFile.writelines(myFile.readlines())

# Print contents of new file.
newFile.seek(0,0)

for line in newFile:
	print(line)

# close the files.
myFile.close()
newFile.close()

