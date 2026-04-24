from flask import Flask, render_template
import os
import PyPDF2

app = Flask(__name__)

def extrair_texto_pdf(caminho_pdf):
    with open(caminho_pdf, "rb") as f:
        leitor = PyPDF2.PdfReader(f)
        texto = ""
        for pagina in leitor.pages:
            texto += pagina.extract_text() + "\n"
        return texto

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre-mim")
def sobre_mim():
    imagem = "portfolio_francisco.png"
    caminho_imagem = os.path.join(app.static_folder, imagem)
    imagem_existe = os.path.exists(caminho_imagem)

    pdf_nome = "livro_sobre_mim.pdf"
    caminho_pdf = os.path.join(app.static_folder, pdf_nome)

    texto_pdf = ""
    if os.path.exists(caminho_pdf):
        texto_pdf = extrair_texto_pdf(caminho_pdf)

    return render_template(
        "sobre_mim.html",
        imagem=imagem,
        imagem_existe=imagem_existe,
        texto_pdf=texto_pdf
    )

@app.route("/docentes")
def docentes():
    return render_template("docentes.html")

@app.route("/pras")
def pras():
    return render_template("pras.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
