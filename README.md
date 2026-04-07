![Python](https://img.shields.io/badge/python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/docker-container-blue)
## 📌 Descrição

Este projeto consiste em uma API CRUD (Create, Read, Update, Delete) para gerenciamento de filmes, com foco em organização de código, escalabilidade e uso de tecnologias modernas do ecossistema Python.

A aplicação utiliza **FastAPI** para construção da API, **MongoDB** como banco de dados NoSQL e **Docker** para containerização.

---

## 🛠️ Tecnologias

- ⚡ FastAPI
- 🐍 Python 3.10
- 🍃 MongoDB
- 🐳 Docker & Docker Compose
- 📦 Pydantic
- 🔗 PyMongo


---

## 🧠 Arquitetura

A aplicação segue o padrão de **arquitetura em camadas**, separando responsabilidades:

- **Router** → recebe requisições HTTP
- **Service** → contém a lógica de negócio
- **Repository** → interage com o banco de dados
- **Schema** → valida os dados de entrada e saída


## ▶️ Como executar o projeto

### 🔧 Pré-requisitos

- Docker instalado
- MongoDB Instalado

---

### 🚀 Subindo a aplicação

```bash
docker-compose up --build
🌐 Acesse a API
Swagger UI:
http://localhost:8000/docs
📌 Endpoints
➤ Criar filme

POST /movies/

{
  "title": "Velozes e Furiosos",
  "director": "Rob Cohen",
  "year": 2001,
  "genre": "Ação"
}
➤ Listar filmes

GET /movies/

➤ Buscar por ID

GET /movies/{id}

➤ Atualizar filme

PUT /movies/{id}

{
  "title": "Velozes e Furiosos 2",
  "director": "Rob Cohen",
  "year": 2003,
  "genre": "Ação"
}
➤ Deletar filme

DELETE /movies/{id}

🐳 Docker

O projeto utiliza Docker para facilitar a execução e garantir consistência do ambiente.

Serviços utilizados:
API → FastAPI rodando na porta 8000
MongoDB → Banco de dados na porta 27017
⚠️ Observações
O MongoDB roda em container local
Não há autenticação implementada nesta versão
Projeto focado em aprendizado de APIs e arquitetura backend
🚀 Melhorias futuras
🔐 Implementar autenticação com JWT
🧪 Adicionar testes automatizados
📊 Implementar logs
☁️ Deploy em produção (AWS, Railway, etc)
🔎 Filtros, paginação e busca
👨‍💻 Autor

Desenvolvido por Cairo 🚀
```
📜 Licença

Este projeto está sob a licença MIT.


---
