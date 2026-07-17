# 🏅 API do Álbum de Figurinhas

Este é o backend da API do Álbum de Figurinhas, desenvolvido com **FastAPI** (Python). Ele gerencia as figurinhas da coleção e disponibiliza as imagens de forma dinâmica e individual para consumo do frontend.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **FastAPI**: Framework moderno e de alto desempenho para construir APIs.
- **Uvicorn**: Servidor ASGI rápido para rodar a aplicação.
- **CORS Middleware**: Configurado para permitir requisições de qualquer origem.

---

## 📂 Estrutura do Projeto

```text
├── figurinhas/        # Pasta contendo as imagens das figurinhas (01-alan-turing.jpg, etc.)
├── .gitignore         # Arquivos ignorados pelo Git (.venv, __pycache__, etc.)
├── main.py            # Código principal do servidor FastAPI
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do projeto (necessário para o deploy)
```

---

## 🚀 Como Rodar o Projeto Localmente

1. **Clone o repositório** para a sua máquina.
2. **Crie e ative o ambiente virtual (venv)**:
   - **No Windows (PowerShell)**:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - **No macOS/Linux/Git Bash**:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```
3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Inicie o servidor local**:
   ```bash
   uvicorn main:app --reload
   ```
   O servidor estará disponível em: **`http://127.0.0.1:8000`**

---

## 📡 Endpoints da API

- **Listar Figurinhas**: `GET /figurinhas`
  Retorna um JSON contendo todas as figurinhas disponíveis.
- **Obter Imagem de uma Figurinha**: `GET /figurinhas/{id}/imagem`
  Retorna o arquivo de imagem correspondente ao ID especificado.

---

## 🌐 Como Subir para o GitHub

1. Inicialize o repositório Git localmente na pasta do projeto:
   ```bash
   git init
   ```
2. Adicione todos os arquivos ao Git (o `.gitignore` garantirá que a pasta `.venv` não seja enviada):
   ```bash
   git add .
   ```
3. Crie o primeiro commit:
   ```bash
   git commit -m "feat: implementa api final com endpoints de imagens e cors"
   ```
4. Crie um repositório no seu GitHub, conecte e envie os arquivos:
   ```bash
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   git push -u origin main
   ```

---

## ☁️ Como Fazer o Deploy no Railway

1. Acesse o painel do [Railway](https://railway.app) e crie uma conta.
2. Clique em **"New Project"** -> **"Deploy from GitHub repo"**.
3. Selecione o repositório deste projeto que você enviou ao GitHub.
4. O Railway detectará o arquivo `requirements.txt` e iniciará a build do Python automaticamente.
5. **Configuração Importante**:
   Nas configurações da aplicação no painel do Railway (**Settings**), localize a seção **"Deploy"** e configure a variável do comando de inicialização (**Start Command**) para:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. O Railway gerará uma URL pública (ex: `https://seu-projeto.up.railway.app`). A partir daí, você poderá acessar os endpoints `/figurinhas` e `/figurinhas/{id}/imagem` diretamente pela internet!
