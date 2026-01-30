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
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }}
            .container {{
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                max-width: 600px;
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
            .nav {{
                margin-top: 20px;
            }}
            .nav a {{
                margin: 0 10px;
                padding: 10px 20px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                display: inline-block;
            }}
            .nav a:hover {{
                background: #764ba2;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Current Time</h1>
            <div class="time">{current_time}</div>
            <div class="nav">
                <a href="javascript:location.reload()">Refresh</a>
                <a href="/about">About Me</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/about')
def about():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Me - Lumanex</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }
            h1 {
                color: #667eea;
                text-align: center;
                margin-bottom: 30px;
            }
            h2 {
                color: #764ba2;
                margin-top: 30px;
                border-bottom: 2px solid #667eea;
                padding-bottom: 10px;
            }
            .intro {
                font-size: 1.1em;
                line-height: 1.6;
                color: #333;
                text-align: center;
                margin-bottom: 30px;
            }
            .section {
                margin: 20px 0;
                line-height: 1.8;
                color: #555;
            }
            .skills {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin: 20px 0;
            }
            .skill-badge {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
            }
            .contact {
                background: #f5f5f5;
                padding: 20px;
                border-radius: 8px;
                margin-top: 30px;
            }
            .contact a {
                color: #667eea;
                text-decoration: none;
                font-weight: bold;
            }
            .contact a:hover {
                color: #764ba2;
            }
            .nav {
                text-align: center;
                margin-top: 30px;
            }
            .nav a {
                padding: 10px 30px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                display: inline-block;
            }
            .nav a:hover {
                background: #764ba2;
            }
            .highlight {
                color: #667eea;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 About Me</h1>
            
            <div class="intro">
                <p>Hello! I'm <span class="highlight">Emmanuel Ulu</span>, a passionate DevOps Engineer based in Lagos, Nigeria 🇳🇬</p>
            </div>

            <div class="section">
                <h2>🚀 What I Do</h2>
                <p>
                    I specialize in building robust CI/CD pipelines, automating infrastructure, 
                    and implementing cloud-native solutions. My focus is on creating efficient, 
                    scalable, and reliable systems that empower development teams to deliver 
                    better software faster.
                </p>
            </div>

            <div class="section">
                <h2>💻 Technical Skills</h2>
                <div class="skills">
                    <div class="skill-badge">Kubernetes</div>
                    <div class="skill-badge">Docker</div>
                    <div class="skill-badge">Terraform</div>
                    <div class="skill-badge">ArgoCD</div>
                    <div class="skill-badge">GitHub Actions</div>
                    <div class="skill-badge">Python</div>
                    <div class="skill-badge">Linux</div>
                    <div class="skill-badge">Helm</div>
                    <div class="skill-badge">AWS/Cloud</div>
                    <div class="skill-badge">Minikube</div>
                </div>
            </div>

            <div class="section">
                <h2>🎯 Current Project</h2>
                <p>
                    This application is part of my <strong>Complete DevOps Project</strong>, 
                    showcasing a full CI/CD pipeline implementation with:
                </p>
                <ul>
                    <li>Automated Docker image builds using GitHub Actions</li>
                    <li>Container orchestration with Kubernetes</li>
                    <li>GitOps deployment using ArgoCD</li>
                    <li>Infrastructure as Code with Terraform</li>
                    <li>Helm charts for application management</li>
                </ul>
            </div>

            <div class="section">
                <h2>🌟 Philosophy</h2>
                <p>
                    I believe in automation, infrastructure as code, and continuous improvement. 
                    Every system should be reproducible, scalable, and maintainable. I'm constantly 
                    learning and exploring new technologies to stay at the forefront of DevOps practices.
                </p>
            </div>

            <div class="contact">
                <h2>📫 Get In Touch</h2>
                <p>
                    <strong>Email:</strong> <a href="mailto:techlumanex@gmail.com">techlumanex@gmail.com</a><br>
                    <strong>GitHub:</strong> <a href="https://github.com/cloudlumanex" target="_blank">@cloudlumanex</a><br>
                    <strong>Location:</strong> Lagos, Nigeria 🌍
                </p>
            </div>

            <div class="nav">
                <a href="/">← Back to Time</a>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)