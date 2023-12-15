# Documentation

## Introduction 

We have some functions in our library, so here's our documentation 

## Text functions

### askLlama
Function that returns the answer of the given prompt of the given language model with the given max_token
```py
def askLlama(prompt, llama_model_path, max_token)
```
- prompt : string of the prompt, exemple :
  > What is the capital of France ?
- llama_model_path : string of the path to the model, example :
  > ./models/model.gguf
  
  By default if not given, will take the first found ".gguf"
- max_token : maximum number of token the language model can return, example :
  > 256

  By default if not given : `64`

## Image functions

### askStableDiffusion
Function that returns a path of an image in the given folder based on a given prompt.
```py
def askStableDiffusion(prompt, outpout_path)
```
- prompt : string of the prompt, example :
  > A realistic picture, small light chestnut shiba, walking towards the camera, a stick in his mouth, on green grass, blue sky, some clouds
  
- outpout_path : string of the folder path where the image will end up, example :
  > ./my_images/dog_images/

  By default if not given : `./images`

### generateRandomImg
Function that returns the path of a random image, uses llama to generate a nice prompt.
```py
def generateRandomImg(llama_model_path, outpout_path)
```
- llama_model_path : string of the path to the model, example :
  > ./models/model.gguf
  
- outpout_path : string of the folder path where the image will end up, example :
  > ./my_images/dog_images/

  By default if not given : `./images`

### generateDogImg
Function that returns the path of a random dog based image, uses llama to generate a nice prompt.
```py
def generateRandomImg(llama_model_path, outpout_path)
```
- llama_model_path : string of the path to the model, example :
  > ./models/model.gguf
  
- outpout_path : string of the folder path where the image will end up, example :
  > ./my_images/dog_images/

  By default if not given : `./images`

### askPrettierStableDiffusion
Function that returns the path of an image, and before modify the prompt using llama to make it better.
You can just call it with a bad prompt like : 
> Dog
And it will make the prompt a little better before generating the image.
```py
def generateRandomImg(basic_prompt, llama_model_path, outpout_path)
```
- basic_prompt : string of the prompt, example :
  > Dog

- llama_model_path : string of the path to the model, example :
  > ./models/model.gguf
  
- outpout_path : string of the folder path where the image will end up, example :
  > ./my_images/dog_images/

  By default if not given : `./images`
