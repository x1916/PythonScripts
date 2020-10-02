########################################################################
#
# SQLITE DATABASE ANALYSER BY PETER BYRNE
#
########################################################################


import sqlite3
import sys
import time

##### Print the usage of the script. ###################################

def usage():

	print("\nSQLite Database Analyser by Peter Byrne.\n")
	print("Usage: python " +sys.argv[0] +" <file1>\n")
	return 0

## End of usage() function.

## Function to convert from webkit timestamp to unix timestamp.
## Because this will be used many times.
## Pass in the Webkit Timestamp, returns the unix epoch timestamp.
##
## By Peter Byrne.

# webkit timestamp = number of microseconds since 01/01/1601.
# convert microseconds to seconds, by dividing microseconds by 1000000.
# then subtract the difference between webkit timestamp and start of
# unix epoch time, which is 11644473600. Result is unix epoch timestamp.

def convertWebkit(timestamp):

	convertedTime = long((timestamp / 1000000) - 11644473600)

	return convertedTime


# function to display the time in the format required by assignment.

def displayTime(epochTime):

	theTime = time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(epochTime))
	
	return theTime

########################################################################
#
# Main Script.
#
########################################################################

# If the arguments are not passed in correctly, call usage function.

if len(sys.argv) != 2:
	usage()
	sys.exit()

# initialise variables.

counter = 0

# Connect to the sqlite database which is passed in as a parameter from
# command line - sys.argv[1].

conn = sqlite3.connect(sys.argv[1])

# cursor position to the sqlite connection.

curs = conn.cursor()

# open the logfile for reading and writing, create if ! exist.

logFile = open("Byrne_Peter_15203514_Comp40120_chrome_report.txt", "w+")


# URL visits.

results = curs.execute("SELECT id, url, visit_count, last_visit_time FROM urls;")

for row in results:
#	print("ID: " +str(row[0]) +"\t" +"URL: " +str(row[1]) +"\t" +"Visit Count: " +str(row[2]) +"\t" +"Visit Time: " +str(time.strftime("%Y %m %d %H:%M:%S", time.gmtime(convertWebkit(row[3])))))
	print("ID: " +str(row[0]) +"\t" +"URL: " +str(row[1]) +"\t" +"Visit Count: " +str(row[2]) +"\t" +"Visit Time: " +str(displayTime(convertWebkit(row[3]))))
#	logFile.write("ID: " +str(row[0]) +"\t" +"URL: " +str(row[1]) +"\t" +"Visit Count: " +str(row[2]) +"\t" +"Visit Time: " +str(time.strftime("%Y %m %d %H:%M:%S", time.gmtime(convertWebkit(row[3])))) +"\n")
	logFile.write("ID: " +str(row[0]) +"\t" +"URL: " +str(row[1]) +"\t" +"Visit Count: " +str(row[2]) +"\t" +"Visit Time: " +str(displayTime(convertWebkit(row[3]))) +"\n")
	counter = counter + 1

# Print number of items:

print("\nNumber of URL history items: " +str(counter) +"\n")

# Downloads.

counter = 0

results = curs.execute("SELECT start_time, end_time, referrer, target_path, received_bytes, total_bytes, state FROM downloads;")

for row in results:
	print("START TIME: " +str(displayTime(convertWebkit(row[0]))) +"\tEND TIME: " +str(displayTime(convertWebkit(row[1]))) +"\tREFERRER: " +str(row[2]) +"\tTARGET PATH: " +str(row[3]) +"\tRECEIVED BYTES: " +str(row[4]) +"\tTOTAL BYTES: " +str(row[5]) +"\tState: " +str(row[6]))
	logFile.write("START TIME: " +str(displayTime(convertWebkit(row[0]))) +"\tEND TIME: " +str(displayTime(convertWebkit(row[1]))) +"\tREFERRER: " +str(row[2]) +"\tTARGET PATH: " +str(row[3]) +"\tRECEIVED BYTES: " +str(row[4]) +"\tTOTAL BYTES: " +str(row[5]) +"\tState: " +str(row[6]) +"\n")
	counter = counter + 1

print("Number of Downloads: " +str(counter))


# Keywords.

counter = 0

results = curs.execute("SELECT keyword_id, url_id, term FROM keyword_search_terms;")

for row in results:

	print("Keyword ID: " +str(row[0]) +"\tURL:" +str(row[1]) +"\tSEARCH TERM:" +str(row[2]) +"\n")
#	print("START TIME: " +str(displayTime(convertWebkit(row[0]))) +"\tEND TIME: " +str(displayTime(convertWebkit(row[1]))) +"\tREFERRER: " +str(row[2]) +"\tTARGET PATH: " +str(row[3]) +"\tRECEIVED BYTES: " +str(row[4]) +"\tTOTAL BYTES: " +str(row[5]) +"\tState: " +str(row[6]))
#	logFile.write("START TIME: " +str(displayTime(convertWebkit(row[0]))) +"\tEND TIME: " +str(displayTime(convertWebkit(row[1]))) +"\tREFERRER: " +str(row[2]) +"\tTARGET PATH: " +str(row[3]) +"\tRECEIVED BYTES: " +str(row[4]) +"\tTOTAL BYTES: " +str(row[5]) +"\tState: " +str(row[6]) +"\n")
	counter = counter + 1

#print("Number of Downloads: " +str(len(row))


# close logfile and sqlite database connection.

logFile.close
conn.close
