# Front-end para `loteria.py` (Flask)

Passos rápidos para rodar no Ubuntu (assumindo Python 3 instalado):

1. Crie um ambiente virtual e ative:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Rode a aplicação:

```bash
python3 app.py
```

Acesse em `http://127.0.0.1:5000` e informe as 6 dezenas (separadas por espaço).

Observações:
- O arquivo `sequencias.json` deve permanecer na mesma pasta.
- O front-end reutiliza as funções de `loteria.py` para carregar as sequências e calcular os acertos.
