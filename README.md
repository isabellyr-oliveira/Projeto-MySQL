# CRUD com MySQL + Python + Streamlit

Este projeto é um exemplo prático de CRUD usando:
- Banco de dados **MYSQL**
- Conexão com o **mysql.connector**
- Interface web com **streamlit**

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/isabellyr-oliveira/Projeto-MySQL
```

### 2. Instalar dependencias 
```bash
pip install -r requirements.txt
```

### 3. Configurar as veriáveis de ambiente
crie um arquivo .env na raiz do seu projeto com:
```bash
DB_NAME=faculdade
DB_USER=root
DB_PASSWORD=dev1t@25
DB_HOST=localhost
```

### 4. Rodar aplicação
```bash
python -m streamlit run app.py
```

### 5. Funcionalidades

- Inserir registros no db

- Listar registros no db

- Atualizar registros no db

- Deletar registros no db

- Interface simples com streamlit