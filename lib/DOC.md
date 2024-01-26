# Documentation

## Introduction 

This documentation presents the available functions in our library.

The lib allows you to assign a style, like `Cartoon` or `Anime` for example, to an image you are generating. These are stored in [style.json](style.json).
You can also add new styles.

## Text functions

### askLlama
Function that asks Llama a question and returns the generated response
```py
def askLlama(prompt)
```
- prompt : string of the prompt, exemple :
  > What is the capital of France ?

## Image functions

### generateRandomImg
Function that generates a random image. It uses llama to generate a prompt and automatic1111 to create an image based on it. 
```py
def generateRandomImg(img_name, style)
```
- img_name : string of the file name that will be used. The image_name is unique beacuse it uses this date format dd-mm-yyyy hh-mm-ss, example :
  > output.png

  By default if not given : `output`

- style : string of the style to use, example :
  > Cartoon

  By default if not given : `None`

### generateImg
Function that generates an image of the given prompt.
```py
def generateImg(prompt, img_name, style)
```
- prompt : string of the prompt, example :
  > A realistic picture, small light chestnut shiba, walking towards the camera, a stick in his mouth, on green grass, blue sky, some clouds
  
- img_name : string of the file name that will be used. The image_name is unique beacuse it uses this date format dd-mm-yyyy hh-mm-ss, example :
  > ./output.png

  By default if not given : `output`

- style : string of the style to use, example :
  > Cartoon

  By default if not given : `Neutral_background`

### generateStory
Function that generates a random story with a given theme. It uses llama to generate a story and automatic1111 to create an image based on it.
```py
def generateStory(theme, img_name, style)
```

- theme : string of the theme used to generate the story, example :
  > a dog eating

  By default if not given : `None`

- img_name : string of the file name that will be used. The image_name is unique beacuse it uses this date format dd-mm-yyyy hh-mm-ss, example :
  > output.png

  By default if not given : `output`

- style : string of the style to use, example :
  > Cartoon

  By default if not given : `None`