from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    file = request.files['dataset']
    file.save('Housing Price data set.csv')  # Save the uploaded dataset file

    # Execute the Python script and capture the output
    output = subprocess.check_output(['python', 'house_price_prediction.py'])

    return output

if __name__ == '__main__':
    app.run(debug=True)
