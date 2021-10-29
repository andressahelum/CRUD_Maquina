import sqlite3
import pandas as pd
import streamlit as st
import time


def conectarSQLServer():
    try:
        # Estabelecendo a conexão com o banco de dados
        # global conexao
        # global cursor

        conexao = sqlite3.connect('Maquinas.db')
        cursor = conexao.cursor()
        return conexao, cursor
        print("Conexão bem sucedida ao banco de dados.")
    except sqlite3.Error as erro:
        print(f"Falha na conexão ao banco de dados. Erro: {erro}")


def selectTabela():
    try:
        with st.spinner(text='Carregando tabela...'):
            time.sleep(3)
        conexao, cursor = conectarSQLServer()
        query = 'Select * from Maquina'
        tbMaquina = pd.read_sql(query, conexao)
        st.success('Tabela carregada com sucesso!')
        st.write(tbMaquina)
    except sqlite3.Error as erro:
        st.error(f'Falha na conexão com o banco de dados. Erro: {erro}')
    finally:
        conexao.close()


def insertMaquina(nome, data, codigo, obs):
    try:
        conexao, cursor = conectarSQLServer()
        query = f'''insert into Maquina (nomeMaquina, dataMaquina, codigoMaquina, obsMaquina)
                values ('{nome}', '{data}', '{codigo}', '{obs}')'''
        cursor.execute(query)
        conexao.commit()
        st.success('Maquina salva com sucesso.')
    except sqlite3.Error as erro:
        st.error(f'Não foi possível salvar os dados. Erro: {erro}')
    finally:
        conexao.close()


def selectMaquina(id):
    try:
        conexao, cursor = conectarSQLServer()
        # Select pra buscar e guardar os dados anteriores da máquina selecionada
        query = f'''select *
                from Maquina
                where idMaquina = {id}
                '''
        cursor.execute(query)
        Linha = cursor.fetchall()
        # Guardar id e nome anteriores
        for coluna in Linha:
            id = coluna[0]
            nome = coluna[1]
            data = coluna[2]
            codigo = coluna[3]
            obs = coluna[4]

            print(f'Id: {id}    Máquina: {nome}     Data: {data}    Codigo: {codigo}      Observação: {obs}')
        return id, nome, data, codigo, obs
    except sqlite3.Error as erro:
        print(f'Não foi possível acessar as informações do ID: {id}. Erro: {erro}')
    finally:
        conexao.close()

