from llama_cpp import Llama
from database import db_config_

# Load DB credentials
user, password, host, port, dbname = db_config_()

# Load the model but first you have to download
llm = Llama(model_path="C:/LLMS_DEV/Model/Meta-Llama-3-8B-Instruct.Q2_K.gguf", n_ctx=2048)

# Query the model
response = llm("Q: What is the capital of France?\nA:", max_tokens=100)

print(response["choices"][0]["text"].strip())

 # this is the Embendings
llm2 = Llama(
    model_path="C:/LLMS_DEV/Model/Meta-Llama-3-8B-Instruct.Q2_K.gguf",
    embedding=True  # 👈 Important!
)

text = "Air quality is important for health."
embedding = llm2.embed(text)

print(f"Embedding length: {len(embedding)}")
print(embedding[:10])  # Preview first 10 dimensions


with open("C:/DEV/Zenith_ETL/Pefect/model.py", "r", encoding="utf-8") as file:
    model_code = file.read()

prompt = (
    "This is a Python machine learning model script:\n\n"
    f"{model_code[:3000]}\n\n"  # 👈 limit if LLaMA context is small
    "Please explain:\n"
    "1. What this model is doing.\n"
    "2. What are the input variables.\n"
    "3. What kind of output it produces.\n"
    "4. What each variable and step means in simple terms.\n"
)


from llama_cpp import Llama

llm3 = Llama(
    model_path="C:/LLMS_DEV/Model/Meta-Llama-3-8B-Instruct.Q2_K.gguf",  # your downloaded model
    n_ctx=2048
)

response = llm3(
    prompt,
    max_tokens=512,
    temperature=0.7,
)

print(response["choices"][0]["text"].strip())