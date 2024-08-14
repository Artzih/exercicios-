import streamlit as st
st.title("Preços e promoções")

st.text("""Códigos de origem:
        1: Norte: 5%
        2: Sul: 15%
        3: Sudeste: 7%
        4: Nordeste: 12%
        5: Centro-Oeste: 20%""")

st.sidebar.header("Escolha os números:")

preco = st.sidebar.number_input("Preço do produto:",value=0)
codigo_produto = st.sidebar.number_input("Digite o código de origem do produto (1-5)",value=0)

preco_total = st.sidebar.button("Calcular preço total")
if preco_total:
    
    if codigo_produto == 1:
        media1 = (preco*0.05)
        st.write(f"O preço total é igual a ",media1)
                
    elif codigo_produto == 2:
        media2 = (preco*0.15)
        st.write(f"O preço total é igual a ",media2)
                 
    elif codigo_produto == 3:
        media3 = (preco * 0.07)
        st.write(f"O preço total é igual a ",media3)
    elif codigo_produto == 4:
        media4 = (preco *0.12)
        st.write(f"O preço total é igual a ",media4)
    elif codigo_produto == 5:
        media5 = (preco*0.20)
        st.write(f"O preço total é igual a ",media5)
else:
    st.write("codigo de produto não valido por favor reinicie a pagina")


