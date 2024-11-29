# 🎨 Econecta ♻️

Este projeto é uma aplicação interativa desenvolvida em **Streamlit** que fornece recomendações de vídeos e projetos DIY (faça-você-mesmo) com base no feedback dos usuários e nos materiais disponíveis. É uma solução prática e sustentável para quem gosta de aprender, reaproveitar materiais e criar coisas novas!

---

## 🛠 Funcionalidades

1. **Recomendação de Vídeos**:
   - Avalie vídeos de categorias como Decoração, Jardinagem, e Utilitário.
   - Receba sugestões de novos vídeos com base nas suas avaliações.

2. **Calculadora Verde - Projetos DIY**:
   - Informe os materiais recicláveis e suas quantidades disponíveis.
   - Receba recomendações de projetos DIY adaptados ao que você possui e ao seu perfil.

---

## 📦 Tecnologias Utilizadas

- **Streamlit**: Para criar a interface interativa.
- **Pandas**: Para manipulação de dados.
- **Scikit-Learn**: Para cálculos de recomendação (similaridade por filtragem colaborativa).
- **Streamlit Option Menu**: Para a criação do menu lateral.

---

## 🚀 Como Rodar o Projeto

1. **Pré-requisitos**:
   - Certifique-se de ter o Python instalado (versão 3.8 ou superior).
   - Instale as dependências com o seguinte comando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Executar a Aplicação**:
   - No terminal, rode o seguinte comando:
     ```bash
     streamlit run app.py
     ```
   - A aplicação será aberta no navegador na URL `http://localhost:8501`.

---

## 📂 Estrutura do Projeto

- `app.py`: Arquivo principal contendo a lógica da aplicação.
- `requirements.txt`: Arquivo com as dependências necessárias.
- `README.md`: Documentação do projeto.

---

## 📊 Detalhes das Funcionalidades

### **Recomendação de Vídeos**
- A aplicação exibe vídeos com um player integrado do YouTube.
- O usuário avalia os vídeos usando um sistema de estrelas.
- Com base nas categorias mais bem avaliadas, a aplicação sugere novos vídeos relacionados.

### **Calculadora Verde - Projetos DIY**
- O usuário escolhe uma categoria de material reciclável (Plástico, Metal, Papel/Papelão ou Vidro).
- Com base na quantidade informada, a aplicação sugere projetos DIY que podem ser realizados.

---

## 🖼 Interface

- Menu lateral para navegar entre as funcionalidades.
- Interface simples e responsiva com feedback visual.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.

---

## 📄 Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

### ✨ Autor

Desenvolvido pelo time Econecta.  

