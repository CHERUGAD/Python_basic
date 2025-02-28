# main.py
import module_usage  # Import whole module

# Access function
module_usage.exampleFuncn("test")

from module_usage import exampleFuncn ##For accessing specific function

exampleFuncn("test")


if __name__ == "__main__":
    exampleFuncn("Direct Call")

