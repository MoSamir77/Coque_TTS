#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install Flask gtts


# In[2]:


import nest_asyncio
from flask import Flask, request, send_file
from gtts import gTTS
import os
from threading import Thread

# Apply the patch to allow nested event loops
nest_asyncio.apply()

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.json
    if 'text' not in data:
        return {"error": "No text provided"}, 400
    
    text = data['text']
    
    # Convert text to speech
    tts = gTTS(text)
    
    # Save the audio file
    audio_file = "output.mp3"
    tts.save(audio_file)
    
    # Return the audio file
    return send_file(audio_file, as_attachment=True)

def run_app():
    app.run(port=5000)

# Run the Flask app in a separate thread
thread = Thread(target=run_app)
thread.start()


# In[15]:


import requests
import os

print("Current working directory:", os.getcwd())

# API endpoint
url = "http://127.0.0.1:5000/convert"

# payload
payload = {
    "text": " Hello, I am a TTS system and i can convert text to natural voice how can i help? "
}

# Send a POST request
response = requests.post(url, json=payload)

# Save response as mp3 
with open("output.mp3", "wb") as file:
    file.write(response.content)

print("Audio file saved as output.mp3")


# In[16]:


from IPython.display import Audio
Audio("output.mp3")


# In[17]:


python --version 


# In[18]:


import sys
print(sys.version)


# In[19]:


import sys
print(sys.version_info)


# In[ ]:




