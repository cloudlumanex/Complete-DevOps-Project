from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Current Time in Nigeria</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }}
            .container {{
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }}
            h1 {{
                color: #333;
                margin-bottom: 20px;
            }}
            .time {{
                font-size: 2em;
                color: #667eea;
                font-weight: bold;
            }}
            .refresh {{
                margin-top: 20px;
                padding: 10px 20px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 1em;
            }}
            .refresh:hover {{
                background: #764ba2;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Current Time</h1>
            <div class="time">{current_time}</div>
            <button class="refresh" onclick="location.reload()">Refresh</button>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)