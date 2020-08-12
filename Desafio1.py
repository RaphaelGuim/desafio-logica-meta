#!/usr/bin/env python3

# 01 - QUESTÃO
# Dado um array de números inteiros, retorne os índices dos dois números de forma que eles se
# somem a um alvo específico.
# Você pode assumir que cada entrada teria exatamente uma solução, e você não pode usar o
# mesmo elemento duas vezes.
# Exemplo:
# Dado nums = [2, 7, 11, 15], alvo = 9,
# Como nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#É necessário ter o Python3 instalado

# Para rodar os testes basta abrir o terminal na pasta onde este aquivo se encontra e digitar
# python3 Desafio1.py

# Para testar a função no terminal, basta abrir o shell do python e digitar:
# from Desafio1 import find_indexes

import random
import unittest 

def find_indexes(nums,target):   
    for idx,number in enumerate(nums):             
        if number <= target: 
            next_nums = nums[:idx]         
            find = next((num for num in next_nums if num + number == target),False)
            if type(find) == int:             
                return [nums.index(find),idx]        
    return False  
 

class Testfind_indexesFunction(unittest.TestCase):
    
             
    def test_example(self):        
       
        self.assertEqual(find_indexes([0,10],10), [0, 1]) 
        
    def test_target_not_found(self):       
        self.assertEqual(find_indexes([1,2,3,4,5],0), False) 
        self.assertEqual(find_indexes([1,2,3,4,5],1), False) 
        self.assertEqual(find_indexes([1,2,3,4,5],2), False) 
        self.assertEqual(find_indexes([1,2,3,4,7],30), False) 
        
    def test_target_found(self):
        self.assertEqual(find_indexes([0,10],10), [0, 1]) 
        self.assertEqual(find_indexes([10,0],10), [0, 1]) 
        self.assertEqual(find_indexes([1,2,3,4,5],3),[0,1]) 
        self.assertEqual(find_indexes([1,2,3,4,5],4),[0,2]) 
        self.assertEqual(find_indexes([1,2,3,4,5],5),[1,2]) 
        self.assertEqual(find_indexes([1,2,3,4,7],6),[1,3])
        self.assertEqual(find_indexes([9,3,10,1,2],19),[0,2])
        self.assertEqual(find_indexes([15,3,7,1,8,12],16 ),[0,3])
        self.assertEqual(find_indexes([12,0,20,39,73],85 ),  [0,4])
        
    def test_random_case(self):        
        target = 100
        test_list = random.sample(range(1, 200), target)
        answer = find_indexes(test_list,100)         
        if answer: 
            self.assertEqual(test_list[answer[0]]+test_list[answer[1]], target)             
        else:
            self.assertEqual(answer, False)

if __name__ == '__main__':
    
    unittest.main()
         
    
