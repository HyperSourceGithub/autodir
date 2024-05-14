import os
from pathlib import Path

def switch(output=None):
    if output.lower() == "detailed":
        print("CWD: ", os.getcwd())
        os.chdir(Path(__file__).parent.absolute())
        print("Parent: ", Path(__file__).parent.absolute())
        print("CWD: ", os.getcwd)
    elif str(output) == "None":
        os.chdir(Path(__file__).parent.absolute())