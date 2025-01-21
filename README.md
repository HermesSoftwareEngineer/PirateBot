# PirateBot 🏴‍☠️🤖  
**PirateBot** é uma inteligência artificial construída com Flask e LangChain que permite interagir com um chatbot que responde como um pirata! ⚓️ Ideal para quem deseja uma experiência divertida e envolvente com respostas no melhor estilo dos sete mares.  

---

## 🚀 Funcionalidades  
- Respostas personalizadas no estilo pirata.  
- Processamento de linguagem natural usando LangChain.  
- Interface simples criada com Flask.  

---

## 🛠️ Tecnologias Utilizadas  
- **Flask**: Framework web para criação da API e interface.  
- **LangChain**: Para orquestrar o comportamento da IA.  
- **OpenAI API**: Motor para geração das respostas.  

---

## 📦 Como Rodar o Projeto  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/piratebot.git
   cd piratebot
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv  
   source venv/bin/activate  # Linux/Mac  
   venv\Scripts\activate  # Windows
3. Instale as dependências:  
   ```bash
   pip install -r requirements.txt  
4. Configure o caminho json da chave da VertexAI API (google) no arquivo app_model:  
   ```bash
   os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'o/caminho/para/sua/chave.json'
5. Execute a aplicação:  
   ```bash
   flask --app piratebot run --debug

---

## 🎯 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests
