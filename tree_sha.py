
# Python program to demonstrate
# command line arguments
 
 
import sys
import subprocess

 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
     
#main program:
print("SHA-1 code: ", sys.argv[1]) #SHA-1: 3b54452c683ab37a1b565f0b559f6e26e1df79d9
cmd = ('git', 'cat-file','-p',sys.argv[1]) #use another command
process = subprocess.run(cmd, capture_output=True, text=True)
print(process.stdout)
