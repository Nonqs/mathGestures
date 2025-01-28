from flask import Flask, Response, jsonify, render_template
from main import getHandInfo, draw, sendToIA
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the AI API
genai.configure(api_key=os.environ.get('GENAI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize webcam and other resources
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Video width
cap.set(4, 720)   # Video height
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# Variables to hold canvas and previous positions
prev_pos = None
canvas = None

# Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main frontend page."""
    return render_template('index.html')


@app.route('/video')
def video_feed():
    """
    Stream video frames with hand detection and drawing.
    """
    def generate_frames():
        global prev_pos, canvas
        while True:
            # Capture the current frame
            success, img = cap.read()
            if not success:
                break

            img = cv2.flip(img, 1)  # Flip for a mirror effect

            # Initialize canvas if not already done
            if canvas is None:
                canvas = np.zeros_like(img)

            # Get hand info and process drawing logic
            info = getHandInfo(img)
            if info:
                fingers, lmList = info
                prev_pos, canvas = draw(info, prev_pos, canvas, img)
                sendToIA(canvas, fingers, model)

            # Combine the original image and the canvas
            combined_img = cv2.addWeighted(img, 0.7, canvas, 0.5, 0)

            # Encode the frame to send it as a response
            ret, buffer = cv2.imencode('.jpg', combined_img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/send_to_ia', methods=['POST'])
def handle_canvas():
    """
    Example endpoint for sending the canvas to the AI.
    """
    # The actual AI logic can be added here
    return jsonify({"message": "Canvas processed by AI"})


if __name__ == '__main__':
    app.run(debug=True)
