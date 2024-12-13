# AutoDir
`[for python3]`

A python library to automatically switch the working directory to the parent folder of the code you're running. No more `cd` continuously!

## Usage
```py
switch(output=False)
```
Switches the working directory to the parent folder in the code.
### Parameters
`output` = `True/False/None` <br />
    -> `True`: prints output (current directory, parent directory of code, then current directory again after changing) <br />
    -> `False/None`: does not print any output.