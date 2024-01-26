#!/bin/bash

#by Evguenia
WARNING_COLOR='\x1b[33;3m'
WARNING_COLOR_BOLD='\x1b[33;1;3m'
NO_COLOR='\033[0m'
GREEN='\033[32m'
BLUE='\x1b[34m'
RED='\x1b[31m'
MAGENTA='\x1b[35;3m'
SUDO_RIGHTS=0

printStep() {
    echo -e "\n\n"
    echo -e "================================${BLUE}STEP $1/5${NO_COLOR}==================================="
    echo -e "${BLUE}$2${NO_COLOR}"
}

# Step 0 : Retrieve the user agrs and update system
printStep 0 "Retrieve the user arguments (python version and path to venv if given) and update system if sudo rights..."

python_version="3.11"
venv_directory="../../.venv"
if [ $# -ge 1 ]; then
     python_version=$1
fi
echo -e "${GREEN}Python version that will be used for doing installation is ${python_version}${NO_COLOR}"

if [ $# -ge 2 ]; then
     venv_directory=$2
fi
echo -e "${GREEN}Directory for the venv environnement will be ${venv_directory}${NO_COLOR}"

if sudo -v; then
     SUDO_RIGHTS=1
     sudo apt-get update
     echo -e "${GREEN}\nUpdating system is done.${NO_COLOR}"
fi

# Step 1 : Check if the user has sudo rights
printStep 1 "Check if the user has sudo rights..."

if [ $SUDO_RIGHTS -eq 1 ]; then
     # Installing pip
     sudo apt-get install -y python3-pip

     # Installing python needed modules
     sudo pip3 install requests Pillow

     # Installing git
     sudo apt-get install git

     # Installing c++ compiler for python
     sudo apt install python3-dev

     # Dependencies for Automatic 1111
     sudo apt install wget python3 python3-venv libgl1 libglib2.0-0
 
     SPECIFIC_CASE=3.11
     if [ ${python_version} == ${SPECIFIC_CASE} ]; then
          sudo apt-get install python3.11-venv
     fi  

     echo -e "${GREEN}\nEvery prerequisites installs are done.${NO_COLOR}"
     
else
     # If the user doesn't have sudo rights
     echo -e "${WARNING_COLOR}Please make sure to have python3-pip, Pillow modules, git, python3, python3-dev, python3-venv, libgl1, libglib2.0-0, tcppinglib installed on your machine. \nRefer to the installation manual for more information.${NO_COLOR}"
fi

# Step 2 : Create a virtual env for python 
printStep 2 "Create a virtual env for python..."

if ! python${python_version} -m venv $venv_directory; then
    echo -e "${RED}Failed to install python env. Make sure that your current version of python is ${python_version} or at least is 3.9 or 3.11${NO_COLOR}"
    echo -e "${RED}Refer to the installation manual for more information.${NO_COLOR}"
    exit 1
else
     echo -e "${GREEN}Installed python env with success !${NO_COLOR}"
fi

# Step 3: Install needed package
printStep 3 "Install needed package..."
if ! $venv_directory/bin/pip$python_version install requests Pillow tcppinglib; then
     echo -e "${RED}Failed to install needed packages, try skipping this step or manually install them.${NO_COLOR}"
     exit 1
else
     echo -e "${GREEN}Installed python env packages with success !${NO_COLOR}"
fi

# Step 4: Create a virtual env for python
printStep 4 "Create a virtual env for python..."
if ! $venv_directory/bin/pip$python_version install llama-cpp-python; then
     echo -e "${RED}Failed to install with pip the llama cpp package :/${NO_COLOR}"
     exit 1
else
     echo -e "${GREEN}Llama cpp package installed successfully !${NO_COLOR}"
fi

# Step 5: Get the webui.sh from Automatic1111 repot
printStep 5 "Get the webui.sh from Automatic 1111 repot..."
if ! wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh; then
    echo -e "${RED}Failed to retrieve the webui.sh from Automatic1111 repot. Refer to https://github.com/AUTOMATIC1111/stable-diffusion-webui to install it manually.${NO_COLOR}"
     exit 1
else
     echo -e "${GREEN}webui.sh retrieve successfully !${NO_COLOR}"
fi

# Last instructions for continue
echo -e "${MAGENTA}\nNow, download a llama2 language model here : https://ai.meta.com/llama/ \nThen update the model path in the llama_example.py to your model path\nAnd then launch it with : \n${venv_directory}/bin/python${python_version} llama_example.py\n${NO_COLOR}"
echo -e "${MAGENTA}\nFor Automatic1111, give rights to webui.sh then run it with preferred arguments.${NO_COLOR}"

echo -e "${MAGENTA}\nRefer to the install manual for more information.${NO_COLOR}"

