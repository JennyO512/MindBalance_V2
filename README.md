# MindBalance_V2

A Flask-based web application for tracking mental health and well-being. Monitor your mood, stress levels, and daily activities to better understand your mental health patterns.

## Features

- **User Authentication**: Secure user registration and login system
- **Mood Tracking**: Rate your daily mood on a 1-10 scale
- **Stress Monitoring**: Track stress levels and identify patterns
- **Activity Logging**: Record daily activities that affect your mental health
- **Dashboard**: View recent entries and track progress over time
- **Responsive Design**: Works on desktop and mobile devices

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JennyO512/MindBalance_V2.git
   cd MindBalance_V2
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (optional):
   ```bash
   cp .env.example .env
   # Edit .env file with your settings
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and visit: `http://localhost:5000`

## Usage

1. **Register**: Create a new account on the registration page
2. **Login**: Sign in with your credentials
3. **Add Entry**: Record your daily mood, stress level, activities, and notes
4. **View Dashboard**: See your recent entries and overall progress
5. **Browse Entries**: View all your historical entries

## Development

This is an MVP (Minimum Viable Product) implementation. For production use, consider:

- Using a proper database (PostgreSQL, MySQL) instead of in-memory storage
- Implementing proper password hashing (bcrypt)
- Adding data visualization features
- Implementing user profile management
- Adding export functionality for personal data
- Setting up proper logging and monitoring

## Security Note

This MVP uses basic authentication for demonstration purposes. In production:
- Use proper password hashing
- Implement CSRF protection
- Use HTTPS
- Set a strong SECRET_KEY
- Implement rate limiting

## License

This project is open source and available under the [MIT License](LICENSE).