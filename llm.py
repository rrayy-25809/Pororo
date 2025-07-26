from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class Model:

    def __init__(self) -> None:
        pass

    def load_file(self, file):
        self.file = file
        self.tokenizer = AutoTokenizer.from_pretrained("./pororo_model")
        self.model = AutoModelForCausalLM.from_pretrained("./pororo_model")

    def ask(self, q):
        return self.model.generate(
            input_ids=torch.tensor([self.tokenizer.encode(q)]),
            max_length=512,
            num_return_sequences=1,
            do_sample=True,
            top_p=0.95,
            top_k=50
        )[0]