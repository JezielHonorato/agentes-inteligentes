# agentes-inteligentes
IMD3001 - Introdução à Inteligência Artificial

Disciplina cursada durante meu bacharelado em Tecnologia da Informação. 

O estudo de *Agentes Inteligentes* é a base da Inteligência Artificial moderna, que pode ser compreendida essencialmente como a ciência do design de agentes. Estudar esses sistemas nos ensina a projetar softwares ou robôs capazes de perceber seus ambientes através de sensores e agir de forma autônoma por meio de atuadores. Ao focar na construção de um **agente racional** — aquele que sempre busca tomar a ação que maximiza a sua medida de desempenho esperada — aprendemos um conjunto de princípios de design universais aplicáveis a qualquer ambiente imaginável. Desde carros autônomos navegando em rodovias até sistemas virtuais de diagnóstico médico dominar a estrutura dos agentes nos permite desenvolver soluções robustas que não apenas reagem aos dados, mas que planejam, otimizam recursos e aprendem continuamente para se adaptar a problemas complexos e incertos no mundo real.

Um agente pode ser compreendido como qualquer entidade que percebe o seu ambiente por meio de sensores e age sobre esse ambiente por meio de atuadores. Matematicamente, o comportamento de um agente é descrito pela **função do agente**, que mapeia sequências de percepções para ações:

$$
\text{agent}: P^* \rightarrow A
$$

em que $P^*$ representa o conjunto de todas as sequências possíveis de percepções (ou seja, o histórico completo de tudo o que o agente já percebeu até o momento) e $A$ representa o conjunto de ações possíveis. É fundamental distinguir a *função do agente*, que é uma descrição matemática abstrata, do **programa do agente**, que é a implementação concreta dessa função rodando dentro de um sistema físico ou computacional (a arquitetura).

Em vez de perguntar apenas se o agente "funciona", a Inteligência Artificial adota uma abordagem baseada no consequencialismo: nós avaliamos o comportamento de um agente pelas consequências de suas ações. Quando um agente atua, ele faz com que o ambiente passe por uma sequência de estados; se essa sequência for desejável, o agente teve um bom desempenho.

A partir dessa medida, definimos um **agente racional** como aquele que, para cada sequência de percepções, escolhe a ação que tem a expectativa de maximizar a sua medida de desempenho. Como regra geral de design, a medida de desempenho deve ser definida de acordo com o que você *realmente deseja que seja alcançado no ambiente*, e não de acordo com a forma como você acha que o agente deveria se comportar.

## Agentes

### Agentes baseados em tabela.

Os agentes baseados em tabela agem de modo que suas percepções são armazenadas em sequencia de modo que sua proxima decisão ira depender da situação listada na tabela.

Todas as possiveis situações deverão estar listadas na tabela, ou seja, o numero de linhas da minha tabela exponencialmente a depender de quais modos o ambiente pode ser alterado
[`table_agent`](table_agent.py)

### Agentes Reflexivos.

Os agentes baseados em tabela agem de modo que suas percepções são armazenadas em sequencia de modo que sua proxima decisão ira depender da situação listada na tabela.

Todas as possiveis situações deverão estar listadas na tabela, ou seja, o numero de linhas da minha tabela exponencialmente a depender de quais modos o ambiente pode ser alterado
[`table_agent`](table_agent.py)

### Agentes baseados em Modelo.

Os agentes baseados em tabela agem de modo que suas percepções são armazenadas em sequencia de modo que sua proxima decisão ira depender da situação listada na tabela.

Todas as possiveis situações deverão estar listadas na tabela, ou seja, o numero de linhas da minha tabela exponencialmente a depender de quais modos o ambiente pode ser alterado
[`table_agent`](table_agent.py)



Fontes:
- Stuart Russell and Peter Norvig. Artificial Intelligence: A Modern Approach. 
- Aulas praticas e teóricas.
