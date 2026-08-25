# Script python que criei para me auxiliar em estudos de estatística descritiva e na análise exploratória dos dados

import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import norm 

# Para variáveis qualitativas
def tabela_frequencia(var):

	frequencia_relativa = var.value_counts()/len(var)

	return pd.DataFrame({
       "Freq. Absoluta": var.value_counts(),
       "Freq. Relativa": frequencia_relativa,
       "Freq. Relativa %": (frequencia_relativa) * 100
    })



# Para variáveis quantitativas
def medidas_tendencia_central(var):
	return{
		"Média": var.mean(),
		"Mediana": var.median(), # Valor central após ordenar os dados
		"Moda": var.mode()[0] # Valor mais frequente
	}

def medidas_dispersao(var):
	return{
		"Amplitude": var.max() - var.min(),
		"Variância": var.var(), # Mede a dispersão em relação à média
		"Desvio padrão": var.std(), # Raiz quadrada da variância
		"Coeficiente de variação": (var.std()/var.mean()) * 100 # Mede a dispersão em relação à média em formato de porcentagem
    }

def medidas_posicao(var):

	q1 = var.quantile(0.25)
	q2 = var.quantile(0.50)
	q3 = var.quantile(0.75)

	iqr  = q3 - q1
	limite_superior = q3 + (1.5 * iqr)
	limite_inferior = q1 - (1.5 * iqr)

	return{
		"Q1": q1,
		"Q2": q2,
		"Q3": q3,
		"Intervalo Interquartil (IQR)": iqr,
		"Limite superior": limite_superior,
		"Limite inferior": limite_inferior,
		"Valores Outliers": var[(var > limite_superior) | (var < limite_inferior)].tolist()
    }





# Probabilidade
# Se as fórmulas de probabilidade que estou usando assumem uma distribuição normal, como eu sei se os meus dados realmente são normais?
# Primeiro devo fazer uma inspeção visual

def inspecao_visual(var):
	var.hist(bins=20)
	var.plot.box()
	plt.show()
	print(f'Média: {var.mean()}')
	print(f'Mediana: {var.median()}')

def z_score(var, valor): # Indica quantos desvios padrões um valor está acima ou abaixo da média

	media = var.mean()
	desvio_padrao = var.std()

	if desvio_padrao == 0:
		return {
			"Z-score": None
		}
	else:
		return {
			"Z-score": (valor - media)/desvio_padrao
		}


# Qual a probabilidade de encontrar um valor menor ou igual a esse Z?
def probabilidade_abaixo(z):
	return norm.cdf(z)

# Qual a probabilidade de encontrar um valor maior ou igual a esse Z?
def probabilidade_acima(z):
	return 1 - norm.cdf(z)

# Qual a probabilidade de encontrar um valor entre dois valores?
def probabilidade_entre(var, valor_min, valor_max):

	media = var.mean()
	desvio_padrao = var.std()

	z_score_min = (valor_min - media)/desvio_padrao
	z_score_max = (valor_max - media)/desvio_padrao

	return norm.cdf(z_score_max) - norm.cdf(z_score_min)
