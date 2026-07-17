import os
import glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# 1. Configura o middleware CORS para aceitar requisições de qualquer origem (crucial para o frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Define os caminhos absolutos para encontrar a pasta de imagens de forma robusta
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# 3. Lista de figurinhas da API
# Apenas figurinhas com imagens físicas correspondentes (1 a 29) estão ativas.
# A figurinha 30 foi comentada por não possuir arquivo correspondente na pasta física.
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Sam", "categoria": "IA", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Geoffrey", "categoria": "IA", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Yann", "categoria": "IA", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Guido", "categoria": "Tecnologia", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Tim", "categoria": "Tecnologia", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Ray", "categoria": "Tecnologia", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Travis", "categoria": "Tecnologia", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Wes", "categoria": "Tecnologia", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Edgar", "categoria": "Tecnologia", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Larry", "categoria": "Tecnologia", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Michael", "categoria": "Tecnologia", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Salvatore", "categoria": "Tecnologia", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eliot", "categoria": "Tecnologia", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Linus", "categoria": "Tecnologia", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Dennis", "categoria": "Tecnologia", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Richard", "categoria": "Tecnologia", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Bill", "categoria": "Tecnologia", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Steve", "categoria": "Tecnologia", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Paulo", "categoria": "Tecnologia", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Guilherme", "categoria": "Tecnologia", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gus", "categoria": "Tecnologia", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Mauricio", "categoria": "Tecnologia", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Andre", "categoria": "Tecnologia", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Guilherme", "categoria": "Tecnologia", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Gi", "categoria": "Tecnologia", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Vinicius", "categoria": "Tecnologia", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Rafa", "categoria": "Tecnologia", "imagem_url": "/figurinhas/29/imagem"},
    # {"id": 30, "nome": "Figurinha 30", "categoria": "Tecnologia", "imagem_url": "/figurinhas/30/imagem"}
]

# 4. Endpoint GET para listar todas as figurinhas disponíveis
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Retorna a lista de figurinhas cadastradas.
    """
    return figurinhas

# 5. Endpoint GET para buscar a imagem de uma figurinha pelo ID
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    """
    Busca o arquivo de imagem correspondente ao ID informado usando glob,
    garantindo que coincida com o padrão numérico de 2 dígitos e não seja seguido de outros números.
    Retorna 404 se não for encontrada, ou a imagem via FileResponse se encontrada.
    """
    # Define o padrão de busca (ex: 01[!0-9]*)
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos_encontrados = glob.glob(padrao)
    
    if not arquivos_encontrados:
        raise HTTPException(status_code=404, detail="Imagem não encontrada para este ID")
    
    # Retorna o arquivo de imagem correspondente
    return FileResponse(arquivos_encontrados[0])
