import torch

class Model:

    def __init__(self) -> None:
        pass

    def load_file(self, file):
        file.load() # type: ignore

    def ask(self, q):
        return "This is a simulated response from your LLM."