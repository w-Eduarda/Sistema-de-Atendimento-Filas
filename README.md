# fila-atendimento-hands-on

## Identificação

**Aluno:** __________________________________________  
**Disciplina:** ______________________________________  
**Data:** ____/____/________

## Objetivo

Este projeto implementa um sistema inteligente de atendimento em Python. O programa compara três formas de organizar clientes: fila clássica, fila circular e fila de prioridade.

Cada cliente possui nome, senha e prioridade. Os valores de prioridade são 1 para emergência, 2 para atendimento prioritário e 3 para atendimento normal.

## Organização dos arquivos

| Arquivo | Descrição |
|---|---|
| `cliente.py` | Classe `Cliente`, usada para representar os atendimentos. |
| `filas.py` | Classes `Fila`, `FilaCircular` e `FilaPrioridade`. |
| `main.py` | Simulação com 20 clientes e menu interativo opcional. |
| `test_filas.py` | Testes automatizados das operações principais. |
| `simulacao.txt` | Saída registrada da execução do desafio final. |

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python3 main.py
```

O programa cria automaticamente 20 clientes, mostra a ordem de chegada, simula as três estruturas e imprime uma comparação dos resultados.

Para executar os testes:

```bash
python3 -m unittest -v
```

O menu interativo está implementado na função `menu_interativo()` do arquivo `main.py`. Para utilizá-lo, basta comentar a chamada de `executar_simulacao()` e descomentar a chamada de `menu_interativo()` no bloco final do arquivo.

## Explicação das implementações

### Fila clássica

A classe `Fila` utiliza uma lista e segue o princípio FIFO, ou seja, o primeiro cliente inserido é o primeiro cliente atendido. O método `enqueue()` adiciona no final da lista e `dequeue()` remove o primeiro elemento. Também foram implementados `head()`, `size()` e `empty()`.

### Fila circular

A classe `FilaCircular` possui capacidade definida, sendo utilizada com capacidade 5 na simulação. Ela mantém os índices `front` e `rear`, além da quantidade de elementos. Quando o índice `rear` chega ao fim do vetor, ele retorna ao índice zero. Assim, posições liberadas depois de remoções podem ser reutilizadas sem criar uma nova lista.

Quando a fila está cheia, uma nova inserção não é realizada e o método `enqueue()` retorna `False`. Quando há espaço, ele retorna `True`.

### Fila de prioridade

A classe `FilaPrioridade` usa o módulo `heapq`. Cada item inserido no heap possui a estrutura `(prioridade, contador, cliente)`. Como o menor número representa a maior prioridade, clientes de emergência são atendidos antes dos demais. O contador aumenta a cada inserção e garante que clientes com a mesma prioridade mantenham a ordem de chegada.

## Respostas às questões

### Por que a ordem da fila de prioridade pode ser diferente da fila clássica?

A fila clássica considera somente a ordem de chegada: quem chegou primeiro é atendido primeiro. Já a fila de prioridade considera o nível de prioridade antes da ordem de chegada. Por isso, um cliente que chegou depois, mas possui prioridade 1, pode ser atendido antes de clientes que chegaram anteriormente com prioridade 2 ou 3. Entre clientes com a mesma prioridade, este projeto preserva a ordem de chegada usando o contador.

### Em quais situações reais uma fila de prioridade seria mais adequada?

Ela é adequada quando alguns atendimentos não podem esperar o mesmo tempo que os demais. Exemplos são pronto-socorros, chamados de suporte técnico com falha crítica, centrais de emergência, processamento de tarefas urgentes e atendimento de incidentes de segurança. Nesses casos, atender apenas pela ordem de chegada poderia causar riscos ou prejuízos.

### Quais são as vantagens e limitações de uma fila circular?

A principal vantagem é reutilizar as posições liberadas de um vetor, evitando deslocamentos e aproveitando melhor uma capacidade fixa de memória. Ela é eficiente para buffers, impressoras, comunicação de dados e sistemas de atendimento com limite de espera. Como limitação, a capacidade é definida previamente, então a fila não cresce automaticamente. Também é necessário controlar corretamente `front`, `rear` e a quantidade de elementos para diferenciar fila vazia de fila cheia.

### O que acontece ao tentar inserir um elemento em uma fila circular cheia?

A inserção não é realizada. Neste projeto, o método `enqueue()` retorna `False` e o estado da fila permanece inalterado. Essa decisão evita sobrescrever um cliente que ainda não foi atendido.

## Evidências dos testes

Os testes foram executados com:

```bash
python3 -m unittest -v
```

Resultado obtido: **5 testes executados com sucesso**. Os testes verificam a ordem FIFO, consulta do primeiro cliente, tamanho da fila, reutilização de posição na fila circular, comportamento de fila circular cheia e prioridade com desempate pela ordem de chegada.

A saída completa da simulação automática com 20 clientes está registrada no arquivo `simulacao.txt`.

## Comparação final

A fila clássica é a mais simples e justa quando todos os clientes devem ser tratados igualmente. A fila circular apresenta a mesma lógica FIFO, mas trabalha com uma capacidade fixa e reaproveita posições. A fila de prioridade é mais adequada quando a urgência do atendimento é mais importante do que a ordem de chegada.
