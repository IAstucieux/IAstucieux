# Llama2 Installation on Mac
## Requirements 
1. Install homebrew: 
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install python 3.9.2
```bash
brew install python@3.9.2
```

3. Install md5sha1sum
This is a tool that allows you to check the integrity of the downloaded files.
```bash
brew install md5sha1sum
```

4. Create a directory for Llama2
```bash
mkdir ~/llama2; cd ~/llama2;
```

## Installation
1. Clone the Llama2 repository and the Llama2.cpp repository
```bash
git clone git@github.com:facebookresearch/llama.git
git clone git@github.com:ggerganov/llama.cpp.git
```

2. Use Meta's URL (retrieved from their website) to download the latest version of the Llama2 dataset
Choose the appropiate model for your system, in this case 7b-chat.

3. Create a Conda environment for Llama2.cpp
```bash
conda create --name llama2
conda activate llama2
```

4. Install pip
```bash
conda install pip
```

5. Install the requirements for Llama2
```bash
python3 -m pip install -r requirements.txt
python3 convert.py --outfile models/7B/ggml-model-f16.bin --outtype f16 ../../llama2/meta_models/llama-2-7b-chat
./quantize  ./models/7B/ggml-model-f16.bin ./models/7B/ggml-model-q4_0.bin q4_0
```

6. Launch Llama2
```bash
./main -m ./models/7B/ggml-model-q4_0.bin -n 1024 --repeat_penalty 1.0 --color -i -r "User:" -f ./prompts/chat-with-bob.txt
```

Congratulations, you have successfully installed Llama2 on your Mac!