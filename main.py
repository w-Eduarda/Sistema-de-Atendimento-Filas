import random

from cliente import Cliente
from filas import Fila, FilaCircular, FilaPrioridade


NOMES = [
    "Ana", "Bruno", "Carla", "Diego", "Elisa", "Fabio", "Gabriela",
    "Hugo", "Iara", "Joao", "Karen", "Lucas", "Marina", "Nicolas",
    "Olivia", "Paulo", "Rafaela", "Sergio", "Tania", "Vitor",
]


def criar_clientes(quantidade=20, semente=42):
    gerador = random.Random(semente)
    clientes = []
    for numero in range(quantidade):
        nome = NOMES[numero % len(NOMES)]
        senha = f"A{numero + 1:02d}"
        prioridade = gerador.randint(1, 3)
        clientes.append(Cliente(nome, senha, prioridade))
    return clientes


def imprimir_clientes(clientes):
    for cliente in clientes:
        print(f"  {cliente}")


def demonstrar_fila_classica(clientes):
    fila = Fila()
    for cliente in clientes:
        fila.enqueue(cliente)
    atendidos = []
    while not fila.empty():
        atendidos.append(fila.dequeue())
    return atendidos


def demonstrar_fila_circular(clientes, capacidade=5):
    fila = FilaCircular(capacidade)
    atendidos = []
    print(f"Capacidade: {capacidade}")
    print(f"Estado inicial: front={fila.front}, rear={fila.rear}")

    for cliente in clientes[:capacidade]:
        fila.enqueue(cliente)
        print(f"Inseriu {cliente.senha}: front={fila.front}, rear={fila.rear} | {fila}")

    while not fila.empty():
        cliente = fila.dequeue()
        atendidos.append(cliente)
        print(f"Removeu {cliente.senha}: front={fila.front}, rear={fila.rear} | {fila}")
        if len(atendidos) == 2:
            novo = clientes[capacidade]
            fila.enqueue(novo)
            print(f"Reutilizou posição com {novo.senha}: front={fila.front}, rear={fila.rear} | {fila}")

    while not fila.empty():
        atendidos.append(fila.dequeue())
    return atendidos


def demonstrar_fila_prioridade(clientes):
    fila = FilaPrioridade()
    for cliente in clientes:
        fila.enqueue(cliente)
    atendidos = []
    while not fila.empty():
        atendidos.append(fila.dequeue())
    return atendidos


def imprimir_ordem(titulo, clientes):
    print(titulo)
    print("  " + " -> ".join(cliente.senha for cliente in clientes))


def executar_simulacao():
    clientes = criar_clientes()
    print("=== DESAFIO FINAL: 20 CLIENTES ===")
    print("\nClientes na ordem de chegada:")
    imprimir_clientes(clientes)

    classica = demonstrar_fila_classica(clientes)
    print()
    imprimir_ordem("Ordem de atendimento - fila clássica (FIFO):", classica)

    print("\nComportamento - fila circular:")
    circular = demonstrar_fila_circular(clientes)

    prioridade = demonstrar_fila_prioridade(clientes)
    print()
    imprimir_ordem("Ordem de atendimento - fila de prioridade:", prioridade)

    print("\nComparação:")
    print("  Fila clássica preserva integralmente a ordem de chegada.")
    print("  Fila circular mantém FIFO e reutiliza posições do vetor.")
    print("  Fila de prioridade atende primeiro os menores valores de prioridade.")
    return clientes, classica, circular, prioridade


def ler_prioridade():
    while True:
        try:
            prioridade = int(input("Prioridade (1-Emergência, 2-Prioritário, 3-Normal): "))
            if prioridade in (1, 2, 3):
                return prioridade
        except ValueError:
            pass
        print("Digite apenas 1, 2 ou 3.")


def menu_interativo():
    fila = FilaPrioridade()
    proxima_senha = 1
    while True:
        print("\n=== MENU DA CENTRAL ===")
        print("1 - Inserir cliente")
        print("2 - Atender próximo cliente")
        print("3 - Consultar próximo cliente")
        print("4 - Visualizar estado da fila")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            prioridade = ler_prioridade()
            cliente = Cliente(nome, f"M{proxima_senha:02d}", prioridade)
            fila.enqueue(cliente)
            proxima_senha += 1
            print(f"Cliente inserido: {cliente}")
        elif opcao == "2":
            cliente = fila.dequeue()
            print("Nenhum cliente aguardando." if cliente is None else f"Atendido: {cliente}")
        elif opcao == "3":
            cliente = fila.head()
            print("Nenhum cliente aguardando." if cliente is None else f"Próximo: {cliente}")
        elif opcao == "4":
            print(f"Clientes aguardando: {fila.size()}")
            print(fila if not fila.empty() else "Fila vazia.")
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar_simulacao()
    # Para testar o menu, descomente a linha sbaixo
    # menu_interativo()
