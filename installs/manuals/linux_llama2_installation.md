# Llama2 installation on Linux
## Requirements


### **Download Python 3.9.2:**

Go to the official Python website to download version 3.9.2. You can do this using `wget` or a web browser. For example, to download the source file from the Python website, you can run the following command:
```bash 
   wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
```

### **Extracting the source file:**

Extract the contents of the downloaded file:
```bash
   tar -xzvf Python-3.9.2.tgz
```

### **Local compilation and installation:**

Once the source file has been extracted, you can compile and install Python 3.9.2 locally in your home directory. Make sure you have the development tools (gcc, make, etc.) installed on your system. Here's how to proceed: 

a. Go to the Python 3.9.2 source directory:
```bash
   cd Python-3.9.2
```

b. Configure Python for local installation:
```bash
   ./configure --prefix=$HOME/python-3.9.2
```

This will install Python 3.9.2 in a local directory, `$HOME/python-3.9.2`. c. Compile and install Python :
```bash
   make
   make install
```

### **Install pip**
Install pip using apt-get :
```bash
sudo apt-get update
sudo apt-get install python3-pip
```


## Llama2 installation


### Clone the project 
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```


### Build the project 
```bash
make
```


### Launch the project 
```bash
./main -m ./models/7B/ggml-model-q4_0.gguf -n 256 --repeat_penalty 1.0 --color -i -r "User:" -f prompts/chat-with-bob.txt
eeec4125e9c7560836b4873b6f8e3025 tokenizer.model
```

When executing this command, an error appears in the terminal: 
![error](https://i.ibb.co/f1st0C0/erreur.png)
To solve this problem : 

1 - Go to the models folder: 
```bash
cd models/
```

2 - You should see the following files: 
![folder](https://i.ibb.co/J5xVQxr/dossier.png)


3 - Add the following folders and files to this folder: 


- Folder 7B: Corresponds to the database for Llama2. Be careful, the folder is quite large.


![size](https://i.ibb.co/FHPkknM/taille.png)


- The tokenizer.model file
- The file tokenizer_checklist.chk


If you've copied all the necessary files and folders, here's what your models folder should look like: 


![archi](https://i.ibb.co/VBbd1Fj/archi.png)
### Using a Hugging Face model 

1 - Download the following model: 
```
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf 
```

2 - Copy and paste the file into the following folder: 
![doss](https://i.ibb.co/bFMTtzM/doss.png)

### Launching the project 
1 - Run the : 
```bash
./main -m ./models/7B/ggml-model-q4_0.gguf -n 256 --repeat_penalty 1.0 --color -i -r "User:" -f prompts/chat-with-bob.txt
eeec4125e9c7560836b4873b6f8e3025 tokenizer.model
```

If all went well, you should see in the terminal : 

![resultat](https://i.ibb.co/jV2H55H/result.png)

Congratulations, you've just installed Llama2 on Linux! 
