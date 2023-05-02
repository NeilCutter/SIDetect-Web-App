from webapp import app, render_template, request, session
from webapp import preprocess_text
from webapp import gpt3
from webapp import file_handling as flh


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/detection")
def detection_page():
    return render_template("detection.html")

@app.route("/hotlines")
def hotline_page():
    return render_template("hotline.html")

@app.route("/team")
def team_page():
    return render_template("team.html")


@app.route("/detection", methods=["POST"])
def detect():
    tf_idf = flh.load_model("./models/tokenizer.pkl")
    rf_model = flh.load_model("./models/ml_model.pkl")
    raw_text = request.form["text"]
    text = flh.load_file("./prompts/prompt.txt").replace("<<BLOCK>>", raw_text)
    text = gpt3.text_process(text)

    new_text = preprocess_text.clean_text(text)
    vec = tf_idf.transform([new_text])
    ml_pred = rf_model.predict(vec)

    if ml_pred[0] == 0:
        session["sample"] = f"{raw_text} : No Suicidal Tendencies"
    else:
        session["sample"] = f"{raw_text} : Has Suicidal Tendencies"

    if ml_pred[0] == 1:
        new_textblock = flh.load_file("./prompts/prompt2.txt").replace("<<BLOCK>>", raw_text)
    else:
        new_textblock = flh.load_file("./prompts/promp3.txt").replace("<<BLOCK>>", raw_text)
    session["anlys"] = gpt3.context(new_textblock)

    return render_template("detection.html", sample=session["sample"], anlys=session["anlys"])


@app.route("/chatbot")
def chatbot_page():
    return render_template("chatbot.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    text_block = request.form["chat"]
    prompt = flh.load_file("./prompts/prompt4.txt").replace("<<BLOCK>>", text_block) + "\n"
    session["chat"] = gpt3.chat(prompt)
    return render_template("chatbot.html", input=session["chat"])
