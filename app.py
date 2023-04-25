from flask import Flask, render_template, request, session
import preprocess_text
import gpt3
import pickle

app = Flask(__name__)
app.secret_key="keep it secret, keep it safe"


def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        return infile.read()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/detection', methods=['GET'])
def detection_page():
    return render_template('detection.html')

@app.route('/team', methods=['GET'])
def team_page():
    return render_template('team.html')

@app.route('/detection', methods=['POST'])
def detect():
    # try:
    tf_idf = pickle.load(open('./Models/tokenizer.pkl', 'rb'))
    rf_model = pickle.load(open('./Models/ml_model.pkl', 'rb'))

    raw_text = request.form["text"]
    text = open_file("prompts/prompt.txt").replace("<<BLOCK>>", raw_text)
    text = gpt3.translate(text)

    new_text = preprocess_text.clean_text(text)
    vec = tf_idf.transform([new_text])
    ml_pred = rf_model.predict(vec)

    if ml_pred[0] == 0:
        session["sample"] = ("{} : {}".format(raw_text, "No Suicidal Tendencies"))
    else:
        session["sample"] = ("{} : {}".format(raw_text, "Has Suicidal Tendencies"))
        
    if ml_pred[0] == 1:
        new_textblock = open_file("prompts/prompt2.txt").replace("<<BLOCK>>", raw_text)
        session["anlys"] = gpt3.context(new_textblock)
    else:
        new_textblock = open_file("prompts/promp3.txt").replace("<<BLOCK>>", raw_text)
        session["anlys"] = gpt3.context(new_textblock)
        
    print("{} : {}".format(new_text, ml_pred))

    return render_template('detection.html',  sample = session["sample"], anlys = session["anlys"])
  
@app.route('/chatbot', methods= ['GET'])
def chatbot_page():
    return render_template("chatbot.html")

@app.route('/chatbot', methods=['POST'])
def chatbot():
    text_block = request.form['chat']
    prompt = open_file("prompts/prompt4.txt").replace("<<BLOCK>>", text_block)
    prompt = prompt + "\n"
    session['chat']= gpt3.chat(prompt)
    return render_template('chatbot.html', input = session['chat'])


if __name__ == '__main__':
    app.run(debug=True)
