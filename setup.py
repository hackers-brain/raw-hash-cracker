import os
try:
    os.system("pip3 install colorama")
    os.system("clear")
    print(" Setup Installed Successfully !!!")
    os.system("python3 main.py")
except Exception as error:
    print(f"\n {error}\n  Error Encountered...")