import os
import subprocess
import sys
import requests
import base64
from PIL import Image
import io


def printStep(step):
    print("\n\n")
    print("=================================================================================")
    print("================================STEP ",step,"===================================");
    print("=================================================================================")
    print("\n\n\n\n\n")


#by default try to use python 3.11, you can change it here or when calling the script
python_version="3.11"
if len(sys.argv) >= 2:
    python_version = sys.argv[1]


def install_llama():
    # Step 1 : update the system
    printStep(1)
    os.system("sudo apt-get update")

    # Step 2 : create a virtual env for python 
    printStep(2)
    if(os.system("python"+python_version+" -m venv .venv")):
        print("Failed to install python env, try skipping this steps (2-3), exiting...")
        return

    else:
        print("Installed python env with success !")


    # Step 3 : Install needed package
    printStep(3)
    if(os.system(".venv/bin/pip"+python_version+" install requests Pillow")):
        print("Failed to install needed packages, try skipping this step or manually install it")
        return

    else:
        print("Installed python env packages with success !\n")

    # Step 4 : create a virtual env for python 
    printStep(4)
    if(os.system(".venv/bin/pip"+python_version+" install llama-cpp-python"))
        print("Failed to install with pip the llama cpp package :/\n")
        return

    else:
        print("Llama cpp package installed successfully !\n")

    # End !
    print("\nNow, download a llama2 language model here : https://ai.meta.com/llama/ \n"+
        "Then update the model path in the llama_example.py to your model path\n"+
        "And then launch it with : \n"+
        ".venv/bin/python"+python_version+" llama_example.py\n")
    
install_llama()
