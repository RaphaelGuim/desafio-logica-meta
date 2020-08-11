#!/usr/bin/env python3

# Um bracket é considerado qualquer um dos seguintes caracteres: (, ), {, }, [ ou ].
# Dois brackets são considerados um par combinado se o bracket de abertura (isto é, (, [ou {) ocorre à esquerda de um
# bracket de fechamento (ou seja,),] ou} do mesmo tipo exato. Existem três tipos de pares de brackets : [], {} e ().
# Um par de brackets correspondente não é balanceado se o de abertura e o de fechamento não corresponderem entre
# si. Por exemplo, {[(])} não é balanceado porque o conteúdo entre {e} não é balanceado. O primeiro bracket inclui o
# de abertura, (, e o segundo inclui um bracket de fechamento desbalanceado,].
# Dado sequencias de caracteres, determine se cada sequência de brackets é balanceada. Se uma string estiver
# balanceada, retorne SIM. Caso contrário, retorne NAO.

# É necessário ter o Python3 instalado

# Para rodar os testes basta abrir o terminal na pasta onde este aquivo se encontra e digitar
# python3 Desafio2.py

# Para testar a função no terminal, basta abrir o shell do python e digitar:
# from Desafio2 import bracket


import unittest 
def bracket(sequence):
    if not sequence:
        return "NAO"
    map_char={'{' :'}','[' :']','(' :')', }    
    stack = [] 
    for letter in sequence:            
        if letter in "{[(" :             
            stack.append(letter)                     
        else:
            if stack:                 
                if map_char[stack.pop()]!= letter:                                
                    return "NAO"
            else:
                return "NAO"
    return "NAO" if stack else "SIM"
                
    
    
class TestBracket(unittest.TestCase):     
             
    def test_example(self):        
        self.assertEqual(bracket('{[(])}'), "NAO")
        
    def test_brackets(self):        
        self.assertEqual(bracket('()'), "SIM")
        self.assertEqual(bracket('[]'), "SIM")
        self.assertEqual(bracket('{}'), "SIM")
        
    def test_brackets_grouped(self):        
        self.assertEqual(bracket('()[]{}'), "SIM")
     
    def test_nested_brackets(self):        
        self.assertEqual(bracket('{[()]}'), "SIM") 
        self.assertEqual(bracket('{{[[({[()]})]]}}'), "SIM")        
        self.assertEqual(bracket('{{[[({[()(){([])}{}[]]})()][]]}}'), "SIM")  
    
    def test_non_brackets(self):        
        self.assertEqual(bracket('{[[()]}'), "NAO") 
        self.assertEqual(bracket('({[[()]}'), "NAO") 
        self.assertEqual(bracket('){[[()]}'), "NAO") 
        self.assertEqual(bracket(')('), "NAO")
        self.assertEqual(bracket('('), "NAO")
        self.assertEqual(bracket('}}}'), "NAO")
    
    def test_others(self):        
        self.assertEqual(bracket('abc'), "NAO") 
        self.assertEqual(bracket('123'), "NAO") 
        self.assertEqual(bracket(''), "NAO") 
    
        
if __name__ == '__main__':
    
    unittest.main()