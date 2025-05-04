from flask import Flask, render_template, request, redirect, url_for
import subprocess
from datetime import datetime, timedelta
import time
import webbrowser
import threading
import os
import json


# List of Knowby IDs from imported Knowbys and put them into a list. 
# Iterate over the list in a seperate function that retieves the length of that dataframe (in the case of views or completions)
# That length can be used for the number of views or completions, can be seperated our later for date based ranges.












app = Flask(__name__)

# Path to your JSON config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "knowby", "config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(new_config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(new_config, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    config = load_config()  # Always load latest config

    last_sync_str = config.get("last_sync", "Never")
    sync_color = "gray"

    if last_sync_str and last_sync_str != "Never":
        try:
            last_sync_time = datetime.strptime(last_sync_str, "%d %b, %y %H:%M")
            time_diff = datetime.now() - last_sync_time

            if time_diff > timedelta(hours=24):
                sync_color = "red"
            elif time_diff > timedelta(hours=1):
                sync_color = "yellow"
            else:
                sync_color = "green"
        except ValueError:
            sync_color = "gray"

    if request.method == "POST":
        if request.form.get("action") == "connect":
            try:
                subprocess.run(["python", "knowby/login.py"], check=True)
                time.sleep(2)
                subprocess.run(["python", "knowby/scraper.py"], check=True)

                # Save current time as last sync
                now = datetime.now().strftime("%d %b, %y %H:%M")
                config["last_sync"] = now
                save_config(config)

                return render_template(
                    "index.html",
                    status="✅ Connected and data extracted successfully!",
                    theme=config["theme"],
                    last_sync=now,
                    sync_color="green"
                )
            except Exception as e:
                return render_template(
                    "index.html",
                    status=f"⛔ Error: {str(e)}",
                    theme=config["theme"],
                    last_sync=last_sync_str,
                    sync_color=sync_color
                )

        elif request.form.get("action") == "shutdown":
            return "✅ Shutting down... You can close this tab."

        elif request.form.get("action") == "set_theme":
            new_theme = request.form.get("themeSelector")
            config["theme"] = new_theme
            save_config(config)
            return redirect(url_for('index'))

    return render_template(
        "index.html",
        status=None,
        theme=config["theme"],
        last_sync=last_sync_str,
        sync_color=sync_color
    )

@app.route("/page2")
def page2():
    config = load_config()
    return render_template("page2_test.html", theme=config["theme"])

if __name__ == "__main__":
    threading.Timer(1.5, lambda: webbrowser.open("http://localhost:5000")).start()
    app.run(debug=True, use_reloader=False)


