from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    buildings = {
        'farm': {'min': 10, 'max': 20},
        'cave': {'min': 5, 'max': 10},
        'house': {'min': 2, 'max': 5},
        'casino': {'min': -50, 'max': 50}
    }
    
    building = request.form['building']
    earnings = random.randint(buildings[building]['min'], buildings[building]['max'])
    
    if building == 'casino':
        earnings *= random.choice([-1, 1]) 
    
    session['gold'] += earnings
    session['activities'].append({'color': 'green' if earnings >= 0 else 'red', 'message': f'Earned {earnings} gold from the {building}!'})
    
    return redirect('/')


@app.route('/reset')
def reset():
    session['gold'] = 0
    session['activities'] = []
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
