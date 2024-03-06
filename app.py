import os

restaurantes = [{'nome':'nico','categoria':'pasta','ativo':True},
             {'nome':'cabana','categoria':'lanche','ativo':False},
             {'nome':'mazaki','categoria':'japonesa','ativo':False}]

def exibir_nome_do_programa():
      print('''
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█  ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀  ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀  ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      ''')

def exibir_opcoes():
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurante')
      print('3. Alternar estado do Restaurante')
      print('4. Sair\n')

def finalizar_app():
     exibir_subtitulo('Finalizando...')

def voltar_menu():
      input('\nDigite outra tecla para voltar ao menu : ')
      main()

def opcao_invalida():
      print('Opcao Invalida\n')  
      voltar_menu()

def exibir_subtitulo(texto):
      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      '''
      Essa funcao e responsavel por cadastrar um novo restaurante
      
      Inputs :
      - Nome do restaurante
      - Categoria

      Output:
      - Adiciona um novo restaurante a lista de restaurantes

      '''
      exibir_subtitulo('Cadastro de novo restaurante')
      nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite o nome da categotia do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_menu()

def listar_novo_restaurante():
      exibir_subtitulo('Listando os restaurantes')

      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')  
      for restaurante in restaurantes:
            nome_restaurantes = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if    restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurantes.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_menu()

def alternar_estado_restaurante():
      exibir_subtitulo('Alterando estado do restaurante')
      nome_restaurante = input('Digete o nome do restaurante que deseja ativar: ')
      restarante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restarante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)
      if not restarante_encontrado:
            print('O restaurante nao foi encontrado')

      voltar_menu()
      

def escolher_opcao():
      try:   
            opcao_ecolhida = int(input('Escolha uma opçao: '))
            #opcao_ecolhida = int(opcao_ecolhida)  

            if opcao_ecolhida == 1 :
                 cadastrar_novo_restaurante()
            elif opcao_ecolhida == 2 :
                  listar_novo_restaurante()
            elif opcao_ecolhida == 3 :
                 alternar_estado_restaurante()
            elif opcao_ecolhida == 4 :
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
      main()
