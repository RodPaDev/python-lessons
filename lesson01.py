## Estou aprender a programar 

## Data Types:

## int : numeros inteiros
## float : numeros, com virgula a ponto preciso
## string : um conjunto de carateis 
## bool : um estado de condicao: true or false
## null : nada (em python é none)
## undefined : nao definido


## def -> nomeDaFuncao -> (paramateros, parametros):
#       codigo..
#       return, pass 

num = 12
floaty = 3.69
string = "foo/"
booly = False
nada = None


## functions

def bar():
    print(string)
    pass

def printAnything(word):
    print(word)
    pass

def onlyPrintCat(word):
    if word == "cat" and word == "gato":
        print(word)
    else:
        print(word + " is not a cat")

def add(a,b):
    result = a + b
    return f"A soma de {a} + {b} é igual a {result}"


## Define a function 'printAnimalSounds' that will take 1 argument representing an animal
# this function will print the sound of the animals
# for example if I give 'dog' as an argument it will print "woof"
# exception if the argument is not a supported animal it will print 'fooooooobar'

# supported animals:
# cat, dog, cow, pig, bird, dolphin