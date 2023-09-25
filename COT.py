import transformers
from transformers import pipeline

math_pipeline = pipeline("text-generation", "TIGER-Lab/MAmmoTH-Coder-7B", device = 0, max_length = 200, temperature = 0)
