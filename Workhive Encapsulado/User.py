from Ad import Ad

class All_users():
    def __init__(self):
        self.users = {
                'Don': Standart_user('Don', '1234556', '123'),
                'Lara': Adm_user('Lara', '9876543', '321')
            }
    def get_users(self):
        return self.users
        
class User():
    def __init__(self, username, cpf, password):
        self.__username = username
        self.__cpf = cpf
        self.__password = password
        self.__favoritos = []
        self.__notificacoes = []

    def create_ad(self, ads_dict, category, description, price):
        ad = Ad(self.__username, category, description, price)
        ad_id = len(ads_dict) + 1
        ads_dict.update({ad_id: ad})
        print(f"Anúncio de id: {ad_id} criado com sucesso!\n")

    def delete_ad(self, id, ads_dict, logged_username):
        if ads_dict.get(id, None):
            if ads_dict[id].get_username() == logged_username:
                ads_dict.pop(id)
                print(f"Anúncio de id: {id} removido com sucesso!\n")
            else:
                print("Usuário não tem acesso para remover o anúncio!\n")
        else:
            print(f"O id: {id} não existe!\n")

    # Métodos para acessar os atributos encapsulados
    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, new_cpf):
        self.__cpf = new_cpf

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_favoritos(self):
        return self.__favoritos

    def favoritar(self, ad_id):
        self.__favoritos.append(ad_id)

    def get_notificacoes(self):
        return self.__notificacoes

    def adicionar_notificacao(self, notificacao):
        self.__notificacoes.extend(notificacao)

class Adm_user(User):
    def __init__(self, username, cpf, password):
        super().__init__(username, cpf, password);
    
    def show_users(self, users):
        for u in users:
            print(f'nome: {users[u].get_username()}')
            print(f'senha: {users[u].get_password()}')
            print(f'cpf: {users[u].get_cpf()}')
        print('')

    def edit_password(self, users):
        if(input('mostrar usuarios? y/n') == 'y'):
            self.show_users(users)

        select_user = input('escolha um usuário: ')
        users[select_user].set_password(input(f'digite uma senha para {users[select_user].get_username()}: '))

    def edit_username(self, users):
        if(input('mostrar usuarios? y/n') == 'y'):
            self.show_users(users)

        select_user = input('escolha um usuário: ')
        new_name = input(f'digite um usuario para {users[select_user].get_username()}: ')
        users[select_user].set_username(new_name)
        users[new_name] = users[select_user]
        del(users[select_user])

    def edit_cpf(self, users):
        if(input('mostrar usuarios? y/n') == 'y'):
            self.show_users(users)

        select_user = input('escolha um usuário: ')
        users[select_user].set_password(input(f'digite um cpf para {users[select_user].get_username()}: '))

class Standart_user(User):
    def __init__(self, username, cpf, password):
        super().__init__(username, cpf, password);
    
    def edit_password(self, user):
        new_password = input('Digite uma nova senha: ')
        self.set_password(new_password)
        return
    
    def edit_username(self, users):
        new_username = input('Digite um novo nome de usuário: ')
        current_name = self.get_username
        self.set_username(new_username)
        users[new_username] = users[current_name]
        del(users[current_name])
        return
    
    def edit_cpf(self, user):
        new_cpf = input('digite um novo cpf')
        self.set_cpf(new_cpf)
        return