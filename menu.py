class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.relatorio_vendas = []
        self.relatorio_compras = []
        self.anuncios = []
        self.perguntas_respostas = []
        self.lista_favoritos = []

class Anuncio:
    def __init__(self, id, titulo, descricao, preco, data_criacao, categoria, proprietario):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.preco = preco
        self.data_criacao = data_criacao
        self.categoria = categoria
        self.proprietario = proprietario
        self.perguntas_respostas = []

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

# Exemplos de listas para simular o banco de dados
usuarios = []
anuncios = []
categorias = []

# Funções para o menu

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    # Simulação de geração de ID único para o usuário
    id_usuario = len(usuarios) + 1

    novo_usuario = Usuario(id=id_usuario, nome=nome, email=email, senha=senha)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def acessar_conta():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if usuario.email == email and usuario.senha == senha:
            return usuario

    print("E-mail ou senha incorretos.")
    return None

def mostrar_anuncios():
    print("Anúncios disponíveis:")
    for anuncio in anuncios:
        print(f"{anuncio.id}: {anuncio.titulo} - R${anuncio.preco}")

def criar_anuncio(usuario):
    titulo = input("Digite o título do anúncio: ")
    descricao = input("Digite a descrição do anúncio: ")
    preco = float(input("Digite o preço do anúncio: "))

    print("Categorias disponíveis:")
    for categoria in categorias:
        print(f"{categoria.id}: {categoria.nome}")

    while True:
        categoria_id = int(input("Digite o ID da categoria do anúncio: "))
        categoria = next((c for c in categorias if c.id == categoria_id), None)

        if categoria:
            # Simulação de geração de ID único para o anúncio
            id_anuncio = len(anuncios) + 1
            novo_anuncio = Anuncio(id=id_anuncio, titulo=titulo, descricao=descricao, preco=preco, data_criacao=None, categoria=categoria, proprietario=usuario)
            anuncios.append(novo_anuncio)
            usuario.anuncios.append(novo_anuncio)
            print("Anúncio criado com sucesso!")
            break
        else:
            print("Categoria inválida. Digite o ID de uma categoria existente.")

def ver_perfil(usuario):
    print(f"Nome: {usuario.nome}")
    print(f"E-mail: {usuario.email}")

def editar_perfil(usuario):
    print(f"Editar Perfil de {usuario.nome}:")
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    novo_email = input("Digite o novo e-mail (ou pressione Enter para manter o atual): ")
    nova_senha = input("Digite a nova senha (ou pressione Enter para manter a atual): ")

    if novo_nome:
        usuario.nome = novo_nome

    if novo_email:
        usuario.email = novo_email

    if nova_senha:
        usuario.senha = nova_senha

    print("Perfil atualizado com sucesso!")

def excluir_conta(usuario):
    confirmacao = input("Tem certeza de que deseja excluir a conta? (s/N): ")

    if confirmacao.lower() == 's':
        usuarios.remove(usuario)
        print("Conta excluída com sucesso!")
    else:
        print("Exclusão de conta cancelada.")

def minhas_perguntas(usuario):
    print("Minhas perguntas:")
    for pergunta in usuario.perguntas_respostas:
        print(f"Pergunta: {pergunta.texto}")
        resposta = pergunta.resposta
        if resposta:
            print(f"Resposta: {resposta.texto}")
        else:
            print("Ainda não há resposta para esta pergunta.")

def ver_minhas_compras(usuario):
    print("Meus relatórios de compras:")
    for compra in usuario.relatorio_compras:
        print(f"{compra.titulo} - R${compra.preco}")

def ver_minhas_vendas(usuario):
    print("Meus relatórios de vendas:")
    for venda in usuario.relatorio_vendas:
        print(f"{venda.titulo} - R${venda.preco}")

def listar_favoritos(usuario):
    print("Meus favoritos:")
    for anuncio in usuario.lista_favoritos:
        print(f"{anuncio.titulo} - R${anuncio.preco}")

def criar_categoria():
    nome_categoria = input("Digite o nome da nova categoria: ")

    # Simulação de geração de ID único para a categoria
    id_categoria = len(categorias) + 1

    nova_categoria = Categoria(id=id_categoria, nome=nome_categoria)
    categorias.append(nova_categoria)

    print("Categoria criada com sucesso!")

# ... (implement other functions)

# Função para o menu do usuário logado

def menu_usuario_logado(usuario_logado):
    while True:
        print(f"\n------- Menu do Usuário: {usuario_logado.nome} -------")
        print("1. Ver Perfil")
        print("2. Editar Perfil")
        print("3. Excluir Conta")
        print("4. Ver Minhas Compras")
        print("5. Ver Minhas Vendas")
        print("6. Criar Anúncio")
        print("7. Minhas Perguntas")
        print("8. Listas de Favoritos")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_perfil(usuario_logado)
        elif opcao == '2':
            editar_perfil(usuario_logado)
        elif opcao == '3':
            excluir_conta(usuario_logado)
            break
        elif opcao == '4':
            ver_minhas_compras(usuario_logado)
        elif opcao == '5':
            ver_minhas_vendas(usuario_logado)
        elif opcao == '6':
            criar_anuncio(usuario_logado)
        elif opcao == '7':
            minhas_perguntas(usuario_logado)
        elif opcao == '8':
            listar_favoritos(usuario_logado)
        elif opcao == '9':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# ... (implement other menu functions)

# Função para o menu principal

def menu_principal():
    while True:
        print("\n------- Menu Principal -------")
        print("1. Cadastrar Usuário")
        print("2. Acessar Conta")
        print("3. Procurar Anúncios")
        print("4. Ver Minhas Compras")
        print("5. Ver Minhas Vendas")
        print("6. Criar Anúncio")
        print("7. Minhas Perguntas")
        print("8. Listas de Favoritos")
        print("9. Criar Categoria")
        print("10. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            usuario_logado = acessar_conta()
            if usuario_logado:
                menu_usuario_logado(usuario_logado)
        elif opcao == '3':
            mostrar_anuncios()
        elif opcao == '4':
            ver_minhas_compras(usuario_logado)
        elif opcao == '5':
            ver_minhas_vendas(usuario_logado)
        elif opcao == '6':
            criar_anuncio(usuario_logado)
        elif opcao == '7':
            minhas_perguntas(usuario_logado)
        elif opcao == '8':
            listar_favoritos(usuario_logado)
        elif opcao == '9':
            criar_categoria()
        elif opcao == '10':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# ... (implement other menu functions)

# Chamar o menu principal para iniciar o programa

menu_principal()
