# Pandas - Data da atividade do Churro - City of Los Angeles
# Encontre a data da inspeção e a categoria de risco (pe_description) das instalações chamadas 'STREET CHURROS' que receberam uma pontuação abaixo de 95.

import pandas as pd

df = pd.DataFrame(los_angeles_restaurant_health_inspections)
instalacao = df[(df['facility_name'] == 'STREET CHURROS') & (df['score'] < 95)]
instalacao[['activity_date', 'pe_description']]

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Pandas - Usuários exclusivos por mês - Microsoft/Apple/Dell
# Escreva uma consulta que retorne o número de usuários únicos por cliente para cada mês.
# Suponha que todos os eventos ocorram no mesmo ano, então o mês precisa estar na saída como um número de 1 a 12.

import pandas as pandas

df = pd.DataFrame(fact_events)
agrupamento = df.groupby(['client_id', pd.to_datetime(df['time_id']).dt.month])['user_id'].nunique()
agrupamento

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Pandas - Número de remessas por mês - Amazon
# Escreva uma consulta que calculará o número de remessas por mês.
# A chave exclusiva para uma remessa é uma combinação de shipment_id e sub_id.
# Produza o year_month no formato YYYY-MM e o número de remessas naquele mês.

import pandas as pd 

df = pd.DataFrame(amazon_shipment)
df['chave_exclusiva_remessa'] = df['shipment_id'].astype(str) + '-' + df['sub_id'].astype(str)
df['ano_mes'] = pd.to_datetime(df['shipment_date']).dt.to_period('M')
agrupamento = df.groupby(['ano_mes'])['chave_exclusiva_remessa'].nunique()

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Pandas - Altos rendimentos em departamentos de apoio - Uber/Spotify/Amazon
# A equipe de RH está revisando pacotes de remuneração para funcionários em funções de suporte.
# Eles querem identificar pessoas com altos rendimentos nos departamentos de RH e Administração para um estudo de avaliação comparativa salarial
# Encontre todos os funcionários que ganham mais de US$ 80.000 e trabalham no departamento de RH ou administrativo.
# Retorne first_name, last_name, department e salary.

import pandas as pd 

df = pd.DataFrame(techcorp_workforce)

df[(df['salary'] > 80000) & ((df['department'] == 'HR') | (df['department'] == 'Admin'))][['first_name', 'last_name', 'department', 'salary']]

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Pandas - Usuários com números de telefone ausentes - Linkedin/Airbnb/Meta
# A equipe de produtos está lançando um novo recurso de notificação do WhatsApp e precisa identificar usuários que ainda não forneceram seus números.
# Esses usuários receberão um prompt para adicionar suas informações de contato.
# Encontre todos os usuários que não forneceram um número de telefone.
# Retorne o user_id e user_name

import pandas as pd 

df = pd.DataFrame(fintech_app_users)

df[df['phone_number'].isnull()][['user_id', 'user_name']]

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Pandas - Completude de informações de contato - Salesforce/Amazon/Shopify
# A equipe de qualidade de dados está auditando os registros dos funcionários para avaliar a integridade das informações de contato.
# Calcule e retorne a proporção de funcionários que possuem número NULL de telefone.

import pandas as pd 

df = pd.DataFrame(techcorp_workforce)


total_funcionarios = df['id'].nunique()
telefones_nulos = df[df['phone_number'].isnull()]['id'].nunique()
proporcao = telefones_nulos/total_funcionarios
proporcao
