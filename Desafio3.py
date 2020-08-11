#!/usr/bin/env python3

# 03 – QUESTÃO
# Digamos que você tenha um array para o qual o elemento i é o preço de uma determinada ação
# no dia i.
# Se você tivesse permissão para concluir no máximo uma transação (ou seja, comprar uma e
# vender uma ação), crie um algoritmo para encontrar o lucro máximo.
# Note que você não pode vender uma ação antes de comprar.
# Exemplo:
# Input: [7,1,5,3,6,4]
# Output: 5 (Comprou no dia 2 (preço igual a 1) e vendeu no dia 5 (preço igual
# a 6), lucro foi de 6 – 1 = 5
# Input: [7,6,4,3,1]
# Output: 0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a
# 0)

# É necessário ter o Python3 instalado

# Para rodar os testes basta abrir o terminal na pasta onde este aquivo se encontra e digitar
# python3 Desafio3.py

# Para testar a função no terminal, basta abrir o shell do python e digitar:
# from Desafio3 import max_Profit

import unittest 

def max_Profit(stocks):
    def find_best(stock_index,stocks):
        actual = stocks[stock_index]
        next_days = stocks[stock_index+1:]
        next_days = filter(lambda num: num>actual,next_days) 
        balances = list(map(lambda day : day - actual,next_days))
        return max(balances) if balances else 0     
        print("oi")
    return max([find_best(stock_index,stocks) for stock_index in range(len(stocks))])

class TestMax_Profit(unittest.TestCase):     
             
    def test_examples(self):        
        self.assertEqual(max_Profit([7,1,5,3,6,4]), 5)
        self.assertEqual(max_Profit([7,6,4,3,1]), 0)
        
    def test_found_max_Profit(self):        
        self.assertEqual(max_Profit([7,3,5,1,2,9]), 8)
        self.assertEqual(max_Profit([7,3,5,4,2,9]), 7)
        self.assertEqual(max_Profit([9,1,3,6,2,7]), 6)
        
    def test_not_found_max_Profit(self):        
        self.assertEqual(max_Profit([4,3,2,1]), 0)
        self.assertEqual(max_Profit([9,7,5,3,2]), 0)
        
if __name__ == '__main__':
    
    unittest.main()