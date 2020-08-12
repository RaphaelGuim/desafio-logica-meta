#!/usr/bin/env python3

# 04 – QUESTÃO
# Dados n inteiros não negativos representando um mapa de elevação onde a largura de cada barra é 1, calcule quanta água é capaz de reter após a chuva.
# Exemplo:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# É necessário ter o Python3 instalado

# Para rodar os testes basta abrir o terminal na pasta onde este aquivo se encontra e digitar
# python3 Desafio4.py

# Para testar a função no terminal, basta abrir o shell do python e digitar:
# from Desafio4 import water_in_reservoir
import unittest 

def water_in_reservoir(elevation_map):    
    def find_next_bound_idx(begin):       
        lower = 0   
        lower_idx = 0
        initial_elevation = elevation_map[begin]         
        for idx, elevation in enumerate(elevation_map[begin+1:]):
            if elevation > initial_elevation:
                return idx + begin + 1            
            elif elevation >= lower:
                lower = elevation
                lower_idx = idx 
        return lower_idx + begin + 1
    
    def water_in(begin,end):  
            
        area = elevation_map[begin:end]        
        initial_elevation = min( elevation_map[begin],elevation_map[end])
        diffs = map(lambda elevation: initial_elevation - elevation,area) 
        diffs =  filter(lambda elevation: elevation > 0,diffs)          
        return sum(diffs)
    
    index = 0;
    water = []
    while index < len(elevation_map)-1: 
        
        end_idx = find_next_bound_idx(index)        
        if not end_idx:
            break
        water.append(water_in(index,end_idx))  
        index = end_idx   
     
    return sum(water)   

 

class TestWaterInReservoir(unittest.TestCase):     
             
    def test_example(self):        
        self.assertEqual(water_in_reservoir( [0,1,0,2,1,0,1,3,2,1,2,1]) , 6)
    
    def test_basic_reservoirs(self):
        self.assertEqual(water_in_reservoir( [0]), 0)
        self.assertEqual(water_in_reservoir( [1]), 0)
        self.assertEqual(water_in_reservoir( [0,0,0]), 0)
        self.assertEqual(water_in_reservoir( [1,1,1]), 0)
        self.assertEqual(water_in_reservoir( [0,1,1,1,0]), 0)
        self.assertEqual(water_in_reservoir( [0,1,3,1,0]), 0)
        self.assertEqual(water_in_reservoir( [1,0,1]), 1)
        self.assertEqual(water_in_reservoir( [10,0,10]), 10)
        self.assertEqual(water_in_reservoir( [10,0,0,10]), 20)
        
    def teste_reservoirs_combinations(self): 
        self.assertEqual(water_in_reservoir( [1,0,1,1,0,1,1,0,1]), 3)
        self.assertEqual(water_in_reservoir( [10,0,10,10,0,10,10,0,10]), 30)
        self.assertEqual(water_in_reservoir( [3,1,0,2,4,3,2,1,0,3,0,4]), 21)
        
        
    def teste_complex_reservoirs(self): 
        self.assertEqual(water_in_reservoir( [0,1,0,2,4,2,0,0,1,3]), 10)
        self.assertEqual(water_in_reservoir( [0,1,0,1,0,3,0,1]), 3)
        self.assertEqual(water_in_reservoir( [0,1,0,2,4,2,0,0,0,0]), 1)
        self.assertEqual(water_in_reservoir( [1,0,2,1,3,0,2,3,5,0,1,0,2,3,4]), 20)
        self.assertEqual(water_in_reservoir( [5,2,1,0,3,2,0,7,0,1,0,1]), 24)
        self.assertEqual(water_in_reservoir( [0,1,2,3,4,5,4,3,2,1,0]), 0)
        self.assertEqual(water_in_reservoir( [5,4,3,2,1,0,1,2,3,4,5]), 25)
        self.assertEqual(water_in_reservoir( [5,4,3,2,1,4,1,2,3,4,5]), 21)
        self.assertEqual(water_in_reservoir( [5,4,3,2,1,10,1,2,3,4,5]), 20)
        
     
if __name__ == '__main__':
    
    unittest.main()
