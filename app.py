from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template (embedded for simplicity)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker CI/CD App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            text-align: center;
            padding: 50px;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            display: inline-block;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }
        h1 {
            margin-bottom: 10px;
        }
        p {
            font-size: 18px;
        }
        .btn {
            margin-top: 20px;
            padding: 10px 20px;
            background: #00c6ff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .btn:hover {
            background: #0072ff;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Docker CI/CD Pipeline</h1>
        <p>Status: Running Successfully</p>
        <p>Built using Flask + Docker + Jenkins</p>
        <button class="btn" onclick="window.location.href='/info'">View Info</button>
    </div>
</body>
</html>
"""

INFO_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>App Info</title>
</head>
<body style="font-family: Arial; text-align:center; padding:50px;">
    <h1>📊 Application Info</h1>
    <p><b>Project:</b> Docker FAT Experiment</p>
    <p><b>DockerHub:</b> akbaraliiii/docker-fat-app</p>
    <p><b>CI/CD:</b> Jenkins Pipeline</p>
    <p><b>Status:</b> ✅ Active</p>
    <br>
    <a href="/">⬅ Back</a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/info')
def info():
    return render_template_string(INFO_PAGE)

@app.route('/health')
def health():
    return {"status": "OK", "message": "App is healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)