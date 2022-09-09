#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:20:09 2022

@author: julioferrer
"""
print("texto explicativo :D")
resposta1=0
perguntas = {
    'pergunta1': {
        'pergunta': 'quanto é 2+2',
        'respostas': {'a':'1','b':'4','c':'5',},
        'resposta_certa':'b',
        },
    'pergunta2': {
        'pergunta': 'quanto é 3*2',
        'respostas': {'a':'4','b':'10','c':'6',},
        'resposta_certa':'c',
        },
     'pergunta3': {
        'pergunta': 'quanto é 1*2',
        'respostas': {'a':'4','b':'2','c':'6',},
        'resposta_certa':'b',
        },
     'pergunta4': {
        'pergunta': 'qual a diferença de 6 e 4 ',
        'respostas': {'a':'4','b':'2','c':'6',},
        'resposta_certa':'b',
        },
     'pergunta5': {
        'pergunta': 'quanto é 2 + 2 ? ',
        'respostas': {'a':'peixe','b':'22','c':'4',},
        'resposta_certa':'c',
        },
    
}
print()


for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print("Respostas: ")
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
        
    resposta=input("Qual sua resposta ?: ")
    
    if resposta == pv['resposta_certa']:
        print("\n você acertou")
        resposta1 += 1
    else:
        print('você errou')
    print()
qnt_perguntas = len(perguntas)
porcentagem_acerto = resposta1 /qnt_perguntas*100

print(f' você acertou {resposta1} respostas.')
print(f'sua porcentagem de acerto foi de {porcentagem_acerto}%')