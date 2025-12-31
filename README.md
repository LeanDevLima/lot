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

Deploy no Render (passos rápidos)

1. Faça push do repositório para o GitHub (já feito): `https://github.com/LeanDevLima/lot`
2. No painel do Render: New -> Web Service.
	- Conecte seu repositório.
	- Language: Python 3
	- Build Command: `pip install -r requirements.txt`
	- Start Command: `gunicorn app:app -b 0.0.0.0:$PORT`
3. (Opcional) O repo inclui `runtime.txt` especificando Python 3.12.3 e `Procfile` com o comando de start.

Depois do build, sua aplicação ficará disponível no subdomínio `onrender.com` fornecido pelo painel.

Observação: Render faz deploy automático a cada push na branch ligada.
