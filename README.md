# eqBolleanTable

Python code that turns boolean equations into truth tables. // Código em python que converte equações booleanas em tabelas verdade.

O desenvolvimento desse método foi baseado em 3 etapas. A primeira etapa foi a de encontrar equações que relacionassem, de forma consisente, os diferentes parâmetros que são implicitamente definidos a partir da simples definição da quantidade de variávis (únicas) presentes na equação requerida. Por exemplo, a relação "2**(len(a)//2 + 1)"; que define, a partir da quantidade de variáveis únicas, quantas linhas estarão presentes para cada coluna.

A segunda etapa foi a percepcão de a estrutura fundamental para estruturação (e inputação) a serem rodados para cada variável única seguia uma sequêncial ordinal, mas no valor em binário de 0 até (n-1); sendo n a quantidade de linhas. Outra percepção importante foi a de que, apesar dessa correlação direta, era necessário uma formatação posterior quanto a extensão de zeros a esquerda necessários serem adicionados para manter a correlação fundamental das tabelas verdades.

A terceira etapa foi a de entendimento de que não era necessário lidar com os operadores inputados na parte de modelagem. Esses seriam a parte fixa, modificando apenas os valores dos operandos dentro dessa estrutura fixa. Além disso, foi importante utilizar o método replace pois, dessa forma, foi possibilitada a definição de variáveis repetidas apenas a partir da iteração sobre a primeira aparição dessa variável no input original.

Desensolvi esse método a partir de cálculos manuais por indução (etapa 1), e a partir da adaptação da minha lógica primeira para os métodos lógicos da linguagem de programação em questão (python).

:D

The development of this method was based on 3 steps. The first one was that of finding equations that relationates, consistently, the different parameters that are implicitly defined by the amount of (unique) variables that are present in the inputted equation. For example, the relation "2**(len(a)//2 + 1)"; which defines, from the amount of unique variables, how many lines each column will hold.

The second step was the perception that the fundamental structure for structuration (and imputation) that are to be defined to each variable follow an ordinal sequence, but on binary ranging from 0 to (n-1); n beeing the amount of lines. Another insightful perception was that of, besides this straigthforward correlation, it was necessary to execute a formatation as for the amount of 0s to be added to the left side of the binary number in order to keep the said fundamental correlation inside the truth tables.

The third step was that of understanding that it was unnecessary to deal with the inputted operators for the molding process. Those were defined to be the static part, only modifying the values of the operands inside those static structures. Besides that, it was important to utilize the "replace" method thus, this way, it turned out to be possible the definition of repeated variables by only iterating through the first appearance of that variable.

I developed this method from manual calculus using induction (first step), and from adaptation of my logical understaning to the logical working of the programing language in question(python).
