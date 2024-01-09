from llama_cpp import Llama
from tcppinglib import tcpping
import os
import requests
import io
import base64
from PIL import Image


class ia_stucieux:
    def __init__(self, ip="127.0.0.1", port=7860, img_path="./img/"):
        self.max_token = 1024
        self.path_model_lama = ""
        self.ip_automatic = ip
        self.port_automatic = port
        self.img_path = img_path
        self.model_exist()
        self.init_img_folder()
        self.llama = Llama(self.path_model_lama)

    ###############################
    #          setter             #
    ###############################
    def set_max_token(self, max_token):
        self.max_token = max_token

    def set_path_model_lama(self, path_model_lama):
        self.path_model_lama = path_model_lama

    def set_ip_automatic(self, ip_automatic):
        self.ip_automatic = ip_automatic

    def set_port_automatic(self, port_automatic):
        self.port_automatic = port_automatic

    def set_img_path(self, img_path):
        self.img_path = img_path

    ###############################
    #          getter             #
    ###############################
    def get_max_token(self):
        return self.max_token

    def get_path_model_lama(self):
        return self.path_model_lama

    def get_ip_automatic(self):
        return self.ip_automatic

    def get_port_automatic(self):
        return self.port_automatic

    def get_img_path(self):
        return self.img_path

    ###############################
    #  Test init functions        #
    ###############################
    def ping_automatic(self):
        host = tcpping(self.ip_automatic, self.port_automatic, count=2)
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
        self.path_model_lama = './models/' + listdir[0]

    def init_img_folder(self):
        if not os.path.exists('./img'):
            os.makedirs('./img')

    ###############################
    #  Llama model interrogation  #
    ###############################
    def askLlama(self, prompt):
        output = self.llama(prompt, max_tokens=self.max_token)
        return output["choices"][0]["text"]

    def generateRandomImg(self, outpout_path):
        prompt = "Generate only a random prompt description for a ai image generator"
        output = self.llama(prompt, max_tokens=self.max_token)
        img = output["choices"][0]["text"]
        self.generateImg(img)

    def generateImg(self, prompt):
        # Effectuer la requête HTTP pour convertir le résultat en image
        url = f"http://{self.ip_automatic}:{self.port_automatic}"
        payload = {
            "prompt": prompt,
            "steps": 5
        }
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
        r = response.json()
        image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
        image.save(f'{self.img_path}/output.png')

    def generate_story(self, theme=None):
        prompt = "Generate a story in few lines" + (f" with the theme is : {theme}" if theme is not None else "")
        output = self.llama(prompt, max_tokens=self.max_token)
        story = output["choices"][0]["text"]
        print("story : " + story)
        prompt = f"With this story : {story}, generate a description image to illustrate it"
        print("prompt : " + prompt)
        self.generateImg(prompt)
        return story


if __name__ == '__main__':
    print("This is a module, not a script")
    ia = ia_stucieux()
    ia.generate_story("love")