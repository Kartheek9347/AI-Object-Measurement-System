from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2

from modules.object_detector import detect_objects
from modules.measurement_engine import estimate_size

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["image"]
        filename = secure_filename(file.filename)

        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        detections = detect_objects(filepath)

        result_img, measurements = estimate_size(filepath, detections)

        result_path = os.path.join(RESULT_FOLDER, filename)
        cv2.imwrite(result_path, result_img)

        return render_template(
            "result.html",
            image=result_path,
            measurements=measurements
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)