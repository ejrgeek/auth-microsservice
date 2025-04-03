# Microsserviço de Autenticação (Auth-Service)

#### Workshop: Deploy & Segurança em Aplicações Web: O que fazer e o que não fazer

##### Ministrado por: Erlon


## Visão Geral
Microsserviço de autenticação básica com:
- Registro e Login de usuários
- Token JWT com expiração configurável
- PostgreSQL
- Dicas e Práticas recomendadas de segurança

## Configuração inicial:
1. Crie seu `.env`:
```bash
DATABASE_URL=postgresql://user:password@localhost/auth_db
JWT_SECRET_KEY=suachavemuitosecreta
``` 

2. Configuração do Banco:
```bash
CREATE DATABASE auth_db;
CREATE USER auth_user WITH PASSWORD 'senha_segura';
GRANT ALL PRIVILEGES ON DATABASE auth_db TO auth_user;
GRANT CREATE, CONNECT ON DATABASE auth_db TO auth_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO auth_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO auth_user;
CREATE SCHEMA auth_schema;
GRANT ALL PRIVILEGES ON SCHEMA auth_schema TO auth_user;
```

3. Aambiente virtual e execução:
```bash
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug --host=0.0.0.0
```

## Endpoints
1. Registro
- POST `/api/auth/register`

**Body:**
```bash
{
  "username": "novousuario",
  "password": "senhasegura123"
}
```
**Response:**
```bash
{
  "message": "User created!",
  "token": "eyJhb...",
  "expires_in": 2592000
}
```

2. Login
- POST `/api/auth/login`

**Body:**
```bash
{
  "username": "novousuario",
  "password": "senhasegura123"
}
```
**Response:**
```bash
{
  "token": "eyJhb...",
  "expires_in": 2592000
}
```

## Boas Práticas
✅ Senhas:
- Hash com PBKDF2-SHA256 + salt (via Werkzeug).

✅ Tokens JWT:

- Expiração em 30 dias (configurável em config.py).
- Chave secreta definida por variável de ambiente.

✅ Banco de Dados:
- Isolamento em schema dedicado (auth_schema).
- Credenciais acessadas apenas por variáveis de ambiente.

⚠️ NUNCA COMETA:
- Hardcodar senhas no código (use .env!)
- Nunca armazenadas em texto puro.crypt)


## Configuração de Deploy:
Deve ser feito pelo Aluno conforme ministrado em aula