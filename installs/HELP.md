# HELP !

In this file you will have a list of errors that can be encountered during the installation of llama2 or automatic1111.
This document will shine some light on the possible problems, but doesn't contain every single possible answer. If you encounter a new error create an **issue**, and we'll be happy to help and make this document cover even more problems !

## Error list
Here starts the errors list : 


### Pip not installed

```bash
pip: command not found
```

You'll need pip to run our installation scripts. Either try to execute `prerequisites.sh` first, or execute : 
```bash
$> sudo apt install python3-pip
```
On windows, go here  : 
https://pip.pypa.io/en/stable/installation/ 


### Cannot install pip

```bash
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Package python3-pip is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'python3-pip' has no installation candidate
```

There are many reasons that can explain this error.
If you're on linux try this : 
```bash
$> sudo apt update
```

```bash
$> sudo apt install python3
```

Edit the file `/etc/apt/sources.list` :
```bash
$> sudo nano /etc/apt/sources.list
```
Then add these lines : 
```text
deb http://archive.ubuntu.com/ubuntu focal universe
deb-src http://archive.ubuntu.com/ubuntu focal universe
```


Run apt update again : 
```bash
$>sudo apt update
```

And try to install python again : 
```bash
$> sudo apt install python3-pip
```
