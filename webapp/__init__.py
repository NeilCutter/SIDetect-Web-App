from flask import Flask, render_template, request, session
import pickle
import openai

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


from webapp import routes