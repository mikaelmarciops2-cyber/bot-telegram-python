🤖 Bot Telegram em Python

Um bot para Telegram desenvolvido em Python, utilizando a biblioteca python-telegram-bot. O projeto serve como uma base simples para criar bots capazes de responder comandos, enviar mensagens automáticas e integrar-se à API oficial do Telegram.

✨ Funcionalidades

- Comando "/start"
- Comando "/ajuda"
- Respostas automáticas
- Integração com a API oficial do Telegram
- Estrutura simples e fácil de expandir

🛠️ Tecnologias

- Python 3.x
- python-telegram-bot

📦 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/bot-telegram-python.git
cd bot-telegram-python

Instale as dependências:

python -m pip install -r requirements.txt

⚙️ Configuração

Adicione o token do seu bot no arquivo "main.py":

TOKEN = "SEU_TOKEN_AQUI"

«Você pode obter um token criando um bot com o @BotFather no Telegram.»

▶️ Executando o projeto

Inicie o bot com:

python main.py

## 📁 Estrutura do projeto

```text
bot-telegram-python/
├── main.py            # Arquivo principal do bot
├── requirements.txt   # Dependências do projeto
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Documentação
```

💡 Exemplo de uso

Após iniciar o bot, envie os seguintes comandos no Telegram:

- "/start" — Inicia a conversa com o bot.
- "/ajuda" — Exibe a lista de comandos disponíveis.

🚀 Possíveis melhorias

- Adicionar variáveis de ambiente (".env") para armazenar o token.
- Criar mais comandos personalizados.
- Integrar banco de dados.
- Implementar registro de logs.
- Adicionar testes automatizados.

📄 Licença

Este projeto está disponível sob a licença MIT. Sinta-se à vontade para utilizar, modificar e distribuir.
