import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load student marks
with open('q-vercel-python.json', 'r') as f:
    student_marks = json.load(f)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    
    # Retrieve marks for requested names
    marks = [student_marks.get(name, None) for name in names]
    
    # Remove None values if any name not found
    marks = [mark for mark in marks if mark is not None]
    
    return jsonify({"marks": marks})

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
