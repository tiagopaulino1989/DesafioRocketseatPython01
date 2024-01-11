from contato import Contato
from agenda import Agenda

def main():
    agenda = Agenda()

    while True:
        print("\n=== Agenda de Contatos ===")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar Favorito")
        print("5. Listar Favoritos")
        print("6. Apagar Contato")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break
        elif escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            favorito = input("É favorito? (S/N): ").upper() == "S"
            novo_contato = Contato(nome, telefone, email, favorito)
            agenda.adicionar_contato(novo_contato)
            print("Contato adicionado com sucesso!")
        elif escolha == "2":
            agenda.visualizar_contatos()
        elif escolha == "3":
            agenda.visualizar_contatos()
            indice = int(input("Digite o número do contato que deseja editar: ")) - 1
            nome = input("Novo Nome: ")
            telefone = input("Novo Telefone: ")
            email = input("Novo Email: ")
            agenda.editar_contato(indice, nome, telefone, email)
            print("Contato editado com sucesso!")
        elif escolha == "4":
            agenda.visualizar_contatos()
            indice = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
            agenda.marcar_favorito(indice)
            print("Favorito atualizado com sucesso!")
        elif escolha == "5":
            agenda.listar_favoritos()
        elif escolha == "6":
            agenda.visualizar_contatos()
            indice = int(input("Digite o número do contato que deseja apagar: ")) - 1
            agenda.apagar_contato(indice)
            print("Contato apagado com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print("Seja bem vindo à sua agenda eletrônica.")
    main()
