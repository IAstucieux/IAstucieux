# Automatic 1111 installation on MacOS
## Requirements
- homebrew
- Python 3.9.2
- cmake

1. **Install homebrew:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. **Install pyenv:**
```bash
brew install pyenv
```
3. **Install Python 3.9.2:**
```bash
pyenv install 3.9.2
```
4. **Update your PATH:**
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
```

5. **Add PyEnv Init to your terminal:**
```bash
echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
```

6. **Restart your terminal:**
```bash
reset
```

## Installation

1. **Follow the instructions to install the Automatic 1111 webui:**
You can find the instructions [here](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon)

2. Run the web UI
```bash
./webui.sh
```

Congratulations! You have successfully installed the Automatic 1111 web UI on your Mac.
