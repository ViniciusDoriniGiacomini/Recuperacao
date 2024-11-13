# Recuperação

## Exercício 1(Calculadora de IMC)
Este é um simples programa em Python para calcular o Índice de Massa Corporal (IMC) de uma pessoa.
O código solicita ao usuário que insira seu peso e altura, realiza o cálculo do IMC e exibe o resultado.


### Como funciona
O código solicita que o usuário digite seu peso e altura por meio da função `input()`. Em 
seguida, ele converte os valores digitados (que são recebidos como strings) para números de
ponto flutuante usando a função `float()`. O IMC é calculado dividindo o peso pela altura ao quadrado. 
O resultado do cálculo é armazenado na variável `calculaIMC` e, por fim, o IMC é exibido na tela usando a função `print()`.

#### Exemplo de execução

```
Digite seu peso: 70
Digite sua altura: 1.75
IMC:  22.86
```

## Exercício 2(Calculadora Simples)
Este é um programa em Python que funciona como uma calculadora simples. O usuário insere dois números e escolhe uma operação matemática (soma, subtração, multiplicação ou divisão), e o programa realiza o cálculo e exibe o resultado.

### Como funciona
O código pede ao usuário para inserir dois números e um operador matemático (como soma, subtração, multiplicação ou divisão). Ele então verifica qual operador foi inserido utilizando uma estrutura condicional (`if`, `elif`) e executa a operação correspondente entre os dois números, convertendo as entradas de texto para inteiros com a função `int()`. O resultado da operação é mostrado na tela. Caso o operador seja inválido ou não seja reconhecido, o código não possui tratamento de erro explícito, mas ele funciona para os operadores definidos: `+`, `-`, `*` e `/`.

#### Exemplo de execução

```
Digite um número: 10
Digite outro número: 5
Digite o operador (+, -, *, /): +
Resultado: 15
```
