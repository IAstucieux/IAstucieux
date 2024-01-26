# Automatic 1111 installation on Linux 
## Requirements
- Python 3.9.2
- Debian 11

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

### **Using Python 3.9.2:**

You can now use Python 3.9.2 using the full path to the Python interpreter you have installed. For example:
```
   $HOME/python-3.9.2/bin/python3.9
```

## Automatic 1111 installation

### Download Automatic 1111 source file: 
```bash
wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh
```

### Grant rights: 
```bash
chmod 777 webui.sh
```

### Run the program: 
```bash
./webui.sh
```

If the installation has gone smoothly, you should see in your terminal : 
![stable](https://i.ibb.co/b76q36X/stable.png)

And a page on your browser should open: 
![generated](https://i.ibb.co/x6M7fwb/generated.png)

Congratulations, Automatic 1111 is now installed on your Linux machine!

## Errors

Warning: if the torch installation fails (code error 137), run the command again until it works.

If you get the error "Torch is not able to use GPU", run the following command: 

```bash
./webui.sh --skip-torch-cuda-test
```

If you get the error "LayerNormKernelImpl" not implemented for 'Half'", run the following command: 

```bash
./webui.sh --skip-torch-cuda-test --precision full --no-half
```
