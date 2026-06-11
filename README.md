# Engenharia de Software - Teste Unitário com Python e Uso de IA

## Aluno

**Edson Mateus Gonçalves**

---

# Parte 1 - Aula Prática: Teste Unitário com Python e PyUnit

## Objetivo

O objetivo desta atividade foi aprender a criar e executar testes unitários utilizando Python e o módulo `unittest` (PyUnit), aplicando os conceitos de teste automatizado em funções simples de uma calculadora.

---

## Estrutura do Projeto

```text
engenharia-software-testes/
│
├── calculadora.py
├── test_calculadora.py
└── README.md
```

---

## Funções Implementadas

No arquivo `calculadora.py` foram implementadas as seguintes funções:

- somar(a, b)
- subtrair(a, b)
- multiplicar(a, b)
- dividir(a, b)
- potencia(a, b)
- calcular_media(lista)

### Código das Funções

```python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def calcular_media(lista):
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia")
    return sum(lista) / len(lista)
```

---

## Testes Implementados

Foram criados testes para verificar:

### Soma
- Soma de números positivos
- Soma com zero
- Soma de números negativos

### Subtração
- Subtração simples
- Resultado negativo
- Subtração com zero

### Multiplicação
- Multiplicação simples
- Multiplicação por zero
- Multiplicação com números negativos

### Divisão
- Divisão exata
- Divisão decimal
- Divisão por zero

### Potência
- Expoente positivo
- Expoente zero
- Valores maiores

### Média
- Lista com números inteiros
- Lista com números decimais
- Lista com apenas um número
- Lista vazia (ValueError)

---

## Execução dos Testes

Comando utilizado:

```bash
python -m unittest discover
```

Resultado obtido:

```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

Todos os testes foram executados com sucesso.

---

## Conceitos Aprendidos

Durante a atividade foram praticados os seguintes conceitos:

- Teste de Software
- Teste Unitário
- PyUnit (unittest)
- Assertions
- Tratamento de Exceções
- Automação de Testes
- Organização de Projetos Python
- Git e GitHub

---

## Conclusão

A atividade permitiu compreender como criar testes unitários em Python utilizando o módulo unittest. Os testes ajudaram a verificar automaticamente o comportamento esperado das funções implementadas, aumentando a confiabilidade do código e facilitando futuras manutenções.

---

# Parte 2 - Uso de IA para Geração de Cenários de Teste

## Função Escolhida

```python
def dividir(a, b):
    return a / b
```

---

## Prompt Utilizado

```text
Atue como um professor de Teste de Software.

Tenho a seguinte função Python:

def dividir(a, b):
    return a / b

Quero criar testes unitários usando unittest.

Liste cenários de teste para essa função, incluindo:

- divisão exata;
- divisão com resultado decimal;
- divisão de número negativo;
- divisão de zero por outro número;
- divisão por zero.

Para cada cenário, informe:

- nome do cenário;
- entrada;
- resultado esperado;
- tipo do cenário: caso normal, caso de borda ou caso de erro.

Não gere código ainda.
```

---

## Cenários Sugeridos pela IA

| ID | Cenário | Entrada | Resultado Esperado | Tipo |
|----|----------|----------|-------------------|------|
| T01 | Divisão exata | dividir(10, 2) | 5 | Caso normal |
| T02 | Divisão decimal | dividir(5, 2) | 2.5 | Caso normal |
| T03 | Divisão com número negativo | dividir(-10, 2) | -5 | Caso normal |
| T04 | Zero dividido por número | dividir(0, 5) | 0 | Caso de borda |
| T05 | Divisão por zero | dividir(10, 0) | ZeroDivisionError | Caso de erro |

---

## Análise dos Cenários

Todos os cenários sugeridos pela IA foram aceitos, pois representam comportamentos importantes da função `dividir(a, b)`.

Os casos normais verificam divisões exatas, divisões com resultado decimal e divisões envolvendo números negativos.

O caso de borda verifica o comportamento da função quando o numerador é zero.

O caso de erro verifica a divisão por zero, situação que gera a exceção `ZeroDivisionError` em Python.

Nenhum cenário precisou ser removido ou alterado.

---

## Código Final dos Testes

```python
def test_dividir(self):
    self.assertEqual(dividir(10, 2), 5)
    self.assertEqual(dividir(9, 3), 3)
    self.assertEqual(dividir(5, 2), 2.5)

def test_dividir_por_zero(self):
    with self.assertRaises(ZeroDivisionError):
        dividir(10, 0)
```

---

## Resultado da Execução

Comando utilizado:

```bash
python -m unittest discover
```

Saída obtida:

```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
