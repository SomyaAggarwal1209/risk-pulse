from flask import Blueprint, request, jsonify
import openai

api_bp = Blueprint('api', __name__)

# Set up OpenAI API key
openai.api_key = 'sk-proj-JheSLxyaqvzF0vCAspJDT3BlbkFJpVfdLKJsDP3ICBRHFdvd'


@api_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    reply = response.choices[0].message['content'].strip()

    return jsonify({'response': reply})


@api_bp.route('/api/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'response': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'response': 'No selected file'})

    # You can save the file and process it if needed
    # filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # For simplicity, just echoing back the filename
    return jsonify({'response': f'File {file.filename} uploaded successfully'})
