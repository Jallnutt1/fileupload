from main import app

if __name__ == '__main__':
    app.run(debug=True)

# gunicorn --bind 0.0.0.0:5000 wsgi:app