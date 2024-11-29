import streamlit as st
import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity

# Biblioteca para abas
from streamlit_option_menu import option_menu

# =================== Configuração de dados ===================
# Base de vídeos para recomendação colaborativa
videos = [
    {"id": "kpOqKoEs1Ds", "title": "10 + Ideias de DIY: Transformando Lixo em Luxo, Artesanato e Reciclagem para 2023", "category": "Decoração"},
    {"id": "KO3tGFHUOKs", "title": "16 IDEIAS DE ARTESANATOS INCRÍVEIS DE RECICLAGEM PARA NATAL", "category": "Decoração"},
    {"id": "fGVk-1NC_pQ", "title": "12 TRUQUES DE RECICLAGEM ABSOLUTAMENTE GENIAIS", "category": "Utilitário"},
    {"id": "90rKz93kA-E", "title": "DIY - IDEIA COM GARRAFA PET / PARA JARDIM", "category": "Jardinagem"},
    {"id": "w5FebJwI4i8", "title": "DIY - IDEIA COM GARRAFA PET / PARA JARDIM #2", "category": "Jardinagem"},
    {"id": "oMq7yB-FkF8", "title": "Casa de Passarinho🐦 feita com garrafa pet e Potes", "category": "Utilitário"},
  
]

# Tamanho do player
player_width = 450
player_height = 200




# Base adicional de vídeos para filtragem por conteúdo
additional_videos = [
    {"id": "7EYglzpo70Q", "title": "10 IDEIAS DE RECICLAGEM ABSOLUTAMENTE GENIAIS COM PLÁSTICO", "category": "Utilitário"},
    {"id": "BLve3TAqWi0", "title": "Diy Decoração Natalina - Mini Arvore de Natal Artesanal", "category": "Decoração"},
    {"id": "2dcjlFhA_jw", "title": "ELEFANTE feito com Embalagem (garrafa) de Amaciante", "category": "Decoração"},
    {"id": "v0aplXQxGFw", "title": "DIY - VASO ELEFANTE feito com vidro de AMACIANTE", "category": "Jardinagem"},

]

st.markdown(
    """
    <style>
    .small-title {
        font-size: 16px; /* Reduz o tamanho do título */
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .small-button {
        font-size: 150px; /* Reduz o tamanho do texto do botão */
        padding: 0px 0px; /* Ajusta o espaçamento interno do botão */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

player_width_recommendation = 30  # Largura menor
player_height_recommendation = 600  # Altura menor
# Estilo CSS para títulos e layout reduzidos
st.markdown(
    """
    <style>
    .recommendation-title {
        font-size: 20px; /* Tamanho menor para títulos */
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .video-frame {
        width: 100%; /* Ajusta a largura para 100% do contêiner */
        max-width: 500px; /* Limita a largura máxima */
        height: auto; /* Mantém a proporção */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Base de projetos DIY (faça-você-mesmo)
projects = [
    {"project": "Vaso de Planta com Garrafa PET", "materials": {"garrafa PET": 1}},
    {"project": "Organizador de Mesa com Caixa de Sapato", "materials": {"caixa de sapato": 1, "papel decorativo": 2}},
    {"project": "Cofrinho com Garrafa PET", "materials": {"garrafa PET": 2, "tampa plástica": 1}},
    {"project": "Porta-Treco com Latas de Alumínio", "materials": {"lata de alumínio": 3, "tinta spray": 1}},
    {"project": "Abajur com Palitos de Sorvete", "materials": {"palitos de sorvete": 30, "cola quente": 1}},
]

# Dados simulados de avaliações de outros usuários (User-Item Matrix)
user_ratings = pd.DataFrame({
    "user": ["User1", "User2", "User3", "User4", "User5"],
    "vajY3r1wAMk": [5, 4, 4, 2, 1],
    "vajY3r1wAMk": [3, 5, 2, 1, 0],
    "vajY3r1wAMk": [4, 0, 3, 5, 2],
    "vajY3r1wAMk": [1, 3, 5, 0, 4],
    "jj1GMYDAeyDM": [5, 0, 4, 3, 2],
    "jj1GMYDAeyDM": [0, 2, 3, 5, 4],
    "jj1GMYDAeyDM": [4, 5, 2, 1, 0],
    "jj1GMYDAeyDM": [3, 2, 1, 5, 4],
}).set_index("user")

# Dados de avaliações do usuário atual
if "user_feedback" not in st.session_state:
    st.session_state.user_feedback = pd.DataFrame(columns=["video_id", "rating"])

# =================== Interface com Abas ===================
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Aprende Mais - Recomendação de Vídeos", "Calculadora Verde - Recomendação por Conteúdo"],
        icons=["play-circle", "tools"],
        menu_icon="cast",
        default_index=0,
    )

# =================== Recomendação de Vídeos (Filtragem por Conteúdo) ===================
if selected == "Aprende Mais - Recomendação de Vídeos":
    st.title("Aprende Mais - Recomendador de Vídeos por Filtragem por Conteúdo")
    st.write("Assista aos vídeos e avalie-os para receber recomendações personalizadas!")

    
    for video in videos:
        # Criação de colunas: uma para o vídeo e outra para o slider e botão
        col1, col2 = st.columns([2, 1])  # Ajuste a proporção (2:1) para balancear o espaço

        # Vídeo na primeira coluna
        with col1:
            st.markdown(f"<div class='small-title'>{video['title']}</div>", unsafe_allow_html=True)
            video_url = f"https://www.youtube.com/embed/{video['id']}"
            st.markdown(
                f"""
                <iframe width="{player_width}" height="{player_height}" 
                src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
                encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
                </iframe>
                """,
                unsafe_allow_html=True,
            )

        # Slider e botão na segunda coluna
        with col2:
            rating = st.feedback(
                "stars",
                key=f"slider_{video['id']}"
            )
            if st.button(f"Salvar Avaliação", key=f"save_{video['id']}"):
                # Adiciona avaliação ao estado
                new_feedback = pd.DataFrame([{"video_id": video["id"], "rating": rating}])
                st.session_state.user_feedback = pd.concat([st.session_state.user_feedback, new_feedback], ignore_index=True)
                st.success("Avaliação salva!")

   

    # Filtragem por conteúdo
    recommendations = []
    if not st.session_state.user_feedback.empty:
        # Identifica categorias favoritas baseadas em avaliações positivas
        liked_categories = st.session_state.user_feedback.merge(
            pd.DataFrame(videos), left_on="video_id", right_on="id"
        )["category"].unique()

        # Busca vídeos na base adicional da mesma categoria
        recommendations = [
            video for video in additional_videos if video["category"] in liked_categories
        ]

    # Exibe as recomendações finais
    if recommendations:
        st.write("### Recomendações para você:")
        for video in recommendations:
            st.markdown(f"<div class='recommendation-title'>{video['title']}</div>", unsafe_allow_html=True)
            # Ajuste de vídeo com novo tamanho
            video_url = f"https://www.youtube.com/embed/{video['id']}"
            st.markdown(
                f"""
                <iframe class="video-frame" src="{video_url}" frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
                </iframe>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.write("### Nenhuma recomendação disponível. Avalie mais vídeos para receber sugestões!")


if selected == "Calculadora Verde - Recomendação por Conteúdo":

    # Base de projetos DIY com materiais e quantidades
    projects_diy = [
        # Plástico
        {
            "project": "Porta-canetas com garrafas PET",
            "materials": {"garrafa PET": 1},
        },
        {
            "project": "Puff com garrafas PET",
            "materials": {"garrafa PET": 20},
        },
        {
            "project": "Vasos para plantas suspensos",
            "materials": {"garrafa PET": 3},
        },
        # Metal
        {
            "project": "Lanternas decorativas com latas de alumínio",
            "materials": {"lata de alumínio": 2},
        },
        {
            "project": "Porta-trecos com latas de conserva",
            "materials": {"lata de conserva": 3},
        },
        {
            "project": "Mini fogareiro com latas de alumínio",
            "materials": {"lata de alumínio": 2},
        },
        # Papel e Papelão
        {
            "project": "Organizador de mesa com rolos de papel higiênico",
            "materials": {"rolo de papel higiênico": 5, "caixa de papelão": 1},
        },
        {
            "project": "Móveis de papelão (banquinho ou mesinha)",
            "materials": {"caixa de papelão": 10},
        },
        {
            "project": "Luminária com tiras de papel",
            "materials": {"tiras de papel": 20},
        },
        # Vidro
        {
            "project": "Vasos decorativos com potes de vidro",
            "materials": {"pote de vidro": 3},
        },
        {
            "project": "Castiçais com frascos de vidro",
            "materials": {"frasco de vidro": 2},
        },
        {
            "project": "Luminária com garrafas de vidro",
            "materials": {"garrafa de vidro": 1},
        },
    ]

    # =================== Recomendação por Conteúdo ===================
    st.title("Calculadora Verde - Recomendação por Conteúdo de Projetos DIY")
    st.write("Selecione o material e informe a quantidade disponível para receber recomendações de projetos DIY!")

    # Entrada do material e quantidade
    material_category = st.selectbox(
        "Selecione o material disponível:",
        options=["Plástico", "Metal", "Papel e Papelão", "Vidro"],
    )

    material_quantity = st.number_input("Informe a quantidade disponível:", min_value=1, step=1)

    # Mapeia a categoria de materiais para os nomes específicos usados nos projetos
    material_mapping = {
        "Plástico": ["garrafa PET"],
        "Metal": ["lata de alumínio", "lata de conserva"],
        "Papel e Papelão": ["rolo de papel higiênico", "caixa de papelão", "tiras de papel"],
        "Vidro": ["pote de vidro", "frasco de vidro", "garrafa de vidro"],
    }

    # Processa a entrada do usuário e filtra projetos
    if st.button("Buscar Projetos"):
        relevant_materials = material_mapping.get(material_category, [])
        recommended_projects = [
            project
            for project in projects_diy
            for material in relevant_materials
            if material in project["materials"] and project["materials"][material] <= material_quantity
        ]

        if recommended_projects:
            st.write("### Projetos recomendados:")
            for project in recommended_projects:
                st.subheader(project["project"])
                st.write("Materiais necessários:")
                for material, quantity in project["materials"].items():
                    st.write(f"- {quantity}x {material.capitalize()}")
        else:
            st.warning("Nenhum projeto encontrado para os materiais e quantidades informados.")