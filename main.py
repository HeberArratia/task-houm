#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pokeapi import *

# First question
def first_question():
    result = []
    pokemon_list = get_all_pokemon(1118)
    for pokemon in pokemon_list:
        name = pokemon['name']
        if 'at' in name and name.count('a') == 2:
            result.append(name)
    return result                

# Second question         
def second_question():
    egg_groups_names = get_egg_groups_name('raichu')
    pokemon_names = []
    for egg_group_name in egg_groups_names:   
        pokemon_names_egg_group = get_pokemon_name_from_egg_group(egg_group_name)
        pokemon_names.extend(pokemon_names_egg_group)
    return list(dict.fromkeys(pokemon_names))    

# Third question
def third_question():
    pokemon_list = get_pokemon_by_type('fighting')  
    widths = []
    for pokemon in pokemon_list:
        widths.append(get_pokemon_weight(pokemon))
    return [max(widths), min(widths)]    

print('***** Question #1 *****')
print(first_question())

print('\n ***** Question #2 *****')
print(second_question())

print('\n ***** Question #3 *****')
print(third_question())