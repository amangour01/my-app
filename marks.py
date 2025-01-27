import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student marks from CSV
df = pd.read_csv('students.csv')

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    
    # Find marks for requested names
    marks = df[df['name'].isin(names)]['marks'].tolist()
    
    return jsonify({"marks": marks})

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
