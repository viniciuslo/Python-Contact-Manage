
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Deletar Contato")
    print("5. Marcar/Desmarcar Contato como Favorito")
    print("6. Sair")

def add_contact(contacts):
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": False
    }
    contacts.append(contact)
    print(f"Contato '{name}' adicionado com sucesso!")

def view_contacts(contacts):
    if not contacts:
        print("Nenhum contato na lista.")
    else:
        for index, contact in enumerate(contacts, start=1):
            favorite = " (Favorito)" if contact["favorite"] else ""
            print(f"{index}. {contact['name']} - {contact['phone']} - {contact['email']}{favorite}")

def edit_contact(contacts):
    view_contacts(contacts)
    try:
        contact_num = int(input("Digite o número do contato a ser editado: "))
        if 1 <= contact_num <= len(contacts):
            contact = contacts[contact_num - 1]
            print("Deixe o campo vazio para manter o valor atual.")
            name = input(f"Nome ({contact['name']}): ") or contact['name']
            phone = input(f"Telefone ({contact['phone']}): ") or contact['phone']
            email = input(f"Email ({contact['email']}): ") or contact['email']
            contact.update({"name": name, "phone": phone, "email": email})
            print("Contato atualizado com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        contact_num = int(input("Digite o número do contato a ser deletado: "))
        if 1 <= contact_num <= len(contacts):
            removed_contact = contacts.pop(contact_num - 1)
            print(f"Contato '{removed_contact['name']}' deletado com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def toggle_favorite(contacts):
    view_contacts(contacts)
    try:
        contact_num = int(input("Digite o número do contato a ser marcado/desmarcado como favorito: "))
        if 1 <= contact_num <= len(contacts):
            contact = contacts[contact_num - 1]
            contact['favorite'] = not contact['favorite']
            status = "favorito" if contact['favorite'] else "não favorito"
            print(f"Contato '{contact['name']}' marcado como {status} com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    contacts = []
    while True:
        clear_screen()
        display_menu()
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            toggle_favorite(contacts)
        elif choice == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
