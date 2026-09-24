from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    senha: str
    prioridade: int

    def __str__(self):
        nomes_prioridade = {
            1: "Emergência",
            2: "Prioritário",
            3: "Normal",
        }
        tipo = nomes_prioridade.get(self.prioridade, "Desconhecida")
        return f"{self.senha} - {self.nome} (prioridade {self.prioridade}: {tipo})"
