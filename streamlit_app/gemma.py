from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load and cache the model/tokenizer only once
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-1.1-2b-it")
    model = AutoModelForCausalLM.from_pretrained(
        "google/gemma-1.1-2b-it",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    return tokenizer, model

# Generate output based on user input
def get_response(prompt: str, tokenizer, model):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=300,              # Reduced for speed
        do_sample=False,                 # Greedy decoding (faster, more predictable)
        top_p=0.9,
        top_k=50,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response.replace(prompt.strip(), "").strip()