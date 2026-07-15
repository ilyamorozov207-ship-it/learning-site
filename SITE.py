from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Мой сайт</title>
</head>
<body>

<header style="text-align:center; padding:50px; background:#2563eb; color:white;">
    <h1>Мой сайт</h1>
    <p>Учебный проект на Flask</p>
</header>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)