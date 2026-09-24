import heapq
from cliente import Cliente


class Fila:
    def __init__(self):
        self._clientes = []

    def enqueue(self, cliente: Cliente):
        self._clientes.append(cliente)

    def dequeue(self):
        if self.empty():
            return None
        return self._clientes.pop(0)

    def head(self):
        if self.empty():
            return None
        return self._clientes[0]

    def size(self):
        return len(self._clientes)

    def empty(self):
        return self.size() == 0

    def __str__(self):
        return " | ".join(str(cliente) for cliente in self._clientes)


class FilaCircular:
    def __init__(self, capacidade=5):
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        self.capacidade = capacidade
        self._clientes = [None] * capacidade
        self.front = 0
        self.rear = 0
        self._tamanho = 0

    def enqueue(self, cliente: Cliente):
        if self.full():
            return False
        self._clientes[self.rear] = cliente
        self.rear = (self.rear + 1) % self.capacidade
        self._tamanho += 1
        return True

    def dequeue(self):
        if self.empty():
            return None
        cliente = self._clientes[self.front]
        self._clientes[self.front] = None
        self.front = (self.front + 1) % self.capacidade
        self._tamanho -= 1
        return cliente

    def head(self):
        if self.empty():
            return None
        return self._clientes[self.front]

    def size(self):
        return self._tamanho

    def empty(self):
        return self._tamanho == 0

    def full(self):
        return self._tamanho == self.capacidade

    def estado(self):
        return {
            "front": self.front,
            "rear": self.rear,
            "tamanho": self._tamanho,
            "posicoes": list(self._clientes),
        }

    def __str__(self):
        posicoes = []
        for indice, cliente in enumerate(self._clientes):
            texto = "vazio" if cliente is None else cliente.senha
            posicoes.append(f"[{indice}: {texto}]")
        return " ".join(posicoes)


class FilaPrioridade:
    def __init__(self):
        self._heap = []
        self._contador = 0

    def enqueue(self, cliente: Cliente):
        heapq.heappush(self._heap, (cliente.prioridade, self._contador, cliente))
        self._contador += 1

    def dequeue(self):
        if self.empty():
            return None
        return heapq.heappop(self._heap)[2]

    def head(self):
        if self.empty():
            return None
        return self._heap[0][2]

    def size(self):
        return len(self._heap)

    def empty(self):
        return self.size() == 0

    def __str__(self):
        ordenados = sorted(self._heap)
        return " | ".join(str(item[2]) for item in ordenados)
