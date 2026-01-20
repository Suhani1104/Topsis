from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import numpy as np
import os
import re
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
STATIC_FOLDER = "static"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# ---------- EMAIL CONFIG ----------
SENDER_EMAIL = "suhani.work04@gmail.com"      # CHANGE
APP_PASSWORD = "tgxu czcr bsab lpqd"   # CHANGE

# ---------- TOPSIS LOGIC ----------
def run_topsis(input_file, weights, impacts, output_file):
    df = pd.read_csv(input_file)

    data = df.iloc[:, 1:].astype(float)

    norm = data / np.sqrt((data ** 2).sum())
    weighted = norm * weights

    ideal_best, ideal_worst = [], []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    d_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = d_neg / (d_pos + d_neg)
    rank = score.rank(ascending=False, method="dense").astype(int)

    df["TOPSIS Score"] = score.round(4)
    df["Rank"] = rank

    df.to_csv(output_file, index=False)
    return df

# ---------- EMAIL ----------
def send_email(receiver, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Analysis Result"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver
    msg.set_content("Hello,\n\n"
                    "Your TOPSIS analysis has been completed successfully.\n" 
 "Please find the attached CSV file containing:\n" 
    "- TOPSIS score\n" 
    "- Final ranking based on the given criteria\n"
    "Thank you for using the TOPSIS Web Service!\n\n"
    "Regards,\n"
    "Suhani Gupta\n")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="topsis_result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download-sample")
def download_sample():
    return send_from_directory(STATIC_FOLDER, "sample.csv", as_attachment=True)

@app.route("/submit", methods=["POST"])
def submit():
    file = request.files.get("file")
    weights = request.form.get("weights", "").strip()
    impacts = request.form.get("impacts", "").strip()
    email = request.form.get("email", "").strip()

    # Email validation
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return render_template("index.html", error="Invalid email format.")

    weights_list = weights.split(",")
    impacts_list = impacts.split(",")

    if len(weights_list) != len(impacts_list):
        return render_template("index.html", error="Weights and impacts count must be equal.")

    if any(i not in ["+", "-"] for i in impacts_list):
        return render_template("index.html", error="Impacts must be '+' or '-' only.")

    try:
        weights_list = [float(w) for w in weights_list]
    except:
        return render_template("index.html", error="Weights must be numeric values.")

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(RESULT_FOLDER, "result.csv")
    file.save(input_path)

    df = pd.read_csv(input_path)
    if len(weights_list) != df.shape[1] - 1:
        return render_template(
            "index.html",
            error="Number of weights/impacts must match number of numeric columns."
        )

    result_df = run_topsis(input_path, weights_list, impacts_list, output_path)
    send_email(email, output_path)

    table_html = result_df.to_html(
        classes="result-table",
        index=False,
        border=0
    )

    return render_template(
        "index.html",
        success="Result sent to email successfully.",
        table=table_html
    )

# ---------- START ----------
#app.run(debug=True)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

