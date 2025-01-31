## AI Camera with Hand Gestures

This project is a Flask-based application designed to interact with mathematical problems through hand gestures. Using a webcam, the application captures video, detects specific hand gestures, and allows users to draw mathematical expressions on a virtual canvas. The drawn expressions are processed by a Generative AI model, which interprets and solves the mathematical problems, providing step-by-step solutions. The results are displayed dynamically on a user-friendly frontend.

---

## Features

- Real-time webcam feed with hand gesture detection using `cvzone` and `mediapipe`.
- Hand-drawn input canvas that interacts with a Generative AI model.
- Real-time AI response displayed dynamically on the frontend.
- Responsive UI built with Bootstrap for clean design and usability.

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

1. Python 3.7 or newer
2. pip (Python package manager)
3. A webcam for video capture

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate      # On Linux/Mac
   env\Scripts\activate         # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the project root with the following content:
     ```
     GENAI_API_KEY=your_openai_api_key
     ```
   - Replace `your_openai_api_key` with your actual API key for the Generative AI model.

5. **Run the Application**
   ```bash
   python app.py
   ```
   - The application will be available at `http://127.0.0.1:5000`.

---

## Usage

1. Open the app in your browser (`http://127.0.0.1:5000`).
2. The camera feed will be displayed in real-time.
3. Use the following gestures to interact:
   - **Draw Gesture**: Use your index finger to draw on the canvas.
   - **Clear Canvas**: Use your thumb gesture to clear the canvas.
   - **Trigger AI**: Use a specific gesture (e.g., `[1, 1, 1, 0, 1]`) to send the canvas to the AI.

4. The AI response will appear in the "AI Answer" section in the frontend.


## Technologies Used

- **Backend**: Flask, Flask-SocketIO
- **Frontend**: HTML, CSS 
- **Hand Detection**: cvzone, mediapipe
- **AI Model**: Generative AI (e.g., OpenAI, Google Generative AI)
- **Python Libraries**: numpy, opencv-python, Pillow, dotenv

---

## Contribution

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Nonqs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

