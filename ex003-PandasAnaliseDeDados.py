# 1 - Encontre todas as postagens às quais reagiram com um coração
# Empresa: Meta

import pandas as pd

df1 = pd.DataFrame(facebook_reactions)
df2 = pd.DataFrame(facebook_posts)

mascara_booleana1 = facebook_reactions['reaction'] == 'heart'
id_heart = df1[mascara_booleana1]['post_id']

mascara_booleana2 = df2['post_id'].isin(id_heart)
df2[mascara_booleana2]

#------------------------------

# 2 - Encontrando registros atualizados
# Empresa: Microsoft

# Temos uma tabela com funcionários e seus salários; 
# No entanto, alguns registros são antigos e contêm informações de salário desatualizadas. 
# Como não há registro de data, suponha que o salário não diminua com o tempo. 
# Você pode considerar que o salário atual de um funcionário é o maior valor de salário entre seus registros. 
# Se vários registros tiverem o mesmo salário máximo, retorne qualquer um deles. 
# Mostre o ID, primeiro nome, sobrenome, ID do departamento e salário atual. 
# Ordene a lista pelo ID do funcionário em ordem crescente.


df_salarios = pd.DataFrame(ms_employee_salary)

df_salarios.loc[df_salarios.groupby('id')['salary'].idxmax()]

#------------------------------

# 3 - Custo Total dos pedidos
# Empresa: Amazon, Etsy

# Encontre o custo total dos pedidos de cada cliente.
# Mostre o ID do cliente, o primeiro nome e o custo total dos pedidos
# Ordene os registros pelo primeiro nome do cliente em ordem alfabética


df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

total_cost = df_orders.groupby('cust_id')['total_order_cost'].sum()

df_merge = pd.merge(df_customers, total_cost, left_on= 'id',right_on = 'cust_id', how = 'inner')

df_merge[['id','first_name', 'total_order_cost']].sort_values('first_name', ascending=True)


#------------------------------

# 4 - Trabalhadores com os salários mais altos
# Empresa: Amazon, DoorDash

# Uma empresa quer revisar a remuneração apenas dos trabalhadores que têm um cargo oficial registrado,
# já que o pagamento não pode ser corretamente comparado com uma função que não está documentada.
# Encontre os cargos dos trabalhadores com o maior salário entre aqueles que têm um registro correspondente na tabela de cargos.
# Se vários trabalhadores compartilharem o mesmo salário, inclua todos os cargos deles.


worker_df = pd.DataFrame(worker)
title_df = pd.DataFrame(title)

df_merge = pd.merge(worker_df, title_df, left_on='worker_id', right_on='worker_ref_id',how='inner')

mascara_booleana = df_merge['salary'] == df_merge['salary'].max()

highest_salaries = (
    df_merge[mascara_booleana][['worker_title']]
    .rename(columns={'worker_title': 'best_paid_title'})
    .reset_index(drop=True)
)


#------------------------------

# 5 - Salários médios
# Empresa: Salesforce, Glassdoor

# Compare o salário de cada funcionário com a média salarial do departamento correspodente.
# Mostre o departamento, o primeiro nome e o salário dos funcionários juntamente com a média salarial desse departamento.


employee_df = pd.DataFrame(employee)

media_departamento = employee_df.groupby('department')[['salary']].mean().rename(columns={'salary':'mean_salary'})

df_merge = pd.merge(employee_df, media_departamento, on = 'department', how = 'inner')[['department', 'first_name', 'salary', 'mean_salary']]


#------------------------------

# 6 - Calcule a receita total de vendas da Samantha e da Lisa
# Empresa: Salesforce, Amazon, Groupon

# Uma equipe de operações de vendas quer verificar a contribuição de receita combinada de duas das melhores vendedoras.
# Descubra a receita total de vendas gerada pela Samantha e pela Lisa.
# Exiba a receita total de vendas como um único número.


sales_df = pd.DataFrame(sales_performance)

mascara_booleana = (sales_df['salesperson']=='Samantha') | (sales_df['salesperson']=='Lisa')

sales_samantha_lisa = sales_df[mascara_booleana]['sales_revenue'].sum()


#------------------------------

# 7 - Variedade de vinho provadas por 'Roger Voss'
# Empresa: Wine Magazine

# Encontre variedade de vinho provadas por Roger Voss e com um valor na coluna 'region_1'do conjunto de dados.
# Mostre apenas os nomes únicos das variedades.


wine_df = pd.DataFrame(winemag_p2)

mascara_booleana = (wine_df['taster_name'] == 'Roger Voss') & (wine_df['region_1'].notnull())

wine_df[mascara_booleana][['variety']].drop_duplicates()


#------------------------------

# 8 - Hora do maior gasto com gasolina
# Empresa: Lyft

# Encontre a hora da única corrida com o maior custo de gasolina.
# Assuma que apenas uma corrida tem esse valor máximo, então exatamente uma hora é válida.


lyft_rides_df = pd.DataFrame(lyft_rides)

mascara_booleana = lyft_rides_df['gasoline_cost'] == lyft_rides_df['gasoline_cost'].max()

lyft_rides_df[mascara_booleana][['hour']]


#------------------------------

# 9 - Encontre todas as corridas da Lyft que aconteceram em dias chuvosos antes do meio-dia
# Empresa: Lyft


lyft_rides_df = pd.DataFrame(lyft_rides)

mascara_booleana = (lyft_rides_df['weather'] == 'rainy') & (lyft_rides_df['hour'] < 12)

lyft_rides_df[mascara_booleana]


#------------------------------

# 10 - Salários de motoristas do Lyft
# Empresa: Lyft

# Encontre todos os motoristas do lyft que ganham igual ou menos de 30 mil USD ou igual ou mais de 70 mil USD 
# Exiba todos os detalhes relacionados aos registros encontrados.


lyft_drivers_df = pd.DataFrame(lyft_drivers)

mascara_booleana = (lyft_drivers_df['yearly_salary'] <= 30000) | (lyft_drivers_df['yearly_salary'] >= 70000)


lyft_drivers_df[mascara_booleana]


#------------------------------

# 11 - Contagem de aparições de artistas
# Empresa: Spotify

# Uma equipe de análise musical quer identificar quais artistas aparecem com mais frequência nos rankings de músicas do Spotify em todo o mundo.
# Conte o número de vezes que cada artista aparece nos dados de classificação.
# Exiba o nome do artista e o número correspondente de aparições


spotify_df = pd.DataFrame(spotify_worldwide_daily_song_ranking)

spotify_df.groupby('artist')['position'].count().sort_values(ascending=False)


#------------------------------

# 12 - Músicas mais classificadas
# Empresa: Spotify

# Uma equipe de análise de música quer ver quais músicas dominam as paradas ao atingir o topo dos rankings diários por região
# Encontre músicas que tenham ficado na posição número 1 pelo menos uma vez.
# Conte cada dia que uma música esteve em primeiro lugar em uma determinada região como uma ocorrência separada.
# Por exemplo: uma música que chega ao #1 em cinco países no mesmo dia conta como 5.


spotify_df = pd.DataFrame(spotify_worldwide_daily_song_ranking)

mascara_booleana = spotify_df['position'] == 1
spotify_df[mascara_booleana].groupby('trackname')['stream_date'].count().sort_values(ascending=False)


#------------------------------

# 13 - Lista de eventos olímpicos por idade
# Empresa: ESPN

# Encontre as idades mais baixas, médias e mais altas dos atletas em todas as olimpíadas.
# DICA: Se um atleta participou de mais de uma modalidade em uma mesma edição dos jogos olímpicos,
# considere-o como um atleta separado, não é necessário remover esses casos especiais.

olympics_df = pd.DataFrame(olympics_athletes_events)


idade_min = olympics_df['age'].min()
idade_media = olympics_df['age'].mean()
idade_maxima = olympics_df['age'].max()

resultado = pd.DataFrame({
    'min': [idade_min],
    'mean': [idade_media],
    'max': [idade_maxima]
})

resultado