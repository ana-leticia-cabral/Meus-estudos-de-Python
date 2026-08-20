# Script em python desenvolvido para auxiliar meus estudos de limpeza e tratamento dos dados
# O objetivo é me oferecer um panorama inicial dos dados que eu obtive
# Qualquer limpeza/procedimento que eu tenha que realizar a parte não estará nesse código.

import pandas as pd

# Compreensão dos dados

def caracteristicas_dados(df):

	print("Primeira visualização dos dados:")
	print(df.head(20))

	linhas, colunas = df.shape
	print(f"Os dados possuem {linhas} linhas e {colunas} colunas.")


	nome_colunas = df.columns
	print(f"Nome das colunas: {nome_colunas}")


	tipo_dados = df.dtypes
	print(f"Tipo de dados para cada coluna: {tipo_dados}")


	valores_nulos = df.isnull().sum() / len(df)
	print(f"Proporção de valores nulos por coluna: {valores_nulos}")
    

    duplicatas = df.duplicated().sum()
    print(f"Quantidade de linhas duplicadas: {duplicatas}")

    return valores_nulos
    

def limpeza_dados_inicial(df):

	# Conferindo as características dos dados
	valores_nulos = caracteristicas_dados(df)
    
    # Removendo duplicatas
    print("Removendo duplicatas...")
    df_2 = df.drop_duplicates(keep="first") # Mantém a primeira linha do registro
    print(f"Verificando se ainda há duplicatas: {df_2.duplicated().sum()}")

    # Tratando valores nulos -> Colunas com a partir de 70% dos valores nulos, removo
    print("Tratando colunas com valores nulos...")
    colunas_nulas = valores_nulos[valores_nulos >= 0.70].index # extrai os nomes das colunas
    df_3 = df_2.drop(columns=colunas_nulas)
    print(f"Verificando se ainda há colunas com valores nulos igual ou acima de 70%: {df_3.isnull().sum() / len(df_3)}")

    # Como os dados estão no momento
    print("Como os dados estão no momento:")
    print(df_3.head(20))

    return df_3
    







