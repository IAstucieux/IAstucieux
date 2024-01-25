# IAstucieux
 Python library that allows easy use of AIs like Llama2 and Stable Diffusion and more.

### What is IAstucieux ? 
IAstucieux is a project carried out as part of our 3rd year of IT BUT

## Introduction
This library allows the use of Llama2 and Stable Diffusion through the use of "Automatic 1111". We are developing a framework that allows the use of these programs locally.

This project contains also the creation of a toolkit as a library that enables the easy use of some AI models
such as [Llama2](https://github.com/facebookresearch/llama) and [Stable Diffusion](https://github.com/CompVis/stable-diffusion), and that can be extended with additional AI models.<br/>
You will be able to use the models you installed through the library that is being developed here.

This project uses Python *3.9.2*, [Llama2](https://github.com/facebookresearch/llama) and [Stable Diffusion](https://github.com/CompVis/stable-diffusion) are included in the base installation.


## Members 
- Charly Flu - Leader of the project and Windows part
- Paolo Hoogland - MacOS part 
- Evguenia Sobine - Linux part 
- Océane Druenne - Linux part 
- Mattéo Tholey - Windows part 
- Sarah Heimburger - Windows part
- Baptiste Saul - Windows part 
- Lucas Grethler - Windows part 
- Isaïe Debèze - Windows part 


## Installation

To install the different AIs available, open the `installs` folder at the root of the project then choose whether you want to use the manual installation type or the automatic type by choosing the correct `manuals` or `automatics` folder. These folders contain all the installation instructions we have done so far for the different OS.

## Use our project 

In order to use our library, you must first launch the automatic 1111 API locally on your machine.

- The command to launch the 1111 API on Linux is: `./webui.sh --skip-torch-cuda-test --precision full --no-half --api`

Then, when developing your code in Python, simply import our library and create an “ia_stucieux” project.
It is then possible to configure the language model you wish to use by entering it in the path via the command `set_path_model_lama`, (for more details about the differents command available, you can check the file of the library located in `lib/ia-stucieux.py`)
An empty “models” folder is already present on this git in order to store the different models acquired.

After that, you finally have access to all the functions of our library to develop your application in Python.

It is possible to retrieve the results from the AI Llama and then process them as you wish depending on your needs, for example by continuing with the use of the AI Automatic 1111 where you can pass whatever you want in the prompt.


## Screenshots 

here is a little overview of what you get by using our library : 




## Issues 

- If you encounter some issues during the installation of llama2 or automatic1111, you can check the `HELP.md` file located in `installs/manuals/HELP.md`. This file contains a list of different errors that can be encountered with their associated solutions.

- If you have any other issues, please refer to the "issues" page and don't hesitate to create a new topic about your problem.
