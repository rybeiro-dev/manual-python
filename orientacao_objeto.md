# Python Orientado a Objeto
Programação orientada a objetos nada mais é do que uma representação de objeto real.

## Classe
A classe seria o modelo para esse objeto. 

E uma classe pode conter atributos/propriedades que representam as características 
de um objeto e os métodos/funções ou ações que representam os comportamentos do objeto. 

Pelos atributos conseguimos representar computacionalmente os estados de um objeto.

Supondo que nossa Classe/Objeto seja um Lâmpada, alguns atributos seriam: voltagem, 
cor, luminosidade. E um método seria ligar/desligar.

Criar uma classe com a palavra reservada ```class``` seguido do nome do objeto que por 
convenção é camel case ```ContaCorrente```.

A palavra ```pass``` é usado para um bloco de código que ainda não foi implementado.

```python
class Pessoa:
    pass

```

## Atributos ou propriedades
Atributos/propriedades que representam as características de um objeto. E pelos
atributos conseguimos representar computacionalmente os estados de um objeto.

A visibilidade dos atributos pode ser públicos ou privados. No caso de um atributo
privado utilizamos duplo underline ```self.__senha``` e atributo público ```self.senha```

Os atributos podem ser divididos em 3 grupos:
- Atributos de instância.
  - São atributos declarados no método construtor.
- Atributos de classe.
- Atributos dinâmicos.

#### Atributos de instância
O método construtor é representado por ```__init__(self)```
```python
class Lampada:
    def __init__(self, volts, cor):
        self.__volts = volts
        self.__cor = cor
```
#### Atributos de classe
Atributos de classe são declarados diretamente na classe, fora de qualquer método.

```python
class Produto:
    imposto = 0.95

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

prod1 = Produto('Playstation 4', 'Vídeo Game', 2300)
print(prod1.valor)
```

#### Atributos dinâmicos - o uso nõa é comum
Atributos dinâmicos são atributos de instância que podem ser criados em tempo de execução.

```python
class Produto:
    imposto = 0.95
    contador = 0
    
    def __init__(self, name, description, value):
        self.id = Produto.contador + 1
        self.name = name
        self.description = description
        self.value = (value * Produto.imposto)
        Produto.contador = self.id

prod1 = Produto('Playstation 4', 'Vídeo Game', 2300)

# atrituto criado dinâmicamente para esse objeto
# atributos dinâmicos estão disponíveis apenas nessa instância

prod1.peso = '2kg'

print(prod1)
```

## Métodos
Métodos/Funções representam os comportamentos do objeto.
São ações que o objeto pode realizar no sistema.

### Métodos de instância

Os métodos de instância sempre tem a referência do objeto.

```python
class Produto:
    imposto = 0.95
    contador = 0
    
    def __init__(self, name, description, value):
        self.id = Produto.contador + 1
        self.name = name
        self.description = description
        self.value = (value * Produto.imposto)
        Produto.contador = self.id
        
    def desconto(self, percentual):
        """retorna o valor do produto já aplicando o desconto"""
        return (self.value * (100 - percentual)) / 100
    

prod1 = Produto('Playstation 4', 'Vídeo Game', 2300)
prod1.desconto(50)
print(prod1)
```

### Métodos de classe
Quando não precisamos ter acesso a atributos de instância utilizamos os 
métodos de classe, e usamos *decorator* ```@classmethod``` 
Métodos de classe são conhecidos como métodos estáticos.

```python
class Usuario:
    @classmethod
    def acesso(cls):
        print(f'Nome da classe: {cls}')
```

#### Métodos privados 
São declarados com duplo underline.

```python
from random import random
def __gerar_numero():
    print(random())
```

#### Métodos estáticos
São declarados com *decorator* ```@staticmethod```

```python
@staticmethod
def definir():
    return 'URX344'
```

## Objetos
Objetos são instância da classe, ou seja, um objeto real representado
computacionalmente.

```python
class Lampada:
    def __init__(self, volts, cor):
        self.__volts = volts
        self.__cor = cor
```

## Abstração e Encapsulamento
Abstração é o ato de expor apenas os dados relevantes de uma classe, ou seja,
atributos e métodos públicos.

Encapsulamento é o ato de dar visibilidade para métodos ou atributos.

## Herança
Herança é quando temos propriedades e métodos comuns entre classes. A ideia é reaproveitar código.

Caso de uso:
```python
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda
        
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
        
```

#### Overwritten - Sobrescrita
```python
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome} sua renda é de {self.__renda}'
```

### Propriedades
Métodos *getter* e *setter* utilizamos decorators 

```@property``` para *getters* e ```@limite.setter``` para *setter*

Caso de uso:
```python
class Conta:
    contador = 1
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, novo):
        self.__limite = novo
        

c1 = Conta('Fabio', 3000, 5000)

# acesso getter saldo
print(c1.saldo)

# definindo novo valor via setter
c1.limite = 7000
print(c1)
```

É possível criar métodos como propriedade, caso de uso:
```python
class Conta:
    contador = 1
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, novo):
        self.__limite = novo
        
    @property
    def saldo_total(self):
      return self.__saldo + self.__limite
        

c1 = Conta('Fabio', 3000, 5000)

# acesso getter saldo
print(c1.saldo)

# definindo novo valor via setter
c1.limite = 7000
print(c1)

print(c1.saldo_total)

```

### Método super()
O método *super()* é uma referência da classe Pai ou super classe.

### Herança multipla
Herança multipla possibilita a ter acesso aos métodos e atributos de todas as classes herdadas.

**Multi-derivação direta**
```python
class Base:
    pass

class Base1:
    pass

class Base2:
    pass

# Herança multipla direta
class HerancaDireta(Base, Base1, Base2):
    pass

```

**Multi-derivação indireta**
```python
class Base3:
    pass

class Base4(Base3):
    pass

class Base5(Base4):
    pass

# herança indireta tem acesso a todos os métodos e atributos das 
# classes Base5, Base4 e Base3
class HerancaIndireta(Base5):
    pass
```

### MRO - Method Resolucion Order



# Dicas
Para criptografar senhas, por exemplo podemos utilizar o pacote ```pip install passlib```

Como usar:
```python
from passlib.hash import pbkdf2_sha256 as crypt

class Usuario:
    def __init__(self):
        pass

    def cadastro(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = crypt.hash(senha, round(200000), salt_size=16)

    def validar_senha(self, senha):
        if crypt.verify(senha):
            return True
        return False

```

O tipo de criptografia usada é sha256. 
- O método ```hash(palavra, rounds=int, salt_size=int)```
- **palavra** é string a ser criptografada
- **rounds=200000** é um número inteiro que a palavra será embaralhada para gerar.
- **salt_size=16** é o tamanho da parte que será juntada.

