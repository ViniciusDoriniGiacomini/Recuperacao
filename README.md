# Recuperação

## Exercício 1 (Calculadora de IMC)
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

## Exercício 2 (Calculadora Simples)
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
## Exercício 3 (Identificador de Números Primos)
Este programa em Python solicita ao usuário um número limite e, em seguida, exibe todos os números primos de 1 até esse limite. Um número é considerado primo se for maior que 1 e não for divisível por nenhum outro número além de 1 e ele mesmo.

### Como funciona
Este código solicita ao usuário um número limite e, em seguida, chama a função `mostrar_primos()` para exibir todos os números primos de 1 até esse limite. A função percorre os números de 1 até o limite, verificando se cada número é primo. Para isso, ela verifica se o número é divisível por algum número entre 2 e ele mesmo (excluindo o próprio número), usando um loop aninhado. Se o número não for divisível por nenhum outro número, ele é considerado primo e é impresso na tela. Se for divisível, o loop é interrompido e o próximo número é verificado.

#### Exemplo de execução

```
Digite o número limite: 20
2 é primo
3 é primo
5 é primo
7 é primo
11 é primo
13 é primo
17 é primo
19 é primo
```
## Exercício 4 (Pirâmide Numérica)
Este programa em Python cria uma pirâmide numérica com base no número inserido pelo usuário. A pirâmide pode ser gerada de forma crescente ou decrescente, dependendo da configuração escolhida.

### Como funciona
Este código define uma função chamada `piramide()` que imprime uma pirâmide numérica com base no número fornecido pelo usuário. A função recebe dois parâmetros: `n`, que é a altura da pirâmide, e `crescente`, que determina se a pirâmide será impressa de forma crescente (do 1 até `n`) ou decrescente (de `n` até 1). A função utiliza um loop `for` para iterar de 1 até `n` (ou de `n` até 1, caso `crescente` seja `False`), e, em cada iteração, imprime uma linha com números de 1 até o valor atual da iteração, formando assim uma pirâmide. O número limite `n` é obtido a partir da entrada do usuário e passado para a função.

#### Exemplo de execução

```
Digite um número: 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
## Exercício 5 (Análise de Conjuntos de Clientes)
Este programa em Python realiza uma análise de dois conjuntos de clientes, verificando a interseção, diferença e união entre eles, e calcula a porcentagem de clientes que estão presentes em apenas um dos conjuntos, em relação ao total de clientes únicos.

### Como funciona
Este código trabalha com dois conjuntos de clientes, `clientes_A` e `clientes_B`, e realiza operações para comparar e calcular informações sobre os clientes presentes em um ou ambos os conjuntos. Primeiro, ele encontra os clientes que estão em ambos os conjuntos (`clientes_em_ambos`), os que estão apenas no conjunto `clientes_A` (`clientes_apenas_A`), os que estão em apenas um dos conjuntos (`clientes_apenas_um_conjunto`), e todos os clientes únicos presentes nos dois conjuntos (`clientes_unicos`). Em seguida, calcula a porcentagem de clientes que estão em apenas um dos conjuntos, em relação ao total de clientes únicos, e imprime os resultados. As operações de conjuntos como `&`, `-`, `^` e `|` são usadas para interseção, diferença, diferença simétrica e união, respectivamente.

#### Exemplo de execução

```
Clientes em ambos os conjuntos: {'Cesar', 'Anderson'}
Clientes apenas em clientes_A: {'Alice', 'Bob'}
Clientes em apenas um dos conjuntos: {'Bruno', 'Gabriel', 'Alice', 'Bob'}
Porcentagem de clientes únicos: 50.0 %
```
