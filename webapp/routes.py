from webapp import app, render_template, request, session
from webapp import preprocess_text
from webapp import gpt3
from webapp import file_handling as flh
from webapp import openai
from webapp import re

TFIDF_MODEL_PATH = "./models/tokenizer.pkl"
RF_MODEL_PATH = "./models/ml_model.pkl"
pattern = "^[^a-zA-Z]+$"

tf_idf = flh.load_model(TFIDF_MODEL_PATH)
rf_model = flh.load_model(RF_MODEL_PATH)

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
    raw_text = request.form["text"]
    print(type(raw_text))
    if re.match(pattern, raw_text):
        print("int")
        int_identification = 0
        return render_template(
            "detection.html", output="Invalid Input", int_text=int_identification
        )

    else:
        print("string")
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
            new_textblock = flh.load_file("./prompts/prompt2.txt").replace(
                "<<BLOCK>>", raw_text
            )
        else:
            new_textblock = flh.load_file("./prompts/promp3.txt").replace(
                "<<BLOCK>>", raw_text
            )
        session["anlys"] = gpt3.context(new_textblock)

        return render_template(
            "detection.html", sample=session["sample"], anlys=session["anlys"]
        )


@app.route("/chatbot")
def chatbot_page():
    return render_template("chatbot.html")


conversation = [
    {
        "role": "system",
        "content": "You are MIKAY that only answers questions related to depression, suicide, mental illness, and has a goal to help and give advices.",
    }
]

@app.route("/get")
def completion_response():
    user_input = request.args.get("msg")
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=1,
        max_tokens=1000,
        top_p=0.9,
    )

    conversation.append(
        {"role": "assistant", "content": response["choices"][0]["message"]["content"]}
    )
    return str(response["choices"][0]["message"]["content"])
