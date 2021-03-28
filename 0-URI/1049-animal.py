palavras = {
    'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'}, 
                   'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}}, 
    
    'invertebrado': {'inseto': {'hematofago': 'pulga', 'herbivoro': 'lagarta'},
                     'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}
    }

op1 = input()
op2 = input()
op3 = input()

print(palavras[op1][op2][op3])