import torch
from transformers import pipeline, set_seed

prompt = "Explain Newton's three laws of motion in simple words."

device = 0 if torch.cuda.is_available() else -1
dtype  = torch.bfloat16 if torch.cuda.is_available() else torch.float32

generator = pipeline(
    "text-generation",
    model="ibm-granite/granite-3.3-2b-instruct",
    tokenizer="ibm-granite/granite-3.3-2b-instruct",
    device=device,
    torch_dtype=dtype,
    trust_remote_code=True
)

set_seed(42)
out = generator(prompt, max_new_tokens=256, temperature=0.2)
print("\n=== Prediction ===\n", out[0]["generated_text"])
