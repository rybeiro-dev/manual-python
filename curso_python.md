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

#### Args
O *args é um parâmetro utilizado em uma função. E colocamos os valores extras informados com tipo tupla(). Lembre-se
que tuplas são imutáveis.

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

## IMPORTANTE: O desempacotamento funciona com as coleções List, Tuple e Sets. Dicionário não funciona.
```

```python
```

```python
```

```python
```

```python
```

### Lambda
_Lambda_ são funções sem nome que com parâmetro opcional e retorno obrigatório.


#### DICAS
Na IDE PYCHARM podemos desabilitar o spelling que sublinha as palavras em português
