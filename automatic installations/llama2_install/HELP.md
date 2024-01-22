# HELP !
## Purpose of this document
In this file you will have a list of errors you can have during the installation of llama2 or automatic1111.
Use this document to maybe find an answer to one of your problem, `ctrl+f` your error and maybe find some answers !

## I don't see my error here
Please if you encounter a new error create an **issue**, and we'll be happy to help and make this document cover even more problems !

## Errors lists
Here's starts the errors list : 


### Pip not installed

```bash
pip: command not found
```

Well, it's in the name, you'll need pip to run our installations scripts, try to execute `prerequisites.sh` first.

Or you can do this on linux : 
```bash
$> sudo apt install python3-pip
```
Or go here on windows : 
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

It can be multiple reasons for that, if you're on linux try this : 
```bash
$> sudo apt update
```

```bash
$> sudo apt install python3
```

Then add this lines : 
```text
deb http://archive.ubuntu.com/ubuntu focal universe
deb-src http://archive.ubuntu.com/ubuntu focal universe
```

To this file `/etc/apt/sources.list`, you can use nano like this :
```bash
$> sudo nano /etc/apt/sources.list
```

Then run apt update again : 
```bash
$>sudo apt update
```

And try again : 
```bash
$> sudo apt install python3-pip
```


