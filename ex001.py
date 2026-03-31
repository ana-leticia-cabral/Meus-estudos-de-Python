
# Sabe-se que um número da forma n^3 é igual a soma de n ímpares consecutivos.

# Exemplo: 1^3= 1, 2^3= 3+5, 3^3= 7+9+11, 4^3= 13+15+17+19,...

# Dado m, determine os ímpares consecutivos cuja soma é igual a n^3 para n assumindo valores de 1 a m.



impares_consecutivos = int(input('Digite até qual número você deseja que n assuma, para o cálculo de n³, mostrando como resultado a soma de ímpares consecutivos: '))

primeiro_impar = 1

for m in range (1, impares_consecutivos + 1, 1 ):
    
    impares = [primeiro_impar + 2 * i for i in range(m)]
    
    string_exibicao = ' + '.join(str(n) for n in impares)
    
    print(f'{m}³ = {string_exibicao}')
    
    primeiro_impar = primeiro_impar + 2 * m