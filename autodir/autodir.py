import os
from pathlib import Path

def switch(output=None):
    """
    Autoswitches directories.
    
    Parameter output: Can be either None (default) or 1, where None returns no output and 1 returns detailed output. Both still change directories.
    """
    if output == 1:
        print("CWD: ", os.getcwd())
        os.chdir(Path(__file__).parent.absolute())
        print("Parent: ", Path(__file__).parent.absolute())
        print("CWD: ", os.getcwd())
    elif output == None:
        os.chdir(Path(__file__).parent.absolute())
