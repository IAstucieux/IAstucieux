# lib setup 

This guide will help you setup the `lib/` directory and its dependencies.
This way, you'll be able to use the functions available in the `lib/` directory.

## Requirements

### tcppinglib

Using pip, install tcppinglib
```bash
pip install tcppinglib
```
Or 
```bash
pip[version] install tcppinglib
```

### Model

Add the downloaded model to the `lib/models/` directory. This way, the model can be used by the `lib/` script ia_stucieux.py


## Usage
### main.py

The main.py script is used to test the available functions and to test the model. Create a `main.py` file, import the available functions and run the script.

An example of a `main.py` file is given below:

```python
from ia_stucieux import ia_stucieux

if __name__ == '__main__':
    ia = ia_stucieux()
    ia.set_img_path("./test/")
    ia.generateRandomImg()
```

you can also choose your own path to the llama model like that : 
```python
ia.set_path_model_lama('../../path/to/llama/llama_model.gguf')
```

This script will generate a random image and save it in the `test/` directory.

For more information, go in the `DOC.md` in  the `lib/` folder.

### Run the script

To run the script, use the following command, depending on the main.py location:

```bash
path/to/root/.venv/bin/python3.9 /path/to/main/main.py
```
