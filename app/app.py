import os
import time
import json

from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

# Mock vulnerable login logic (same as before)
USER_DB = {"admin": "password123"}

@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Vulnerable logic - (No rate limiting, weak password checking)
    if username in USER_DB and USER_DB[username] == password:
        return jsonify({"message": "Login successful", "success": True}), 200
    else:
        return jsonify({"message": "Invalid credentials", "success": False}), 401


def simulate_attack():
    password_file = "../pass_strings.txt"
    username = "admin"
    if not os.path.exists(password_file):
        yield "data: " + json.dumps({"message": "Password file not found!"}) + "\n\n"
        return

    with open(password_file, "r") as file:
        passwords = [line.strip() for line in file]

    for password in passwords:
        time.sleep(0.5)  # Simulate delay for realism
        if username in USER_DB and USER_DB[username] == password:
            yield "data: " + json.dumps({
                "username": username,
                "password": password,
                "message": f"[SUCCESS] Username: {username}, Password: {password}"
            }) + "\n\n"
            return
        else:
            yield "data: " + json.dumps({
                "username": username,
                "password": password,
                "message": f"[FAILED] Username: {username}, Password: {password}"
            }) + "\n\n"

    yield "data: " + json.dumps({"message": "No valid password found."}) + "\n\n"


@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)


@app.route("/start_attack", methods=["GET"])
def start_attack():
    return Response(simulate_attack(), content_type="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True)