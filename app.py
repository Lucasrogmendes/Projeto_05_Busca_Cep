import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd

##### TÍTULO DA APLICAÇÃO #####

st.title("Busca CEP")


##### Lista de Opções #####

opcao = ["Buscar CEP","Descobrir CEP"]

##### BARRA LATERAL #####

st.sidebar.title("Busca CEP")
st.sidebar.image("logo.png", width=400)
st.sidebar.write("Aplicação para buscar endereço a partir do CEP e mostrar localização no mapa")
escolha = st.sidebar.selectbox("Escolha uma opção:", opcao)
##### BOTÃO BUSCAR CEP #####

if pagina == "Buscar CEP":
    st.header("Buscar endereço pelo CEP")
    cep = st.text_input("Digite o CEP (somente números):")


    if st.button("Buscar"):
            if len(cep) != 8 or not cep.isdigit():
                st.error("Por favor, insira um CEP  válido com 8 digitos numéricos.")
            else:
                try:
                    endereço = BuscarCep.buscar_cep(cep)
                    if endereço:
                         st.success("Endereço encontrado:")
                         st.write(f"CEP: {endereço[0]}")
                         st.write(f"Endereço: {endereço[1]}")
                         st.write(f"Bairro: {endereço[2]}")
                         st.write(f"cidade: {endereço[3]}")
                         st.write(f"Estado: {endereço[4]}")

                         ## Mapas
                         st.title("Localização no Mapa")
                         df = pd.DataFrame({"latitude": [endereço[5]], "longitude": [endereço[6]]})
                         st.map(df, zoom=15)
                    else:
                         st.error("CEP não encontrado")
                except Exception as e:
                     st.error(f"Ocorreu um erro ao buscar o CEP: {e}")




##### BOTÃO DESCOBRIR CEP #####

elif escolha == "Descobrir CEP":
    st.image("Descobrir.png")
    st.header("Descobrir CEP pelo Endereço")
    endereco_usuario = st.text_input("Digite o endereço (ex: Rua olga, Barueri, SP):")

    if st.button("Descobrir"):
        if not endereco_usuario.strip():
            st.error("Por favor, insira um endereço válido.")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("Link de busca no Google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro ao descobrir o CEP: {e}")

            
