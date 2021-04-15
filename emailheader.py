# Python Script to parse e-mail

import sys

##### Print the usage of the script. ###################################

def usage():
    print ("Sctipt to parse Google Disclosed E-Mail Headers\n")
    print ("Usage: python " +sys.argv[0] +" <file1>\n")
    return 0

## End of usage() function.


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

# open the logfile for reading.

try:
    logFile = open(sys.argv[1], "r")
except (IOError, ValueError) as e:
#    print ("Could not find file: " +sys.argv[1])
    print(e)