import matplotlib as plt
import numpy as np

#Constantes utilizadas

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
wav = np.arange(1e-9, 3e-6, 1e-9)

#Definindo a funcao

def planck(T):
    '''Esta funcao apresenta como saida o grafico da curva de emissao de um corpo negro de temperatura T. 
	INPUT: Temperatura em Kelvin
	OUTPUT: curva de corpo negro Intensidade[unidade indefinida] vs. comprimento de onda [nm]
	'''
    a=2.0*h*c*c
    b=h*c/(wav*k*T)
    intensity = a/(wav*(np.exp(b)-1.0))
    
    plt.plot(wav,intensity,'g-')
    plt.show()
