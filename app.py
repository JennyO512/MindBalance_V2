from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# In-memory storage for MVP (replace with database in production)
users = {}
entries = []

@app.route('/')
def index():
    """Home page showing recent entries if logged in"""
    if 'user_id' not in session:
        return render_template('welcome.html')
    
    user_entries = [entry for entry in entries if entry.get('user_id') == session['user_id']]
    recent_entries = sorted(user_entries, key=lambda x: x['date'], reverse=True)[:5]
    return render_template('dashboard.html', entries=recent_entries)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        if not username or not password:
            flash('Username and password are required', 'error')
            return render_template('register.html')
        
        if username in users:
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        users[username] = {
            'password': password,  # In production, hash this!
            'created_at': datetime.now()
        }
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        if username in users and users[username]['password'] == password:
            session['user_id'] = username
            flash('Welcome back!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout"""
    session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    """Add a new mind balance entry"""
    if 'user_id' not in session:
        flash('Please log in to add entries', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        mood_rating = request.form.get('mood_rating')
        stress_level = request.form.get('stress_level')
        notes = request.form.get('notes', '').strip()
        activities = request.form.getlist('activities')
        
        if not mood_rating or not stress_level:
            flash('Mood rating and stress level are required', 'error')
            return render_template('add_entry.html')
        
        entry = {
            'id': len(entries) + 1,
            'user_id': session['user_id'],
            'date': datetime.now(),
            'mood_rating': int(mood_rating),
            'stress_level': int(stress_level),
            'notes': notes,
            'activities': activities
        }
        
        entries.append(entry)
        flash('Entry added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_entry.html')

@app.route('/entries')
def view_entries():
    """View all user entries"""
    if 'user_id' not in session:
        flash('Please log in to view entries', 'error')
        return redirect(url_for('login'))
    
    user_entries = [entry for entry in entries if entry.get('user_id') == session['user_id']]
    user_entries.sort(key=lambda x: x['date'], reverse=True)
    return render_template('entries.html', entries=user_entries)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', error_code=500, error_message="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True)