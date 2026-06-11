# Atividade de Testes Unitários com IA

## Aluno

Edson Mateus Gonçalves

---

## Uso de IA para geração de cenários de teste

### Função escolhida

```python
def dividir(a, b):
    return a / b
```

---

## Prompt utilizado

Atue como um professor de Teste de Software.

Tenho a seguinte função Python:

```python
def dividir(a, b):
    return a / b
```

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

---

## Cenários sugeridos pela IA

| ID | Cenário | Entrada | Resultado Esperado | Tipo |
|----|----------|----------|-------------------|------|
| T01 | Divisão exata | dividir(10, 2) | 5 | Caso normal |
| T02 | Divisão decimal | dividir(5, 2) | 2.5 | Caso normal |
| T03 | Divisão com número negativo | dividir(-10, 2) | -5 | Caso normal |
| T04 | Zero dividido por número | dividir(0, 5) | 0 | Caso de borda |
| T05 | Divisão por zero | dividir(10, 0) | ZeroDivisionError | Caso de erro |

---

## Análise dos cenários

Todos os cenários sugeridos pela IA foram aceitos, pois representam comportamentos importantes da função `dividir(a, b)`.

Os casos normais verificam divisões exatas, divisões com resultado decimal e divisões envolvendo números negativos.

O caso de borda verifica o comportamento da função quando o numerador é zero.

O caso de erro verifica a divisão por zero, situação que gera a exceção `ZeroDivisionError` em Python.

Nenhum cenário precisou ser removido ou alterado.

---

## Código final dos testes

```python
import unittest
from calculadora import dividir


class TestCalculadora(unittest.TestCase):

    def test_divisao_exata(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_decimal(self):
        self.assertEqual(dividir(5, 2), 2.5)

    def test_divisao_com_negativo(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_zero_dividido_por_numero(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()
```

---

## Resultado da execução

Comando utilizado:

```bash
python -m unittest discover
```

Saída obtida:

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---
