# Curso Python
Cada projeto em python deve ser criado em um ambiente virtual (.venv). Python é uma linguagem de tipagem dinâmica, o tipo de dado é inferido na atribuição.

### Comentários
Comentário de várias linhas utilize 3 aspas duplas para abrir/fechar o comentário.

Comentário de uma linha utilize cerquilha ou hashtag

### PEP8 - Boas práticas
- Nomeie as Classes em Camel Case.
  - Sintaxe: CalculadoraCientifica.
- Métodos, funções e variáveis em Lower Case.
  - Sintaxe: soma ou soma_dois.
- Indentação deve ter 4 espaços em branco. Não utilize tab.
- Separar métodos, funções com 2 linhas em branco.
- Imports devem ser em linhas separadas, ou seja, cada importação em uma linha.
- Imports de classes de um mesmo pacote podem separar por vírgula.
- Imports devem ficar no topo do arquivo py e após de comentários se estiver no topo.
- Finalize os blocos de instruções com uma linha em branco.

### DIR e HELP
O dir() exibe todos os atributos e funções / métodos para determinado tipo de dado ou variável.
```python
dir("texto")
```
O help() exibe a documentação de como utilizar os atributos ou propriedades disponíveis para determinado tipo de dado 
ou variável.

```python
help("texto".lower)
```

### Entrada de dados do usuário

```python
# entrada de dados
nome = input()
name = input("Qual seu nome? ")
```

### Saida de dados
```python

# imprimir
nome = input("Qual o seu nome? ")

# Saída de desses dados. Versão 2x.

print('seja bem vindo, %s' % nome)
idade = int(input("Qual a sua idade? "))
print('%s você tem %s anos' % (nome, idade))

# Saída de dados. Versão 3x
print('Seja bem vindo, {0}'.format(nome))

# Saída de dados. A partir da versão 3.6
print(f'Seja bem vindo, {nome}')
```

### Builtins - Funções reservadas da linguagem
Para exibir as funções reservadas podemos utilizar o _dir()_

```python
# A saída será todas as funções disponíveis. Entre elas o input
dir(__builtins__)
```

### Tipos de dados
Para identificar o tipo de dado utiliza-se o método _type()_

- Integer
	- Multiplicação
      - Sintaxe: 2 * 2
	- Divisão.
      - Sintaxe: 5 / 2 # o resultado é do tipo real
	- Divisão:
      - Sintaxe: 5 // 2 # o resultado é do tipo inteiro
	- Exponenciação.
      - Sintaxe: 2**2
	- Módulo.
      - Sintaxe: 5%2
- Float
    - São números Reais e decimais.
	- Utilize ponto como separador.
      - Sintaxe: 1.44
- Complex
	- Números complexos em _python_ pode ser representados acrescentando a letra j
    - Sintaxe: 5j
- Boolean
    - Sintaxe: True, False
- String
    - Alguns métodos: slice, split, upper, lower, nome[0::4], nome[5::15], nome[::-1]

### Escopo de variáveis
- Global
    - Acessível dentro do escopo do arquivo
- Local
    - Acessível dentro do escopo do bloco de código


# OPERADORES LÓGICOS

### Operadores lógicos
- not
  - Operador unário
- is
  - Operador unário
- or
  - Operador binário
- and
  - Operador binário

# CONDIÇÃO IF, ELSE, ELIF

### Estrutura condicionais
```python
idade = 18
if idade >= 18:
    print("Acesso autorizado")
elif idade < 18:
    print("Acesso não autorizado")
else:
    print("Isso foi só uma demonstração de uso do bloco IF,ELFI e ELSE")
    print("Na verdade nunca vai cair nessa condição")

```

# LOOPs

#### Estrutura de repetição
As estrutura de repetição (loop) podem ser aplicados em:
- String: nome = 'Fabio Ribeiro'
- List -> listas = [1,3,5,7,9]
- Range -> Intervalos = range(1,10)

### FOR

```python
# for -> 
nome = 'Fabio Ribeiro'

for letra in nome:
	print(letra)

# for -> index, 
# em string utilizar enumerate
for valor in nome:
	print(valor)

for index, letra in nome:
	print(f'A letra {letra} está na posição {index}')

# ex.: com range
qnt = int(input('Entre com u número de 1 a 100? '))

for num in range(1, qnt):
	print(num)

```

##### Enumerate
Retorna um objeto do tipo tupla

### WHILE

```python
numero = 1
while numero < 10:
	print(numero + 1)


resposta = ''
while resposta != 'sim':
	resposta = input('Você tem certeza que quer sair? ')


```

#### Break
Usado para sair de loops

```python
# FOR
for i in range(1,10):
	if i == 6:
		break
	print(i)


# WHILE
while True:
	comando = input("Digite q para sair")
	if comando == 'q':
		break

```

### Range
Gera sequências numéricas.

```python
# valor de inicio
for i in range(10):
	print(i)


# valor de inicio, valor de parada
for i in range(2, 10):
	print(i)


# valor de inicio, valor de parada, passo (valor)
for i in range(1, 10, 2):
	print(i)

# contagem regressiva
for i in range(10, 0, -1):
	print(i)



```

# COLLECTIONS - Coleções
### LIST - Listas
Também conhecida com Array, Vetor ou Matriz. É dinâmico e aceita qualquer tipo de dado.

As listas em _Python_ são representadas por colchetes: []
Sintaxe: lista = [] ou lista = list()

Algumas funções para trabalhar com coleções
- join
- extends
- append
- slice
- index
- copy - gera uma cópia nova
- sum
- max
- min
- len

```python
# exemplos
lista1 = [1,2,3,4,5]
lista2 = ['F','a','b','i','o']
lista3 = list(range(1,6))
lista4 = list('Fabio')

# Verificar se existe um determinado valor na lista
if 8 in lista3:
	print("Encontrado")
else:
	print("Não encontrado")

# adicionar valor na lista 
# append()
lista1.append(6)

#adicionar múltiplos valores na lista
lista1.extend([6,7,8])
```

#### Tuple - Tuplas
As tuplas em _Python_ são representadas por parenteses: (). As tuplas são imutáveis e toda operação em uma tupla gera 
uma nova tupla.

```python
# ex: 1
tupla1 = (1,2,3)

# ex: 2
tupla2 = 1,2,3

# ex: 3 com 1 elemento
tupla3 = (4,)

# ex: 4 com 1 elemento
tupla4 = 4,

# ex: 5 gerar um tupla

tupla5 = tuple(range(11))
```

##### Desempacotamento

```python
tupla = ('Fabio', 'Ribeiro')

nome, sobrenome = tupla
```


### Dict - Dicionários
Dicionários são conhecidos como Mapas é uma coleção do tipo chave/valor.

Dicionário é representado por chaves {} e chave/valor devem ser separados por dois pontos {'br':'Brasil'}

Formas para criação de dicionários
```python
# mais comum
paises = {'br':'Brasil', 'eua':'Estados unidos', 'py':'Paraguai'}

# outra
paises2 = dict(br='Brasil', eua='Estados unidos', py='Paraguai')
```

O acesso ao valor via chave pode ser usando a sintaxe: paises['br']

```python
paises = {'br':'Brasil', 'eua':'Estados unidos', 'py':'Paraguai'}
print(paises['br'])
# output: Brasil

# a chave não existe
print(paises['ru'])
# output: exception error
```

IMPORTANTE: Para acesso ao valor o uso recomendado é paises.get('br')

```python
paises = {'br':'Brasil', 'eua':'Estados unidos', 'py':'Paraguai'}
print(paises.get('br'))
# output: Brasil

# a chave não existe
print(paises.get('ru'))
# output: None
```

Adicionar elementos
```python
novo = {'ar':'Argentina'}

paises = {'br':'Brasil', 'eua':'Estados unidos', 'py':'Paraguai'}

paises.update(novo)

# ou
paises.update({'ar':'Argentina'})
```

Recursos disponíveis para dicionário
- {}.fromkeys()
- {}.keys()
- {}.values()
- {}.items()


### Conjuntos - Sets
Teoria de conjuntos da matemática. Em _Python_ os conjuntos são chamados de _Sets_.

Os conjuntos _Sets_ são representados por chaves {} e só armazena valores. 

Diferença entre Conjuntos (Sets) e Dicionários/Mapas (Dict) em Python:
- Dict tem chave/valor.
- Sets tem somente valor.

- Sets não possuem valores duplicados.
- Sets não podem ser ordenados.
- Sets não tem índice.

Definindo conjuntos (sets)

```python
# exemplo de uso 
# mais comum
conj = {12,3,4,4,5,6,7}
# output: 12,3,4,6,7

# exemplo de uso
# conj2 = set({1,2,3,4,3,2,5,7,6})
# print(conj2)
# output: 1,2,3,4,5,7,6

# adicionar
conj.add(11)

# remover - exemplo 1
conj.remove(3)
# Caso o valor não exista retornará um KeyError

# remover - exemplo 2 ( uso recomendado )
conj.discard(5)

# Shallow copy
novo = conj

# Deep copy
novo2 = conj.copy()

```

##### Métodos matemáticos da Teoria dos conjuntos

Dado 2 conjuntos: Estudantes de curso Python e Java

```python
curso_py = {'Allan', 'Silva', 'Denise', 'Paulo', 'Fabio'}
curso_ja = {'Fabio', 'Mariana', 'Denise', 'Paulo', 'Claudio'}

# Gere um conjunto com estudantes únicos
# Union (recomendado)
estudante = curso_ja.union(curso_py)

# Union usando pipe
estudante2 = curso_ja | curso_py


# Gere um conjunto com estudantes que estão em ambos cursos
# Intersection (recomendado)
estudante3 = curso_ja.intersection(curso_py)

# Intersection usando &
estudante4 = curso_ja & curso_py

# Gere um conjunto com estudantes que não estão no curso de Java
# Difference
estudantes_java = curso_ja.difference(curso_py)

# Gere um conjunto com estudantes que não estão no curso de Python
# Difference
estudante_python = curso_py.difference(curso_ja)

```

### Collections -> High Performance Container Datatypes

#### Módulo Counter
Recebe um inteirável como parâmetro e cria um objeto Counter. Ele cria uma chave do elemento e o valor é a quantidade de ocorrências encontradas.

Para usar o Counter é necessário importá-lo.

```python
#import
from collections import Counter

lista = ['Allan', 'Silva', 'Denise', 'Paulo', 'Fabio', 'Fabio', 'Mariana', 'Denise', 'Paulo', 'Claudio']
res = Counter(lista)
print(res)


# exemplo de encontrar o top x ocorrências
texto = """"
A inteligência artificial (de sigla: IA; do inglês: artificial intelligence, de sigla: AI) é um campo de estudo 
multidisciplinar que abrange varias áreas do conhecimento.[1][2] É também um conjunto de novas tecnologias que 
permitem aos aparelhos smart executarem várias funções avançadas de modo quase autônomo,[2][3] representando um marco
histórico na computação moderna.[3] Embora seu desenvolvimento tenha avançado mais na ciência da computação, sua 
abordagem interdisciplinar envolve contribuições de diversas disciplina
"""
palavras = texto.split()
res = Counter(palavras)

# função para o top x
res.most_common(5)
# output: Será as 5 palavras com mais ocorrências
```


#### Módulo Default Dict
Ao criar um dicionário utilizando o _Default Dict_ deve-se informar um valor padrão.

Para utilizar o _Default Dict_ é necessário importá-lo.
```python
from collections import defaultdict

dicionario = defaultdict(lambda: 'Padrão')

dicionario['curso'] = "Python"

print(dicionario)
print(dicionario['curso'])
print(dicionario)
print(dicionario['outro'])
print(dicionario)
```


#### Módulo Ordered dict
Em um dicionário a ordem de inserção dos elementos não é considerada. 
Para garantir a ordem utilizamos o _Ordered Dict_.

Para uso do _Ordered dict_ é necessário importá-lo.

```python
# ex: dicionário, ordem não considerada
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = { 'c':3, 'a': 1, 'b': 2}

print(dict1 == dict2)
# output: True
# ex: OrderedDict, ordem é considerada
# import
from collections import OrderedDict

odict1 = OrderedDict({'a':1, 'b':2, 'c':3})
odict2 = OrderedDict({ 'c':3, 'a': 1, 'b': 2})
# output: False
```

#### Named Tuple
É uma tupla nomeada.

É necessário importar para usar.

Formas de usar o _Named Tuple_
```python
from collections import namedtuple

# declaração 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# declaração 2
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# declaração 3
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando a Named Tuple
toto = cachorro(idade=2, raca='Chow-Chow', nome='Toto')

print(toto)

# Acessando os valores, forma 1
print(toto[0])
print(toto[1])
print(toto[2])

# Acessando os valores através da chave
print(toto.idade)
print(toto.raca)
print(toto.nome)

# Identificando o índice de um determinado valor
print(toto.index('Chow-Chow'))

# Contando quantas ocorrências de um determinado valor
print(toto.count('Chow-Chow'))

```
#### Deque
Podemos considerar o _Deque_ como uma lista de alta desempenho.

É necessário importar para usar.

```python
from collections import deque

# criar um deque
deq = deque('Fabio')
print(deq)

# Adiciona um elemento no final da lista
deq.append('R')

# Adiciona um elemento no inicio da lista
deq.appendleft('F')


# Remover um elemento do final da lista e retorna
deq.pop()

# Remover um elemento do início da lista e retorna
deq.popleft()
```

### Funções
Funções ou métodos são pequenos blocos de código que realizam tarefas específicas.

```python
# Definição da função sem parâmetros
def nome():
    print("oi")

# Definição da função com parâmetro
def sobrenome(sobrenome):
    print('Oi %s', sobrenome)

# isso é a chamada da função passando o argumento
print(sobrenome("Ribeiro"))

# Definição de funções padrões
def exponencial(num, potencia=2):
    print(num ** potencia)

## Se o argumento para o parâmetro potencia não for passado a função usará o valor padrão.
# Exemplo:
print(exponencial(2))

# Exemplo 2:
print(exponencial(2, 3))

```

#### Docstrings
O uso do Docstring é utilizado para documentar as funções e nortear os demais desenvolvedores.

Para acessar a documentação utilizamos o  _help()_
```python
# Exemplo

def saudacao():
    """Uma função simples que retorna um Oi"""
    return "Oi"

print(saudacao())

help(saudacao)

# Ou
print(saudacao.__doc__)
```

#### *args
O *args é usado em funções para permitir que um número variável de argumentos seja passado para a função. Quando você 
usa *args na definição de uma função, ele coleta os argumentos adicionais fornecidos à função em uma tupla. Isso é útil
quando você não sabe antecipadamente quantos argumentos serão passados para a função.. Lembre-se que tuplas são imutáveis.

```python
# Declarando o *args
def soma_numero(*args):
   print(args)
   # somando todos os números
   return sum(args)

# Exemplo de chamada e argumentos ilimitados
print(soma_numero())
print(soma_numero(1,2,4,5))
print(soma_numero(1,2,4))
print(soma_numero(1,2,4,5,6,7,8))
print(soma_numero(1,2))


# Caso utilize uma lista, use o desempacotamento
# Lembrando como funciona o desempacotamento
nums = [1,2,3,4] # lista

# Desempacotamento
num1, num2, num3, num4 = nums

# Exemplo utilizando função
def soma(*args):
    return sum(args)

numeros = [1,2,3]
print(soma(numeros))
# output: TypeError: unsupported operand type(s) for +: 'int' and 'list'

# Desempacotamento automático
print(soma(*numeros))
# output: 6

## IMPORTANTE: O desempacotamento funciona com as coleções List, Tuple e Sets. 
# Dicionário não funciona. É outra abordagem.
```

#### **kwargs
é usado para permitir que uma função aceite um número variável de argumentos nomeados (ou argumentos de palavra-chave). 
Quando você usa **kwargs na definição de uma função, ele coleta todos os argumentos nomeados adicionais fornecidos à 
função em um dicionário. Isso é útil quando você não sabe antecipadamente quais e quantos argumentos nomeados serão 
passados para a função.

```python
# Exemplo de uso
def imprimir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Exemplo de uso
imprimir_informacoes(nome="João", idade=30, cidade="São Paulo")
```
##### IMPORTANTE:
Ordem de definição de parâmetros de funções e métodos:
- Parâmetros obrigatórios
- *args
- Parâmetros default
- **kwargs

```python
def funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'Parâmetros obrigatórios: idade {idade} e nome {nome}')
    print(f'Parâmetros do Args: {args}')
    print(f'Parâmetros default: {solteiro}') 
    print(f'Parâmetros do Kwargs: {kwargs}')
```
### List Comprehension
Utilizado para gerar uma nova lista a partir de dados processados de outro iterável.

Sintaxe de uso de List Comprehension: [ dado for in iterável ]

```python
# Uso
numeros = [1,2,3,4,5]
res = [numero * 10 for numero in numeros]

print(res)


# Estrutura condicionais dentro do for
pares = [numero for numero in numeros if not numero % 2 == 0]


# Estrutura condicional fora do for
result = [numero * 10 if numero % 2 == 0 else numero for numero in numeros]

```
### Listas Aninhadas
São array unidimensionais (Array/Vetores) e multidimensionais (Matriz)

Sintaxe: [[1,2,3], [4,5,6]]

```python
```

### Dict Comprehension
Utilizado para gerar um novo dicionário a partir de dados processados de outro iterável.

```python
numeros = {'a':1, 'b':2, 'c':3, 'd':4}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

```

### Set Comprehension
Utilizado para gerar um novo (Set) conjunto a partir de dados processados de outro iterável.

```python
numeros = { numero for numero in range(1,10)}

print(numeros)

quadrados = { quadrado ** 2 for quadrado in range(1,10)}

# Gerando um dicionário a partir de um conjunto
dicionario = { x: x ** 3 for x in range(1,10)}

```

### Generator express
Tuple Comprehension são chamadas de Generator express.

```python
gerador = (x * 2 for x in range(1000))

```

### Expressões Lambdas
Lambda é uma função anônima. Para usar o lambda é necessário usar a palavra reservada.

```python
# Função comum
def soma(x):
    3 * x + 1

print(soma(4))

# A mesma função utilizando lambda
calc = lambda x: 3 * x + 1

# como usar lambda
print(calc(4))


### Mais sobre Lambda
# sem parâmetro
saudacao = lambda: 'Seja bem vindo'
# com mais parâmetros
nome_completo = lambda nome, sobrenome: f'{nome.strip().title()} {sobrenome.strip().title()}'

# usando Sort e Lambda para ordenar pelo sobrenome
autores = ['Joaquim Silva', 'Maria Gusman Alvim', 'Marta Maria', 'Suegon Sunami Daemon']

print(autores.sort(key=lambda sobrenome: sobrenome.split(' ').title()))

```
##### Função Quadrática - Solução usando lambda
Relembrando a função quadrática: f(x) = a * x ** 2 + b * x + c

```python
def quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

fx = quadratica(2, 3, -5)

print(fx(0))
print(fx(2))
print(fx(1))

print(quadratica(2,5,7)(2))
```

### Maps
É uma função que recebe dois parâmetros, uma função e um iterável, e retorna um _Map Object_.

```python
import math

raios  = [5, 2, 0.4, 8, 3.4]
# função
def area(r):
    return math.pi * (r ** 2)

# map
areas = map(area, raios)
print(areas)
print(list(areas))

# MAP com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
```

### Filter
Utilizado para filtrar dados de uma coleção. É uma função que recebe dois parâmetros, uma função e um iterável, 
e retorna um _Filter Object_

Filter verificar se a função que foi passada retorna True ou False para filtrar e retornar dados.

```python
# calculo de média
valores = [1.3, 0.5, 2.5, 4.1, 5.7, -0.3, 9.8]

import statistics
# media = sum(valores) / len(valores) # método convencional
media = statistics.mean(valores)

print(media)

# Utilizando o Filter
res = filter(lambda valor: valor > media, valores)

print(list(res))

# Como remover dados em branco/vazios
# 
paises = ['', '', 'Brasil', ' ', 'China', 'Russia', '', 'Eua', 'Marrocos', 'Israel', '', 'Japão']
print(paises)

# Opção 1: None
res = filter(None, paises)
print(list(res))

# opção 2: lambda
res1 = filter(lambda pais: len(pais) > 0, paises)
print(list(res1))

# opção 3: lambda + for
res2 = filter(lambda pais: pais != '' and pais != ' ', paises)
print(list(res2))

```

### Reduce
Para usar _reduce_ é necessário importá-la do módulo _functools_

 É uma função que recebe dois parâmetros, uma função com dois parâmetros e um iterável.

```python
# Reduce para multiplicar os dados de uma lista
dados = [1,2,3,4,5,6,7,8,9]

from functools import reduce

res = reduce(lambda x, y: x * y, dados)
print(res)
```

### Any - Algum
Retorna True se apenas um elemento do iterável for verdadeiros e False para vazio.
```python
print(any([0,1,2,3,4])) # True
# output: True 

print(any([0, False, {}, (), []]))
# output: False 
```

### All - Todos ou vazio
Retorna True se todos os elementos do iterável são verdadeiros ou vazio.

```python
print(all([0,1,2,3]))
# output: False porque o zero é falso.

print(all([0,1,2,3]))
# output: True
```

### Sorted
Aplicável em qualquer iterável, serve para ordenar. Retorna uma nova lista, independente do iterável.

```python
lista = [8, 1, 7, 2]
# Menor para o Maior
print(sorted(lista))

# Maior para o Menor
print(sorted(lista, reverse=True))

```

### Min e Max
- Max retorna o maior valor em um iterável, dois valores ou dois elementos. 
- Min retorna o menor valor em um iterável, dois valores ou dois elementos.

```python
valores = range(1000)
print(max(valores))
print(min(valores))
```

- Min e Max tem a opção key que recebe uma função.

```python
usuarios = [
    {'nome': 'Claybom Cremoso', 'idade': 54},
    {'nome': 'Jao Mao de Pilao', 'idade': 18},
    {'nome': 'Doritos Gostoso', 'idade': 37},
    {'nome': 'Charlie Charp', 'idade': 13},
    {'nome': 'Agora ou Nunca', 'idade': 54},
]

print(max(usuarios, key=lambda user: user['idade']))
print(min(usuarios, key=lambda user: user['idade']))
```

### Reversed
O _reversed()_ retorna uma lista chamada de _List Reverse Iterator_, esse retorno pode ser convertido em lista e tupla.

```python
lista = [1,2,3,4,5,6,7,8]

print(list(reversed(lista)))
```
### Zip
O _zip()_ cria um iterável (Zip Object) dada 2 ou mais iteráveis retornando pares a partir da combinação da posição.
O zip pode ser convertido em lista, tupla, conjunto ou dicionário.

```python
lista1 = [1,2,3]
lista2 = [3,4,5]
zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))
print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))
```

## Erros comuns
- IndexError
- ValueError
- SyntaxError
- KeyError
- NameError
- AttributeError
- IndentationError

### Raise
O _raise_ lança uma exceção pré-definida pelo usuário. 

A Sintaxe é: raise TipoErro('Mensagem')
```python
# Lançando uma exceção do tipo ValueError
# raise ValueError("Valor incorreto!")

# exemplo de uso
def colorir(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto informado não é válido, passe uma string')

    if type(cor) is not str:
        raise TypeError('A cor informada não é válida, passe uma string')

colorir('test', 4)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "<stdin>", line 3, in colorir
# TypeError: O texto deve ser uma string
```

### Try/Except
Usamos try/except para tratar bloco de código que possam gerar uma falha, prevenindo que o sistema pare.

O _try_ é utilizado para trecho de código problemático e o _except_ o que deve ser feito em caso de falha.

```python
# try/except simples
try:
    area()
except:
    print("Houve uma falha no processo")
# output: Houve uma falha no processo

# Conhecendo o tipo de erro, definimos no except
try:
    area()
except NameError:
    print("Houve uma falha no processo")
# Output: Houve uma falha no processo

# Capturando o erro quando sabemos o tipo
try:
    area()
except NameError as err:
    print(f"Houve uma falha no processo: {err}")
# Output: Houve uma falha no processo: name 'area' is not defined
```

### Try, except, else e finally
Toda entrada de dados no sistema deve ser tratada.

O try tenta executar um trecho de código, caso de alguma falha cai no except. O else só é executado caso o try seja 
bem-sucedido. O finally sempre é executado independentemente se houve exceção ou não. Geralmente é utilizado para fechar
conexão com o banco de dados.

```python
# caso de uso
try:
    num = int(input("informe um número: "))
except ValueError:
    print("você não digitou um número")
else:
    print(f'O número digitado foi {num}')
finally:
    print('O finally vai ser executado de quaquer jeito')

```

### Debugando código com PDB - Python debugging
Usar o breakpoint da ferramenta Pycharm.

Caso não utilize a ferramente é possível utilizar o breakpoint nativo do python.

Atalhos da linha de comando:
- (l) lista aonde está no código
- (n) vá para próxima linha
- (p) imprime variável
- (c) continua e finaliza o debugging

Exemplo de uso
```python
nome = 'Fabio'
sobrenome = 'Ribeiro'
nome_completo = f'{nome} {sobrenome}'
breakpoint()
curso = 'Programação Python'
estudante = f'{nome_completo} faz o curso {curso}'
print(estudante)
```

### Módulos
Módulo em Python é todo arquivo e podemos importar métodos específicos.

Para usar módulo externos devemos instalar. Podemos encontrar todos os pacotes de terceiros no site oficial: 
https://pypi.org

Para instalar utilizamos o gerenciador de pacotes PIP
````shell
pip install colorama
````

### Pacotes
Pacote Python é um diretório.

Nas versões 2x é obrigatório o arquivo chamado __init__.py, nas versões 3x não é obrigatório mas é usado para manter
a compatibilidade.

### Dunder Name e Dunder Main
Dunder é Doble underscore ou duplo sublinhado.

- Dunder Name: __name__ 
- Dunder Main: __main__

Quando um arquivo python é executado ele implicitamente passa para o __name__ como valor __main__ isso para evitar 
conflitos. E quando o arquivo é importado o __name__ recebe o nome do arquivo como valor.

```python
# Verificação comum em python
if __name__ == '__main__':
    """código omitido"""
```


## Trabalhando com Arquivos
Passos básicos para trabalhar com arquivos.

- Abrir o arquivo
- Trabalhar no arquivo
- Fechar o arquivo

### Leitura de arquivos
Para leitura do conteúdo de um arquivo usamos a função integrada open(), essa função retorna um _io.TextIOWrapper.

Para escrever ou ler dados em arquivos é necessário ter a devida permissão do sistema operacional.

```python
# abre o arquivo 
arquivo = open('arquivo.txt')

# O tipo do arquivo é _io.TextIOWrapper
type(arquivo)

"""arquivo.read() lê todo o arquivo"""
arquivo.read()

"""Limite de caracteres"""
arquivo.read(50)

"""arquivo.readline() lê o arquivo linha a linha"""
arquivo.readline()

"""arquivo.readlines() lê todo arquivo e cria uma lista unificando todas as linhas"""
arquivo.readlines()

"""arquivo.close() fechar o arquivo"""
arquivo.close()

"""arquivo.closed verifica se o arquivo está fechado o retorno é um booleano"""
t = arquivo.closed
```
### seek()
O seek() movimenta o cursor dentro do arquivo.

### Bloco With
O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco.

O With abre e fecha o arquivo/conexão automaticamente.

```python
with open('arquivo.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
```

### Escrever em arquivos
Para escrever em um arquivo precisamos abrir. Precisa passar o modo de escrita.

Se o arquivo não existir é criado no sistema operacional. E para escrever utilizamos a função write().

Importante saber que a função write() recebe como argumento uma string.

Abrindo um arquivo utilizando o modo de escrita 'w', se o arquivo não existir será criado e caso exista ele é apagado 
e um novo arquivo é criado para o conteúdo. Portanto, o conteúdo é perdido.

```python
with open('novo.txt', 'w') as escrever:
    escrever.write('Novo conteúdo escrito com sucesso!')
    escrever.write('Novo2 conteúdo escrito com sucesso!')
    escrever.write('Novo3 conteúdo escrito com sucesso!')
```

### Modos de arquivos
- O 'r' abre para leitura - modo padrão.
- O 'w' abre para escrita.
- O 'x' abre para escrita somente se o arquivo não existir, caso exista lança uma except FileExistsError.
- O 'a' abre para escrita  adicionando o conteúdo no final do arquivo.
- O 'a+' abre para leitura e escrita.

### StringIO
Podemos criar um arquivo em memória e efetuar a leitura quantas vezes for necessário.

Para utilizar é necessário fazer o import.

```python
from io import StringIO

mensagem = "Teste de escrita temporária e na memória"

arquivo2 = StringIO(mensagem)

print(arquivo2.read())
```

### Sistemas de arquivo
Para fazer manipulação de arquivos do sistema operacional, precisamos importar o módulo _os_.

```python
import os

# caminho absoluto
os.getcwd()

# mudar de diretório
os.chdir('..')

# verificar se o diretório atual é absoluto ou relativo
os.path.isabs('/home/projetos')

# Detalhes do sistema operacional
os.uname()

# juntar diretórios
os.path.join(os.getcwd(), 'teste')

# listar arquivos e diretórios
os.listdir()

# listar arquivos e diretórios com mais detalhes
scanner = os.scandir()
arquivos = list(scanner)
print(dir(arquivos))
print(arquivos[0].stat())

scanner.close()

# verificar se um arquivo ou diretório existe
os.path.exists('teste.txt') # arquivo
os.path.exists('teste') # diretório


# criar arquivo definindo o caminho do path
os.mknod('~/Downloads/teste.txt')

# criar diretório, esse comando cria um a um
os.mkdir('teste')

# criar vários diretórios
os.makedirs('teste/teste2')

# verificar se o diretório jé existe ante de criar vários diretórios
os.makedirs('teste/teste2', exist_ok=True)

# Renomear arquivos ou diretórios
os.rename('teste', 'novo')
os.rename('teste.txt', 'novo.txt')

# Remover arquivos
os.remove('texto.txt')

# Remover diretórios
```

### Iterators e Iterable
Iterators é um objeto que pode ser iterado, sendo um elemento por vez quando usamos a função next().

Iterable é um objeto que ira retornar um iterator quando a função iter() for chamada.

```python
nome = "Teste"
next(nome) # vai gerar uma exceção.

nome = iter(nome)
next(nome)
```

### Generators
São iterators e utiliza o _yield_ e o retorno é um generator.

Como o Yield é de múltiplo retorno ele sempre aguarda o next() para continuar a execução.

```python
# 
def contador(val_max):
    count = 1
    while count <= val_max:
        yield count
        count = count + 1
        
#
gen = contador(10)

#
print(next(gen))

print("Teste")

for i in gen:
    print(i)

# se tranformar em uma lista já temos todos os valores
gen2 = list(gen)
```

### Teste de mémoria com Generators

Sequência de Fibonacci 1,1,3,5,8,13...

```python
# Função padrão
def fibo(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# essa função alocou aproximadamente 450MB na memória
fibo(100_000)

# Generators

def fibo_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# essa generator alocou aproximadamente 3MB na memória
fibo_gen(100_000)
```

### Teste de velocidade

```python
import time

# Generator express
gen_start = time.time()
print(sum(num for num in range(1_000_000)))
gen_end = time.time()

# List Comprehension
list_start = time.time()
print(sum(num for num in range(1_000_00)))
list_end = time.time()

print(f'Tempo de execução do Generator express: {gen_end - gen_start}')
print(f'Tempo de execução do List Comprehension:  {list_end - list_start}')
```

### Funções de maior grandeza | HOF - Higher Order Function
Exemplo de definição de função
```python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# HOF
def calcular(a, b, funcao):
    return funcao(a, b)


print(calcular(4,3,somar))
print(calcular(4,3,subtrair))
print(calcular(4,3,multiplicar))
print(calcular(4,3,dividir))
```

### Funções aninhadas - Nested Function
Exemplo de função aninhada

```python
# a função choice escolhe uma opção aleatoriamente
from random import choice

def cumprimento(nome):
    def humor():
        return choice(('Você está bem?', 'Trabalhou hoje?', 'Está descansada?'))
    return nome + humor()

print(cumprimento('Fabio'))
```
### Decoradores - Decorators
Decorators são funções, envolvem outras funções, são Higher Order Function, tem sintaxe própria usando o "@".

```python
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudar(nome):
    return f'Olá eu sou {nome}'

saudar("Fabio")

```

### Decorator Pattern
Esse padrão de projeto utiliza o args e kwargs.

Caso haja a necessidade, pode ser definido argumentos para o decorators.

```python
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudar(nome):
    return f'Olá eu sou {nome}'

print(saudar("Fabio"))

@gritar
def pedir(principal, acompanhamento):
    return f'Olá eu gostaria de {principal} acompanhado de {acompanhamento}'

print(pedir('Picanha', 'Fritas'))
```

### Preservando Metadata com Wraps


# DICAS
Na IDE PYCHARM podemos desabilitar o spelling que sublinha as palavras em português.

# Benchmark  
Medir quantos bytes um dado está ocupando na mémoria.

```python
from sys import getsizeof

lista = getsizeof([ x * 10 for x in range(1000)])
conjunto = getsizeof(( x * 10 for x in range(1000)))
dicionario = getsizeof({x: x * 10 for x in range(1000)})
gerador = getsizeof(x * 10 for x in range(1000))

print(f'List Comprehension:  {lista} bytes')
print(f'Set Comprehension:  {conjunto} bytes')
print(f'Dict Comprehension:  {dicionario} bytes')
print(f'Generator Express:  {gerador} bytes')

```

# BIBLIOTECAS
Para trabalhar com estatística utilize: statistics.

