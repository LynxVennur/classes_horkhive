from User import *
from Ad import Ad
import smtplib
import ssl
from email.message import EmailMessage

class Manager():
    def __init__(self):
        self._logged_username = None
        self._users = {}
        self._ads_dict = {}
        self.all_users = All_users()
        
        self.ads_dict = {
            1: Ad('Don', 'tecnologia', 'crio sites', '76543'),
            2: Ad('Don', 'Marcenaria', 'mesas artesanais', '123'),
            3: Ad('Lara', 'Hidráulico', 'conserto canos', '45'),
            4: Ad('Lara', 'eletricista', 'crio tomadas', '150'),
        }

        self.category = ['tecnologia', 'consultoria juridica', 'consultoria engenharia', 'ensino']
        
        self.execute()



    def _get_logged_username(self):
        return self._logged_username

    def _set_logged_username(self, username):
        self._logged_username = username

    def _get_users(self):
        return self.all_users.get_users()

    def _get_ads_dict(self):
        return self._ads_dict


    # Métodos encapsulados
    def _send_email(self, email_receiver, subject, body):
        email_sender = self._get_email_sender()
        email_password = self._get_email_password()

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    def _get_email_sender(self):
        return 'noreply.workhive@gmail.com'  # Encapsulamento
        
    def _get_email_password(self):
        return 'glapmivmumcddcce'  # Encapsulamento

    def _exibir_anuncio(self, ad, id_anuncio):
        if ad:
            print(f"ID: {id_anuncio}")
            print(f"Username: {ad.get_username()}")
            print(f"Categoria: {ad.get_category()}")
            print(f"Descrição: {ad.get_description()}")
            print(f"Preço: R${ad.get_price():.2f}\n")
        else:
            print(f"Anúncio com ID {id_anuncio} não encontrado.\n")

    def _get_users(self):
        return self.all_users.get_users()  # Encapsulamento

    def _get_ads_dict(self):
        return self.ads_dict  # Encapsulamento

    def _get_logged_username(self):
        return self._logged_username  # Encapsulamento

    def _set_logged_username(self, username):
        self._logged_username = username  # Encapsulamento

    def menu_principal(self):
        print('\n*** MENU ***')
        print('1 para criar usuário.')
        print('2 para fazer login.')
        return int(input('\nSelect option: '))

    def menu_logado(self):
        print('\n*** MENU ***')
        print('1 para editar usuário.')
        print('2 para remover usuário.')
        print('3 para deslogar.')
        print('4 para criar um anúncio')
        print('5 para deletar um anúncio')
        print('6 para mostrar anúncios existentes')
        print('7 para favoritar um anúncio')
        print('8 para listar os favoritos')
        print('9 mostrar anúncios por categoria')
        print('10 para adicionar feedbacks')
        print('11 para visualizar feedbacks')
        print('12 para visualizar notificações')
        print('13 para enviar email para o prestador de serviço')
        return int(input('\nSelect option: '))

    def execute(self):
        while True:
            if self._get_logged_username() is None:
                option = self.menu_principal()
                if option == 1:
                    self.create_user_menu()
                elif option == 2:
                    self.login_menu()
    
            else:
                option = self.menu_logado()
                if option == 1:
                    self.edit_user()
                elif option == 2:
                    self.delete_user()
                elif option == 3:
                    self.logout()
                elif option == 4:
                    self.create_ad_menu()
                elif option == 5:
                    self.delete_ad_menu()
                elif option == 6:
                    self.show_ads()
                elif option == 7:
                    self.favoritar()
                elif option == 8:
                    self.show_favoritos()
                elif option == 9:
                    self.listar_anuncios_por_categoria()
                elif option == 10:
                    self.adicionar_feedback_anuncio()
                elif option == 11:
                    self.visualizar_feedbacks()
                elif option == 12:
                    self.mostrar_notificacoes()
                elif option == 13:
                    self.send_email()
    

    def login_menu(self):
        username = input('Digite seu nome de usuário: ')
        password = input('Confirme sua senha: ')
        self.login(username, password)

    def create_user_menu(self):
        username = input('Digite seu nome de usuário: ')
        cpf = input('Digite seu CPF (apenas números): ')
        password = input('Crie sua senha (apenas números): ')
        self.create_user(username, cpf, password)

    

    def login(self, username, password):
        user = self._get_users().get(username, None)
        if user:
            if user.get_password() == password:
                self._set_logged_username(username)
            else:
                print('Senha incorreta!')
        else:
            print('Usuário não encontrado!')

    def create_user(self, username, cpf, password):
        if username in self._get_users():
            print('Este usuário já existe!')
        else:
            user = Standart_user(username, cpf, password)
            self._get_users().update({username: user})
            print('Usuário criado com sucesso!')

    def edit_user(self):
        print('\nO que deseja mudar?')
        print('1 para usuário')
        print('2 para senha')
        print('3 para cpf\n')
        option = int(input("Digite sua opção: "))

        if option == 1:
            self._get_users()[self._get_logged_username()].edit_username(self.all_users.users)

        elif option == 2:
            self._get_users()[self._get_logged_username()].edit_password(self.all_users.users)

        elif option == 3:
            self._get_users()[self._get_logged_username()].edit_cpf(self.all_users.users)
        
    def delete_user(self):
        self._get_users().pop(self._get_logged_username())
        print(f"Usuário {self._get_logged_username()} removido com sucesso!")
        self.logout()
    def logout(self):
        self._set_logged_username(None)
        print('Você foi deslogado.')

    def create_ad_menu(self):
        user = self._get_users()[self._get_logged_username()]
        category = input('Qual a categoria do serviço? ')
        description = input('Descreva o serviço: ')
        price = float(input('Qual o preço do serviço? R$'))
        user.create_ad(self._get_ads_dict(), category, description, price)
        for u in self._get_users().values():
            if u.get_username() != user.get_username():
                u.adicionar_notificacao(f'Novo anúncio disponível: {category}')

    def delete_ad_menu(self):
        id = int(input('Digite o ID do anúncio a ser deletado! '))
        user = self._get_users()[self._get_logged_username()]
        user.delete_ad(id, self._get_ads_dict(), self._get_logged_username())

    def show_ads(self):
        print('Anúncios existentes:')
        for id_anuncio, ad in self._get_ads_dict().items():
            self._exibir_anuncio(ad, id_anuncio)

    
    def favoritar(self):
        id_anuncio = int(input('Qual o ID do anúncio que deseja favoritar? '))
        if id_anuncio in self.ads_dict:
            self.users[self._logged_username].favoritar(id_anuncio)
            self.ads_dict[id_anuncio].favoritar()  # Chama o método favoritar do objeto Ad
            print('Anúncio favoritado com sucesso!')
        else:
            print('Anúncio não encontrado.')



    def show_favoritos(self):
        user = self._get_users()[self._get_logged_username()]
        favoritos = user.get_favoritos()

        if not favoritos:
            print('Aba de favoritos vazia.')
        else:
            print('Aba de favoritos:')
            for id_anuncio in favoritos:
                self._exibir_anuncio(self._get_ads_dict().get(id_anuncio), id_anuncio)

    def listar_anuncios_por_categoria(self):
        categoria = input('Digite a categoria: ')

        print(f'\nAnúncios na categoria "{categoria}":')
        encontrou_anuncios = False

        for id_anuncio, ad in self.ads_dict.items():
            if ad.get_category().lower() == categoria.lower():
                self._exibir_anuncio(ad, id_anuncio)
                encontrou_anuncios = True

        if not encontrou_anuncios:
            print(f'Não há anúncios na categoria "{categoria}".')
    
    def _exibir_anuncio(self, ad, id_anuncio):
        if ad:
            print(f"ID: {id_anuncio}")
            print(f"Username: {ad.get_username()}")
            print(f"Categoria: {ad.get_category()}")
            print(f"Descrição: {ad.get_description()}")
            print(f"Preço: R${ad.get_price():.2f}\n")
        else:
            print(f"Anúncio com ID {id_anuncio} não encontrado.\n")

    def adicionar_feedback_anuncio(self):
        identificador = int(input('Digite o ID do anúncio: '))
        feedback = input('Digite seu feedback: ')

        if identificador in self._get_ads_dict():
            ad = self._get_ads_dict()[identificador]
            ad.add_feedback(feedback)

            print('Feedback adicionado com sucesso!')
        else:
            print('Anúncio não encontrado.')

    def visualizar_feedbacks(self):
        user = self._get_users()[self._get_logged_username()]

        print('Feedbacks dos seus anúncios:')
        found_feedback = False

        for id_anuncio, ad in self._get_ads_dict().items():
            if ad.get_username() == user.get_username():
                feedbacks = ad.get_feedbacks()
                if feedbacks:
                    print(f"Anúncio ID {id_anuncio}:")
                    print(f"Username: {ad.get_username()}")
                    print(f"Categoria: {ad.get_category()}")
                    print(f"Descrição: {ad.get_description()}")
                    print(f"Preço: R${ad.get_price():.2f}")
                    print("Feedbacks:")
                    for feedback in feedbacks:
                        print(feedback)
                    print()
                    found_feedback = True

        if not found_feedback:
            print("Não há feedbacks para seus anúncios.")

    def mostrar_notificacoes(self):
        user = self._get_users()[self._get_logged_username()]

        notificacoes = user.get_notificacoes()

        if notificacoes:
            print("Você tem", len(notificacoes), "notificação(ões):")
            for notificacao in notificacoes:
                print(notificacao)
            user.adicionar_notificacao([])  # Limpa as notificações após exibi-las
        else:
            print("Você não possui notificações.")

    def send_email(self):
        email_receiver = input('Email do destinatário: ')
        subject = input('Qual o assunto do seu email? ')
        print('\nLembre de informar uma forma de contato pessoal para futuro contato com o prestador de serviço.\n')
        body = input('Digite sua mensagem: ')

        self._send_email(email_receiver, subject, body)

if __name__ == "__main__":
    manager = Manager()
    manager.execute()




