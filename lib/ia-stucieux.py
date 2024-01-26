from llama_cpp import Llama
from tcppinglib import tcpping
import json
import os
import requests
import io
import base64
from PIL import Image
from datetime import datetime


class ia_stucieux:
    def __init__(self, ip="127.0.0.1", port=7860, img_path="./img/"):
        self._max_token = 1024
        self.jsonPath = "./style.json"
        self._path_model_lama = ""
        self._ip_automatic = ip
        self._port_automatic = port
        self._img_path = img_path
        self._negative_prompt = "(deformed iris, deformed pupils), text, worst quality, low quality,jpeg artifacts, ugly, duplicate, morbid, mutilated, (extra fingers), (mutated hands), poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, (fused fingers), (too many fingers), long neck, camera, name, signature, watermark, logo, autograph, trademark, cut off, censored, bad anatomy, bad body, bad face, bad teeth, deformities, (boring, uninteresting:1.1)"
        self.modelExist()
        self.initImgFolder()
        self.llama = Llama(self._path_model_lama)
        self.styles = self.getJsonStyle()

    ###############################
    #          setter             #
    ###############################
    def setMaxToken(self, max_token):
        """
        Set the maximum token value.

        Parameters:
            max_token (int): The maximum token value to be set.

        Returns:
            None
        """
        self._max_token = max_token

    def setPathModelLama(self, path_model_lama):
        """
        Set the path to the model for Lama.

        Parameters:
            path_model_lama (str): The path to the model for Lama.

        Returns:
            None
        """
        self._path_model_lama = path_model_lama

    def setIpAutomatic(self, ip_automatic):
        """
        Set the value of the ip of automatic1111.

        Parameters:
            ip_automatic (str): The new value for the 'ip_automatic' attribute.

        Returns:
            None
        """
        self._ip_automatic = ip_automatic

    def setPortAutomatic(self, port_automatic):
        """
        Set the value of the port of automatic1111.

        Parameters:
            port_automatic (int): The new value for the port_automatic attribute.

        Returns:
            None
        """
        self._port_automatic = port_automatic

    def setImgPath(self, img_path):
        """
        Set the image path and create the folder.

        Parameters:
            img_path (str): The path to the image.

        Returns:
            None
        """
        self._img_path = img_path
        self.initImgFolder()

    def setNegativePrompt(self, negative_prompt):
        """
        Sets the negative prompt for the AI.

        Parameters:
        negative_prompt (str): The negative prompt to be set.

        Returns:
        None
        """
        self._negative_prompt = negative_prompt

    def addStyle(self, style, theme):
        """
        Adds a style and its corresponding theme to the styles dictionary.

        Parameters:
            style (str): The name of the style.
            theme (str): The corresponding theme for the style.

        Returns:
            None
        """
        self.styles[style] = theme
        with open(self.jsonPath, "w") as f:
            json.dump(self.styles, f)

    ###############################
    #          getter             #
    ###############################
    def getMaxToken(self):
        """
        Returns the maximum token value.
        """
        return self._max_token

    def getPathModelLama(self):
        """
        Returns the path of the model used by the Lama algorithm.
        """
        return self._path_model_lama

    def getIpAutomatic(self):
        """
        Returns the ip of automatic1111.
        """
        return self._ip_automatic

    def getPortAutomatic(self):
        """
        Returns the port of automatic1111.
        """
        return self._port_automatic

    def getImgPath(self):
        """
        Returns the image path.
        """
        return self._img_path

    def getNegativePrompt(self):
        """
        Returns the negative prompt used to generate image.
        """
        return self._negative_prompt
    
    def getJsonStyle(self):
        """
        Returns the styles dictionary.
        """
        with open(self.jsonPath, "r") as f:
            data = json.load(f)
        return data

    ###############################
    #  Test init functions        #
    ###############################
    def pingAutomatic(self):
        """
        Ping the automatic 1111 API to check if it is running.

        Parameters:
        None

        Returns:
        None
        """
        host = tcpping(self._ip_automatic, self._port_automatic, count=2)
        if host.is_alive:
            print("automatic 1111 api is running")
        else:
            print("error automatic 1111 api is not running")
            exit(1)

    def modelExist(self):
        """
        Check if there is at least one model in the './models/' directory.
        If no model is found, print an error message and exit the program.
        If a model is found, set the path to the model.

        Parameters:
        None

        Returns:
        None
        """
        listdir = os.listdir('./models/')
        if '.gitkeep' in listdir:
            listdir.remove('.gitkeep')
        if listdir == []:
            print("No model found in ./models/")
            exit(1)
        self._path_model_lama = './models/' + listdir[0]

    def initImgFolder(self):
        """
        Initializes the image folder if it doesn't exist.

        Parameters:
        None

        Returns:
        None
        """
        if not os.path.exists(self._img_path):
            os.makedirs(self._img_path)

    ###############################
    #  Llama model interrogation  #
    ###############################
    def askLlama(self, prompt):
        """
        Asks Llama a question and returns the generated response.

        Parameters:
            prompt (str): The question or prompt to ask the Llama model.

        Returns:
            str: The generated response from the Llama model.
        """
        output = self.llama(prompt, max_tokens=self._max_token)

        return output["choices"][0]["text"]

    def generateRandomImg(self, img_name="output", style=None):
        """
        Generates a random prompt description for automatic1111 and generates the corresponding image.

        Parameters:
            img_name (str, optional): The name of the output image file. Defaults to "output".
            style (str, optional): The style of the generated image. Defaults to "".

        Returns:
            str: The generated prompt description.
        """
        self.pingAutomatic()
        prompt = "Generate only a random prompt description for a ai image generator"
        output = self.llama(prompt, max_tokens=self._max_token)
        promptImg = output["choices"][0]["text"]
        self.generateImg(promptImg, img_name, style)

        return promptImg

    def generateImg(self, prompt, img_name="output", style="Neutral_background"):
        """
        Generates an image based on the given prompt using the specified style.

        Parameters:
            prompt (str): The text prompt for generating the image.
            img_name (str, optional): The name of the output image file. Defaults to "output".
            style (str, optional): The style to be applied to the image. Defaults to "Neutral_background".

        Returns:
            None
        """
        self.pingAutomatic()
        # Effectuer la requête HTTP pour convertir le résultat en image
        url = f"http://{self._ip_automatic}:{self._port_automatic}"
        prompt += f" with this style : {self.styles[style]}"
        payload = {
            "prompt": prompt,
            "steps": 7,
            "negative_prompt": self._negative_prompt
        }
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
        r = response.json()
        image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))

        image.save(f'{self._img_path}/{img_name + "-" + str(datetime.now().strftime("%Y%m%d%H%M%S"))}.png')

    def generateStory(self, theme=None, img_name="output", style=None):
        """
        Generates a story in few lines based on the given theme (optional).
        It also generates a image to illustrate the story.

        Parameters:
            theme (str, optional): The theme of the story. Defaults to None.
            img_name (str, optional): The name of the output image. Defaults to "output".
            style (str, optional): The style of the output image. Defaults to "".

        Returns:
            str: The generated story.
        """
        self.pingAutomatic()
        prompt = "Generate a story in few lines" + (f" where the theme is : {theme}" if theme is not None else "")
        output = self.llama(prompt, max_tokens=self._max_token)
        story = output["choices"][0]["text"]
        prompt = f"With this story : {story}, generate a description image to illustrate it"
        self.generateImg(prompt, img_name, style)

        return story
