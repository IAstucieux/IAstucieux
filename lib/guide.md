# lib/ setup 
## Requirements

1. tcppinglib

Using pip, install tcppinglib
```bash
pip install tcppinglib
```

2. Model

Add the downloaded model to the `lib/models/` directory. This way, the model can be used by the `lib/` script ia_stucieux.py


## Usage
1. main.py

The main.py script is used to test the available functions and to test the model. Create a `main.py` file, import the available functions and run the script.

An example of a `main.py` file is given below:

```python
from ia_stucieux import ia_stucieux

if __name__ == '__main__':
    ia = ia_stucieux()
    ia.set_img_path("./test/")
    ia.generateRandomImg("Small dog in a park")
```

This script will generate a random image of a small dog in a park and save it in the `test/` directory.

2. Run the script

To run the script, use the following command, depending on the main.py location:

```bash
path/to/root/.venv/bin/python3.9 /path/to/main/main.py
```