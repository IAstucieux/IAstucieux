# Script to install Llama2 on linux (needs testing for Windows)

## Instructions 

First do this to install the dependencies :
```bash
$> sh prerequisites.sh
```

Then execute this script with or without the version you want, you can choose "3.9" or "3.11" or something else if it doesn't work.
```bash
$> python3 install_llama.py <version>
```
If you have a problem finding the corresponding version of your python, when the env is setup, look in `.venv/bin` and choose your version.

Then the script tells you to download a model here : 
> https://ai.meta.com/llama/

And then, after modifying the path in the `llama_example.py` you can do : 

```bash
$> .venv/bin/python<version> llama_example.py
```
