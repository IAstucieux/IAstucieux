# Llama 2 installation on Windows
## Requirements 
### Clone the project
Clone the official llama.cpp project
````bash
git clone https://github.com/ggerganov/llama.cpp
````

### w64devkit
Quit the folder, create a new folder called w64devkit. Go into it, then download [w64devkit](https://github.com/skeeto/w64devkit/releases) (latest version in .zip).

Extract the folder and run **w64devkit.exe**.

A terminal will open. Go back to the llamacpp folder and run the following command: 
````bash
make
````

Once the command is complete, run the following command: 
````bash
python3 -m pip install -r requirements.txt
````
This may vary from one computer to another: you'll need to test with python3 or just python. 

### Models
Go to the models folder in llamacpp. Create a 7B folder and copy all the contents of the models folder into 7B. Your 7B folder should look like this: 
![llama2-folder-7b](https://i.ibb.co/tpd33n1/llama2-tuto1.png)

### test-7B.git
Clone the following directory: 
````bash
git clone https://github.com/oceanedruenne/test-7B.git
````

### Tokenizer
Move the **tokenizer.model** and **tokenizer_model.chk** files to the **models** folder. 
Move the file **checklist.chk** to folder **7B**.

Upload the following model to the 7B folder: 
````bash
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf  
````
### Execute
Return to the w64devkit terminal and execute the following command: 
````bash
./main -m ./models/7B/ggml-model-q4_0.gguf -n 256 --repeat_penalty 1.0 --color -i -r "User:" -f prompts/chat-with-bob.txt eeec4125e9c7560836b4873b6f8e3025 tokenizer.model
````

If all went well, you should see this in the terminal: 
![terminal llama2](https://i.ibb.co/6nSFT82/llama2-tuto2.png)

Congratulations, Llama2 is now installed on your Windows machine!
