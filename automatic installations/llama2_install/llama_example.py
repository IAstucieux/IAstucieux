from llama_cpp import Llama

# Change the path / name of the model if needed
model_path_str="./model.gguf"

# load the large language model file

LLM = Llama(model_path=model_path_str)

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
