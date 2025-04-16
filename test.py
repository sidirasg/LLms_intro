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