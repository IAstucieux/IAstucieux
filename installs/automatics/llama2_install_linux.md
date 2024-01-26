# Script to install Llama2 on Linux

## Instructions 

Run this command to install all of the prerequisites:
```bash
$> sh prerequisites.sh
```

Then execute this script with the version you want, in this case "3.9".
```bash
$> python3 install_llama.py <version>
```
If you have a problem finding the corresponding version of your python, when the env is setup, look in `.venv/bin` and choose your version.

Then the script tells you to download a model here : 
> https://ai.meta.com/llama/

After modifying the relative path in the `llama_example.py` you can do : 

```bash
$> .venv/bin/python<version> llama_example.py
```
