"""
The flask application package.
"""

from gtts import gTTS
from flask import Flask
app = Flask(__name__)

tts = gTTS(text="Hello", lang='en')
tts.save("hello.mp3")

import web.views
