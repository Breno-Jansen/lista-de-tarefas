import os

class tarefa:
    ESTADOS = ["a_fazer", "executando", "pronta"]

    def __init__(self, nome: str, descricao: str, estado: str = "a_fazer"):
        if estado not in tarefa.ESTADOS:
            raise ValueError(f"Estado inválido: {estado}")
        self.nome = nome
        self.descricao = descricao
        self.estado = estado

    def __str__(self):
        return f"{self.nome} - {self.descricao} [{self.estado}]"


class tarefalista:
    def __init__(self):
        # dicionário de listas para cada estado
        self.tarefas = {estado: [] for estado in tarefa.ESTADOS}

    def adicionar_tarefa(self, tarefa: tarefa):
        self.tarefas[tarefa.estado].append(tarefa)

    def mover_tarefa(self, index: int, de_estado: str, para_estado: str):
        if de_estado not in self.tarefas or para_estado not in self.tarefas:
            raise ValueError("Estado inválido")
        if index < 0 or index >= len(self.tarefas[de_estado]):
            raise IndexError("Índice de tarefa inválido")
        tarefa = self.tarefas[de_estado].pop(index)
        tarefa.estado = para_estado
        self.tarefas[para_estado].append(tarefa)

    def remover_tarefa(self, index: int, estado: str):
        if estado not in self.tarefas:
            raise ValueError("Estado inválido")
        if index < 0 or index >= len(self.tarefas[estado]):
            raise IndexError("Índice de tarefa inválido")
        self.tarefas[estado].pop(index)

    def lista_tarefas(self):
        for estado, tarefas in self.tarefas.items():
            print(f"=== {estado.upper()} ===")
            if tarefas:
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa.nome} - {tarefa.descricao}")
            else:
                print("(nenhuma)")
            print()


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    lista_de_tarefas = tarefalista()

    while True:
        limpar_terminal()
        print("Bem-vindo à ToDo lista OOP!")
        print("1. listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Mover tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            limpar_terminal()
            lista_de_tarefas.lista_tarefas()
            input("Pressione Enter para voltar...")

        elif escolha == '2':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição: ")
            lista_de_tarefas.adicionar_tarefa(tarefa(nome, descricao))

        elif escolha == '3':
            limpar_terminal()
            lista_de_tarefas.lista_tarefas()
            de_estado = input("De qual estado mover? (a_fazer/executando/pronta): ").strip().lower()
            idx = int(input("Número da tarefa: ")) - 1
            para_estado = input("Para qual estado mover? (a_fazer/executando/pronta): ").strip().lower()
            try:
                lista_de_tarefas.mover_tarefa(idx, de_estado, para_estado)
            except Exception as e:
                print(f"Erro: {e}")
                input("Pressione Enter para continuar...")

        elif escolha == '4':
            limpar_terminal()
            lista_de_tarefas.lista_tarefas()
            estado = input("De qual estado remover? (a_fazer/executando/pronta): ")
            idx = int(input("Número da tarefa: ")) - 1
            try:
                lista_de_tarefas.remover_tarefa(idx, estado)
            except Exception as e:
                print(f"Erro: {e}")
                input("Pressione Enter para continuar...")

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


if __name__ == '__main__':
    main()
