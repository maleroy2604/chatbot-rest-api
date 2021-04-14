from flask import Flask, jsonify, request
from tensorflow import keras
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import tensorflow as tf 
from chatgui import chatbot_model

app  = Flask(__name__)
messages =['aaaaa','bbbbb']

@app.route('/message', methods=['POST '])
def create_store():
    pass

@app.route('/getMessages/<string:msg>')
def get_messages(msg):
    chatbot = chatbot_model()
    return jsonify({'messages' : chatbot.chatting(msg)})
    


app.run(port=5000)

