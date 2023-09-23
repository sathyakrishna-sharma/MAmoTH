import requests
import transformers

API_TOKEN = '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'

API_URL = "https://api-inference.huggingface.co/models/TIGER-Lab/MAmmoTH-Coder-7B"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, json=payload)
	return response.json()

output = query({
	"inputs": " what is 2+2 ",})

print(output)