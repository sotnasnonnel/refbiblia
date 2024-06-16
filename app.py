import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import random
import base64

# Função para carregar a imagem de fundo como base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Carregar dados
file_path = 'cross_reference.csv'
data = pd.read_csv(file_path)

# Função para criar o gráfico de arco
def plot_arcs(data, num_edges_to_plot=1000):
    # Converter versos e referências para índices numéricos para plotagem
    verses = data['verse'].values
    references = data['ref'].values
    all_verses = sorted(set(verses) | set(references))
    verse_index = {verse: idx for idx, verse in enumerate(all_verses)}

    # Limitar o número de arestas para visualização
    edges = list(zip(verses, references))[:num_edges_to_plot]

    # Preparar os dados para plotagem
    fig = go.Figure()

    for verse, ref in edges:
        start = verse_index[verse]
        end = verse_index[ref]
        mid = (start + end) / 2
        height = abs(end - start) / 2
        theta = np.linspace(0, np.pi, 100)
        x = np.linspace(start, end, 100)
        y = height * np.sin(theta)
        color = 'rgba(%d, %d, %d, 1)' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color=color, width=0.5)))

    fig.update_layout(
        showlegend=False, 
        xaxis=dict(visible=False), 
        yaxis=dict(visible=False),
        title="Referências Bíblicas Cruzadas",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig)

# Layout da página
st.set_page_config(layout="wide")

# Adicionar o fundo da página e estilos
background_image_base64 = get_base64_of_bin_file('background.png')
page_bg_img = f'''
<style>
body {{
    background-image: url("data:image/png;base64,{background_image_base64}");
    background-size: cover;
    color: white;
}}
.stApp {{
    background: url("data:image/png;base64,{background_image_base64}");
    background-size: cover;
}}
h1, h2, h3, h4, h5, h6, p, div, span {{
    color: white !important;
}}
footer {{
    visibility: hidden;
}}
.footer {{
    position: fixed;
    bottom: 0;
    right: 0;
    width: 100%;
    text-align: right;
    font-size: small;
    color: white;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Dividir a página em duas colunas
col1, col2 = st.columns([3, 1])

with col1:
    # Título
    st.title("Visualização das Referências Cruzadas na Bíblia")

    # Mostrar total de referências
    total_references = data.shape[0]
    st.write(f"Total de referências na Bíblia: {total_references}")

    # Plotar o gráfico
    num_edges_to_plot = st.slider("Número de arestas para plotar ( foi acrescentado para carregar o gráfico de forma mais rápida)", min_value=100, max_value=total_references, value=1000)
    plot_arcs(data, num_edges_to_plot)

    # Adicionar o texto explicativo abaixo do gráfico
    st.write("""
    Este gráfico representa as conexões entre diferentes versículos da Bíblia. Cada linha colorida representa uma referência cruzada entre dois versículos.
    A Bíblia é um texto altamente interconectado, e estas conexões mostram como diferentes partes da escritura se referem e se complementam.
    """)

with col2:
    # Informações adicionais sobre a Bíblia
    total_books = 66  # Total de livros na Bíblia
    total_verses = 31102  # Aproximadamente o total de versículos na Bíblia
    total_authors = 40  # Aproximadamente o total de autores diferentes

    # Espaçamento para centralizar o texto
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.write(f"""
    ### A Interconexão da Bíblia:
    Este gráfico representa as conexões entre diferentes versículos da Bíblia. Cada linha colorida representa uma referência cruzada entre dois versículos. 
    A Bíblia é um texto altamente interconectado, e estas conexões mostram como diferentes partes da escritura se referem e se complementam.

    A Bíblia contém um total de {total_books} livros e aproximadamente {total_verses} versículos. 
    Ela foi escrita por cerca de {total_authors} autores diferentes ao longo de muitos séculos, cobrindo uma vasta gama de temas e histórias.
    Mesmo assim, ela apresenta uma unidade e coerência impressionantes, demonstrando como essas diversas partes se conectam de maneira harmoniosa.

    Essa interconexão extraordinária é um testemunho da perfeição e da inspiração divina da Bíblia. Cada referência cruzada ressalta como 
    Deus, através de diferentes autores e épocas, revelou Sua mensagem de forma consistente e perfeita.

    As 612.591 referências cruzadas da Bíblia referem-se às interconexões entre diferentes versículos, 
    capítulos e livros da Bíblia, onde um texto faz referência ou se relaciona com outro texto em algum lugar da Bíblia. 
    Essas referências cruzadas podem incluir citações diretas, alusões, paralelos temáticos, 
    profecias e seus cumprimentos, entre outros.

    Um exemplo famoso é o diagrama de referências cruzadas criado por Christoph Römhild e Chris Harrison, 
    que visualiza todas essas conexões em um gráfico impressionante, mostrando as relações complexas e interconectadas dentro 
    do texto bíblico.

    Embora listar todas as 612.591 referências cruzadas individualmente aqui seja impraticável, 
    esses tipos de gráficos e ferramentas de estudo bíblico podem ser usados para explorar essas conexões. 
    Ferramentas como software de estudo bíblico (e.g., Logos, Accordance, BibleWorks) e algumas Bíblias digitais oferecem 
    funcionalidades para explorar essas referências cruzadas detalhadamente.
    """)

# Rodapé
st.markdown("""
    <div class="footer">
        by: Lennon Santos
    </div>
""", unsafe_allow_html=True)
