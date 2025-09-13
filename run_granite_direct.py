import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed

model_path = "ibm-granite/granite-3.3-2b-instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map=device,
    torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

conv = [{"role": "user", "content": "Explain Newton's three laws of motion in simple words."}]

input_ids = tokenizer.apply_chat_template(
    conv,
    return_tensors="pt",
    thinking=True,
    return_dict=True,
    add_generation_prompt=True
).to(device)

set_seed(42)
output = model.generate(
    **input_ids,
    max_new_tokens=256,
)

prediction = tokenizer.decode(output[0, input_ids["input_ids"].shape[1]:], skip_special_tokens=True)
print("\n=== Prediction ===\n", prediction)
