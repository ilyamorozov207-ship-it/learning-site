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

<section style="padding:40px;">

<h2 align="center">Наши разделы</h2>

<div style="display:flex;justify-content:space-around;flex-wrap:wrap;">

<div style="width:220px;padding:20px;margin:10px;background:#eee;border-radius:10px;">
<h3>Python</h3>
<p>Изучение Python.</p>
</div>

<div style="width:220px;padding:20px;margin:10px;background:#eee;border-radius:10px;">
<h3>Flask</h3>
<p>Создание сайтов.</p>
</div>

<div style="width:220px;padding:20px;margin:10px;background:#eee;border-radius:10px;">
<h3>Git</h3>
<p>Контроль версий.</p>
</div>

<div style="width:220px;padding:20px;margin:10px;background:#eee;border-radius:10px;">
<h3>GitHub</h3>
<p>Публикация проектов.</p>
</div>

</div>

</section>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)