from autodir import autodir

help(autodir.switch())
choice = input("Enter choice of 1 or None: ")
if choice == "None":
    autodir.switch()
elif choice == "1":
    autodir.switch(1)
