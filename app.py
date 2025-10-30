from flask import Flask, request, render_template_string

app = Flask(__name__)
# Szablon HTML
HTML = """
<!doctype html>
<html>
<head>
    <title>Witaj!</title>
</head>
<body>
    <h1>"Podaj swoje imię":</h1>
    <form method="post">
    <input type="text" name="name" placeholder="Twoje imię">
    <input type="submit" value="Wyślij">
    </form>

    {%if name%}
        <h2>WITAJ {{ name }}</h2>
    {%endif%}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        mame = request.form.get('name')
    return render_template_string(HTML, name=name)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000)