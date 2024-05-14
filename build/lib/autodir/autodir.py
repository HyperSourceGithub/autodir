import os
from pathlib import Path

def switch(output=None):
    if output == 1:
        print("CWD: ", os.getcwd())
        os.chdir(Path(__file__).parent.absolute())
        print("Parent: ", Path(__file__).parent.absolute())
        print("CWD: ", os.getcwd())
    elif output == None:
        os.chdir(Path(__file__).parent.absolute())