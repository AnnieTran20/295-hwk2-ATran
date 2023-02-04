# Python program to demonstrate
# command line arguments
 
import sys
import subprocess
     
#main program:
#SHA-1 commit: 3b54452c683ab37a1b565f0b559f6e26e1df79d9
cmd = ('git', 'cat-file','-p',sys.argv[1]) #use another command
process = subprocess.run(cmd, capture_output=True, text=True)

info = process.stdout

treeCode = info.split("\n")[0][5:] #The first line is tree information, substring staring from index 5 is the sha1 code
print(treeCode)
