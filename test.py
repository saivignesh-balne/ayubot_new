import requests

url = "https://api.together.xyz/v1/chat/completions"
headers = {
    "Authorization": "Bearer 4e5ed785b761e8a31e04bcd6529761f554c27030601eb1a163bb1a0dd23487fd",
    "Content-Type": "application/json"
}
data = {
    "model": "mistralai/Mistral-7B-Instruct-v0.1",
    "messages": [
                {
                    "role": "system",
                    "content": "You are an Ayurvedic doctor. Answer briefly (2 sentences max) about:"
                              "\n- Vata/Pitta/Kapha doshas"
                              "\n- Diet recommendations"
                              "\n- Daily routines (dinacharya)"
                              "\n- Herbal remedies"
                },
                {
                    "role": "user", 
                    "content": "hey, I have a headache and feel tired. What should I do?"
                }
            ],
    "temperature": 0.7,
    "max_tokens": 150
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.json())