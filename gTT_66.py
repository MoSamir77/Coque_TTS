#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, send_file
from gtts import gTTS
import os

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

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000)


# In[ ]:




