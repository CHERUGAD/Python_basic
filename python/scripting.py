#retrive a path of the current working directory
import os

def current_directory():
    cwd=os.getcwd()     # os.getcwd() returns the absolute path of the directory where the script is running. Useful for checking where your script is executing.
    print("The current working directory is",cwd)
#This will retrive a path current working file

def file_path(filename):
    path=os.path.abspath(filename)   #os.path → A submodule inside the os module that handles file paths..abspath(filename) → Converts a relative path to an absolute path.
    print("The absolute path of the file is",path)

current_directory()
filename="thread.py"
file_path(filename)