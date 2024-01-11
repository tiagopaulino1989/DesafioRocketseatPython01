class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def visualizar_contatos(self):
        for i, contato in enumerate(self.contatos, start=1):
            print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email} {'(Favorito)' if contato.favorito else ''}")

    def editar_contato(self, indice, nome, telefone, email):
        contato = self.contatos[indice]
        contato.nome = nome
        contato.telefone = telefone
        contato.email = email

    def marcar_favorito(self, indice):
        contato = self.contatos[indice]
        contato.favorito = not contato.favorito

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        for i, contato in enumerate(favoritos, start=1):
            print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email}")

    def apagar_contato(self, indice):
        del self.contatos[indice]
        