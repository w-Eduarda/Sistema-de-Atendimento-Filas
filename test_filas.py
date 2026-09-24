import unittest

from cliente import Cliente
from filas import Fila, FilaCircular, FilaPrioridade


class TestFila(unittest.TestCase):
    def test_ordem_fifo(self):
        fila = Fila()
        clientes = [Cliente("Ana", "A1", 3), Cliente("Bruno", "A2", 1)]
        for cliente in clientes:
            fila.enqueue(cliente)
        self.assertIs(fila.dequeue(), clientes[0])
        self.assertIs(fila.dequeue(), clientes[1])
        self.assertTrue(fila.empty())

    def test_consulta_e_tamanho(self):
        fila = Fila()
        cliente = Cliente("Carla", "A3", 2)
        fila.enqueue(cliente)
        self.assertIs(fila.head(), cliente)
        self.assertEqual(fila.size(), 1)


class TestFilaCircular(unittest.TestCase):
    def test_reutilizacao_de_posicao(self):
        fila = FilaCircular(3)
        clientes = [Cliente("A", "A1", 3), Cliente("B", "A2", 2), Cliente("C", "A3", 1)]
        for cliente in clientes:
            self.assertTrue(fila.enqueue(cliente))
        self.assertTrue(fila.full())
        self.assertIs(fila.dequeue(), clientes[0])
        novo = Cliente("D", "A4", 3)
        self.assertTrue(fila.enqueue(novo))
        self.assertEqual(fila.estado()["posicoes"][0], novo)
        self.assertEqual(fila.size(), 3)

    def test_fila_cheia_nao_insere(self):
        fila = FilaCircular(1)
        fila.enqueue(Cliente("A", "A1", 1))
        self.assertFalse(fila.enqueue(Cliente("B", "A2", 2)))


class TestFilaPrioridade(unittest.TestCase):
    def test_prioridade_e_ordem_de_chegada(self):
        fila = FilaPrioridade()
        clientes = [
            Cliente("Normal", "A1", 3),
            Cliente("Emergencia 1", "A2", 1),
            Cliente("Prioritario", "A3", 2),
            Cliente("Emergencia 2", "A4", 1),
        ]
        for cliente in clientes:
            fila.enqueue(cliente)
        ordem = [fila.dequeue() for _ in clientes]
        self.assertEqual(ordem, [clientes[1], clientes[3], clientes[2], clientes[0]])


if __name__ == "__main__":
    unittest.main()
