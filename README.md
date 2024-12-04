# API de Produtos

Este projeto é uma API para gerenciar produtos, desenvolvida com Flask e documentada com Swagger. A API permite criar, listar, atualizar e deletar produtos.

## 🛠️ Pré-requisitos

- Python 3.12+
- Virtualenv (opcional, mas recomendado)

## 🚀 Como Executar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Nuisigor/flask-api.git
   cd api-produtos
   ```

2. **Crie e ative o ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate          # Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Crie o arquivo `.env` na raiz do projeto** de acordo com as configurações necessárias indicadas no arquivo `.env.example`

5. **Execute o servidor**:

   ```bash
   flask --app main run
   ```

6. Acesse o projeto no navegador:
   ```
   http://localhost:5000
   ```

## 📖 Documentação da API

A documentação completa da API está disponível no Swagger UI, acessível em:

```
http://localhost:5000/docs
```

Lá você encontrará todas as rotas disponíveis, seus parâmetros e exemplos de respostas.

## 📝 Notas Importantes

- Para realizar requisições nas rotas protegidas (POST, PATCH, DELETE), é necessário incluir o cabeçalho `API-KEY` com sua chave de autenticação.
- O banco de dados padrão é configurado como SQLite.
