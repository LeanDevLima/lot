#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, flash
from loteria import carregar_sequencias, calcular_acertos, ARQUIVO_JSON
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

try:
    sequencias = carregar_sequencias(ARQUIVO_JSON)
    load_error = None
except Exception as e:
    sequencias = None
    load_error = str(e)


@app.route("/", methods=["GET", "POST"])
def index():
    if load_error:
        return render_template("error.html", error=load_error), 500
    if request.method == "POST":
        # coletar os seis campos individuais
        campos = []
        for i in range(1, 7):
            v = request.form.get(f"dez{i}")
            if v is None:
                flash("Todos os 6 campos devem ser preenchidos.")
                return redirect(url_for("index"))
            campos.append(v.strip())
        try:
            dezenas = [int(x) for x in campos]
        except ValueError:
            flash("Use apenas números inteiros nos campos.")
            return redirect(url_for("index"))
        if len(dezenas) != 6 or len(set(dezenas)) != 6 or any(n < 1 or n > 60 for n in dezenas):
            flash("Informe exatamente 6 dezenas distintas entre 1 e 60.")
            return redirect(url_for("index"))
        resultado = calcular_acertos(sequencias, dezenas)
        return render_template("result.html", dezenas=dezenas, resultado=resultado)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
