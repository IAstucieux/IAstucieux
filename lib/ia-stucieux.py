from llama_cpp import Llama
from tcppinglib import tcpping
import os
import requests
import io
import base64
from PIL import Image
from datetime import datetime


class ia_stucieux:
    def __init__(self, ip="127.0.0.1", port=7860, img_path="./img/"):
        self._max_token = 1024
        self._path_model_lama = ""
        self._ip_automatic = ip
        self._port_automatic = port
        self._img_path = img_path
        self.model_exist()
        self.init_img_folder()
        self.llama = Llama(self._path_model_lama)

    ###############################
    #          setter             #
    ###############################
    def set_max_token(self, max_token):
        self._max_token = max_token

    def set_path_model_lama(self, path_model_lama):
        self._path_model_lama = path_model_lama

    def set_ip_automatic(self, ip_automatic):
        self._ip_automatic = ip_automatic

    def set_port_automatic(self, port_automatic):
        self._port_automatic = port_automatic

    def set_img_path(self, img_path):
        self._img_path = img_path
        self.init_img_folder()

    ###############################
    #          getter             #
    ###############################
    def get_max_token(self):
        return self._max_token

    def get_path_model_lama(self):
        return self._path_model_lama

    def get_ip_automatic(self):
        return self._ip_automatic

    def get_port_automatic(self):
        return self._port_automatic

    def get_img_path(self):
        return self._img_path

    ###############################
    #  Test init functions        #
    ###############################
    def ping_automatic(self):
        host = tcpping(self._ip_automatic, self._port_automatic, count=2)
        if host.is_alive:
            print("automatic 1111 api is running")
        else:
            print("error automatic 1111 api is not running")
            exit(1)

    def model_exist(self):
        listdir = os.listdir('./models/')
        if '.gitkeep' in listdir:
            listdir.remove('.gitkeep')
        if listdir == []:
            print("No model found in ./models/")
            exit(1)
        self._path_model_lama = './models/' + listdir[0]

    def init_img_folder(self):
        if not os.path.exists(self._img_path):
            os.makedirs(self._img_path)

    ###############################
    #  Llama model interrogation  #
    ###############################
    def askLlama(self, prompt):
        output = self.llama(prompt, max_tokens=self._max_token)
        return output["choices"][0]["text"]

    def generateRandomImg(self, img_name="output"):
        self.ping_automatic()
        prompt = "Generate only a random prompt description for a ai image generator"
        output = self.llama(prompt, max_tokens=self._max_token)
        img = output["choices"][0]["text"]
        self.generateImg(img, img_name)

    def generateImg(self, prompt, img_name="output"):
        self.ping_automatic()
        # Effectuer la requête HTTP pour convertir le résultat en image
        url = f"http://{self._ip_automatic}:{self._port_automatic}"
        payload = {
            "prompt": prompt,
            "steps": 5
        }
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
        r = response.json()
        image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))

        image.save(f'{self._img_path}/{img_name +"-"+ str(datetime.now().strftime("%Y%m%d%H%M%S"))}.png')

    def generate_story(self, theme=None, img_name="output"):
        self.ping_automatic()
        prompt = "Generate a story in few lines" + (f" where the theme is : {theme}" if theme is not None else "")
        output = self.llama(prompt, max_tokens=self._max_token)
        story = output["choices"][0]["text"]
        prompt = f"With this story : {story}, generate a description image to illustrate it"
        self.generateImg(prompt, img_name)
        return story
