import sys
import subprocess
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("Root file name: ", sys.argv[1]) 
print("")

# Main program
# name of the file: tree_sha.py
cmd = ('git', 'log','--pretty', '--',sys.argv[1], '-1') #use another command
process = subprocess.run(cmd, capture_output=True, text=True)

info = process.stdout
print(info)