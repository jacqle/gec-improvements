from .gector import model
import re

model = model.load_model(
    vocab_path = "src/gector/data/output_vocabulary",
    model_paths = ["src/gector/data/model_files/xlnet_0_gector.th"],
    model_name = "xlnet"
)
