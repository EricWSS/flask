from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola():
    return """<!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Aqui tentarei executar um formulário.</h1>
            
        </body>
        </html>"""

if __name__ == '__main__':
    app.run(debug=True)
