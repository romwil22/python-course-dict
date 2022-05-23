import os

if os.path.exists("pythonQuestion.txt"):
    print("Text file deleted.")
    os.remove("pythonQuestion.txt")
else:
    print("Text file doesn't exist.")