import streamlit as st
import QuerySQL as qSQL


# É necessário criar o banco de dados sqlite com a tabela e colunas que quiser.

st.markdown('# *Máquinas*')

opção = st.selectbox('Selecione uma das opções', ['Maquinas cadastradas', 'Inserir nova maquina', 'Atualizar registro'])

if opção == 'Maquinas cadastradas':
    st.spinner()
    qSQL.selectTabela()
elif opção == 'Inserir nova maquina':
    maquina = st.text_input('Informe a máquina: ')
    data = st.date_input('Data: ')
    codigo = st.text_input('Código: ')
    obs = st.text_input('Observação (caso tenha): ')

    inserir = st.button('Salvar')

    if inserir == True:
        qSQL.insertMaquina(maquina.upper(), data, codigo.upper(), obs)
elif opção == 'Atualizar registro':
    idMaquina = st.text_input('Informe o id da máquina que se quer alterar: ')
    # idMaquina = int(input('Informe o id da máquina que se quer alterar: '))
    id, nome, data, codigo, obs = qSQL.selectMaquina(idMaquina)
    # qSQL.updateMaquina(id, nome, obs)


