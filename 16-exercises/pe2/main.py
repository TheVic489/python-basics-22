"""
Exercici 2:

- Fes un programa que mostri seqüències aleatòries d'ADN a una pàgina html.
- Les seqüències han de tenir només les lletres A, T, C o G
  i tenir longitud d'entre 100 i 120 bases.
- Per generar la pàgina html, utilitzeu Jinja.
- A la pàgina html les seqüències han d'estar en línies de màxim 60 lletres.
- El programa només rep un paràmetre: el número de seqüències a generar.
- El programa ha de rebre el número de seqüències des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

"""
# Nom: Victor Piñana Cortés
# Ex : 2
from pathlib import Path
import random
import engine

def get_random_adn_seq(seq_len: int) -> str:
    '''
    Inuput: lenght of the sequence
    Randomly generates a str of sequence'''
    bases_list:      list[str] = ['A','T','C','G']
    adn_seq_list:    list[str] = []
 
    for i in range(seq_len): 

        base: str = random.choice(bases_list)        
        adn_seq_list.append(base)

    adn_seq = ''.join(adn_seq_list)

    return adn_seq


def cut_adn_seq(adn_seq:str) -> list[str]:
    '''Take adn squence string and cut for each 60 '''
    x = 60
    cuted_adn_seq =[adn_seq[y-x:y] 
                    for y in range(x, len(adn_seq)+x,x)]
    print(cuted_adn_seq)
    return cuted_adn_seq

def create_html(cuted_adn_seq: list[str], 
                num_of_seq:    int, 
                html_template: str) -> str:

    vars_dict: dict = {'sequence':cuted_adn_seq, "num_of_sequences": num_of_seq}
    html_seq:   str = engine.fill_template_str(html_template, vars_dict)

    return html_seq
 
 #No tengo tiempo, me 

#Main     
adn_seq:       str       = get_random_adn_seq(180)
cuted_adn_seq: list[str] = cut_adn_seq(adn_seq)
html_seq:       str      = create_html(cuted_adn_seq, 3,'template.html')