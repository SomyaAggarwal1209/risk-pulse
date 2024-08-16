from flask import Blueprint, request, jsonify
import google.generativeai as genai

g_api_bp = Blueprint('g_api', __name__)

# Configure the Gemini API key
genai.configure(api_key="AIzaSyA3MzKibpGjCn3VCUvE3oo4-ZRtB9H9I4M")

@g_api_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)

    reply = response.candidates[0].content.parts[0].text

    return jsonify({'response': reply})

@g_api_bp.route('/api/upload', methods=['POST'])
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
