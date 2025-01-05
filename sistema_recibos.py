import sqlite3
import os
from datetime import datetime
from fpdf import FPDF

class Recibo(FPDF):
    def __init__(self):
        super().__init__()
        self.line_height = 7.5  # espaçamento entre linhas

    def header(self):
        self.image("H:\\repos\\gerarRecibosPDF\\logo.png", 10, 8, 33) # Alterar o seu caminho para a logo
        self.set_font("Arial", "B", 16)
        self.cell(0, self.line_height, "NOME DA SUA EMPRESA", 0, 1, "C") # Nome da empresa
        self.set_font("Arial", "B", 12)
        self.cell(0, self.line_height, "RECIBO", 0, 1, "C")
        self.ln(15)
        self.line(50, self.get_y(), 200, self.get_y())

    def dados_empresa(self):
        self.set_font("Arial", "B", 10)
        self.cell(0, self.line_height, "DADOS DA EMPRESA", 0, 1, "C")
        self.ln(5)
        # informações
        self.set_font("Arial", "B", 10)
        self.cell(20, self.line_height, "CNPJ:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "46.298.652/0001-55", 0, 1, "L") # CNPJ da empresa
        self.set_font("Arial", "B", 10)
        self.cell(20, self.line_height, "CEP:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "00000-000", 0, 1, "L") # CEP da empresa

        self.set_font("Arial", "B", 10)
        self.cell(20, self.line_height, "END:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "RUA SENADOR BERNARDO MONTEIRO, 184. UF: RJ", 0, 1, "L") # ENDEREÇO DA EMPRESA

        self.set_font("Arial", "B", 10)
        self.cell(35, self.line_height, "BAIRRO/DISTRITO:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "BAIRRO DA EMPRESA", 0, 1, "L") # BAIRRO DA EMPRESA

        self.set_font("Arial", "B", 10)
        self.cell(15, self.line_height, "TEL:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "(00) 00000-0000", 0, 1, "L") # TELEFONE DA EMPRESA

        self.set_font("Arial", "B", 10)
        self.cell(20, self.line_height, "EMAIL:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "EMAIL@GMAIL.COM", 0, 1, "L") # EMAIL DA EMPRESA

        self.set_font("Arial", "B", 10)
        self.cell(30, self.line_height, "VENDEDOR:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "NOME DO VENDEDOR", 0, 1, "L") # NOME DO VENDEDOR

        self.set_font("Arial", "B", 10)
        self.cell(30, self.line_height, "DATA:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.cell(0, self.line_height, data_hora_atual, 0, 1, "L")
        self.ln(5)

        self.line(10, self.get_y(), 200, self.get_y())  # linha

    def dados_cliente(self, cliente, cnpj_cpf, endereco, bairro, uf, cep):
        self.set_font("Arial", "B", 10)
        self.cell(0, self.line_height, "DADOS DO CLIENTE", 0, 1, "C")
        self.ln(5)
        # campo cliente
        self.set_font("Arial", "B", 10)
        self.cell(20, self.line_height, "CLIENTE:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, cliente, 0, 1, "L")
        self.set_font("Arial", "B", 10)
        self.cell(20, self.line_height, "CNPJ/CPF:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, cnpj_cpf, 0, 1, "L")
        self.set_font("Arial", "B", 10)
        self.cell(20, self.line_height, "END:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, f"{endereco}, {bairro}, {uf}. CEP: {cep}", 0, 1, "L")
        self.ln(5)

        self.line(10, self.get_y(), 200, self.get_y())  # Linha divisória

    def descricao_produtos(self, produtos, total, pagamento):
        self.set_font("Arial", "B", 10)
        self.cell(0, self.line_height, "DESCRIÇÃO DOS PRODUTOS", 0, 1, "C")
        self.ln(5)
        # lista produtos
        self.set_font("Arial", "", 10)
        for produto, (quantidade, _) in produtos.items():  # Ignorando o preço unitário
            self.cell(0, self.line_height, f"- {quantidade}x {produto}", 0, 1, "L")
        self.ln(5)
        # total
        self.set_font("Arial", "B", 10)
        self.cell(30, self.line_height, "TOTAL:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, f"R${total:.2f}", 0, 1, "L")
        # nota
        self.set_font("Arial", "B", 10)
        self.cell(30, self.line_height, "NOTA:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "A PAGAR", 0, 1, "L")
        # forma de pagamento
        self.set_font("Arial", "B", 10)
        self.cell(50, self.line_height, "FORMA DE PAGAMENTO:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, pagamento, 0, 1, "L")
        self.ln(5)
        self.line(10, self.get_y(), 200, self.get_y())  # Linha divisória

    def dados_bancarios(self):
        self.set_font("Arial", "B", 10)
        self.cell(0, self.line_height, "DADOS BANCÁRIOS", 0, 1, "C")
        self.ln(5)
    # pix
        self.set_font("Arial", "B", 10)
        self.cell(40, self.line_height, "PIX:", 0, 0, "L")  # Largura fixa para o rótulo
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "(21) 98359-1329", 0, 1, "L")  # Valor ocupa o restante da linha
    # nome
        self.set_font("Arial", "B", 10)
        self.cell(40, self.line_height, "NOME:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "Sandra Ferreira da Silva da Rocha", 0, 1, "L")
    # banco
        self.set_font("Arial", "B", 10)
        self.cell(40, self.line_height, "BANCO:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "Bradesco", 0, 1, "L")
    # agencia
        self.set_font("Arial", "B", 10)
        self.cell(40, self.line_height, "AGÊNCIA:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "2922", 0, 1, "L")
    # conta poupança
        self.set_font("Arial", "B", 10)
        self.cell(40, self.line_height, "CONTA POUPANÇA:", 0, 0, "L")
        self.set_font("Arial", "", 10)
        self.cell(0, self.line_height, "1004831-1", 0, 1, "L")

        self.ln(10)

def configurar_produtos():
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    # Cria a tabela se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)

    # Produtos fixos
    produtos_fixos = [
        ("Salgados misto", 0.48),
        ("Churros", 0.55),
        ("Pão de queijo congelado", 0.55),
        ("Pão de queijo assado", 0.70),
    ]

    # Inserir apenas se não existirem duplicados
    for nome, preco in produtos_fixos:
        cursor.execute("""
            SELECT * FROM produtos WHERE nome = ?
        """, (nome,))
        if cursor.fetchone() is None:  # Apenas insere se o produto não existir
            cursor.execute("""
                INSERT INTO produtos (nome, preco) VALUES (?, ?)
            """, (nome, preco))

    conexao.commit()
    conexao.close()

def adicionar_produto(nome, preco):
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, preco) 
        VALUES (?, ?)
    """, (nome, preco))
    conexao.commit()
    conexao.close()
    print(f"Produto '{nome}' adicionado com sucesso!")

def menu_adicionar_produtos():
    while True:
        print("\nMenu - Adicionar Produtos")
        nome = input("Nome do produto (ou pressione ENTER para sair): ")
        if not nome:
            break  # Sai do menu se o usuário pressionar ENTER

        preco = input(f"Digite o preço do produto '{nome}': ").replace(",", ".")
        try:
            preco = float(preco)  # Converte o preço para float
            adicionar_produto(nome, preco)  # Adiciona o produto ao banco de dados
        except ValueError:
            print("Preço inválido. Tente novamente.")

        if __name__ == "__main__":
    # Configurar o banco de dados, se ainda não existir

            configurar_db_produtos()

    while True:
        print("\nMenu Principal")
        print("1. Adicionar produtos")
        print("2. Gerar recibo")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_adicionar_produtos()
        elif escolha == "2":
            # Aqui você chama as funções para coletar dados e gerar o recibo
            break  # Saindo para o código existente de geração de recibo
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")



def buscar_produtos():
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos

def exibir_tabela_produtos():
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, preco FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()

    print("\nProdutos disponíveis:")
    for id_produto, nome, preco in produtos:
        print(f"{id_produto}. {nome} - R$ {preco:.2f}")


# funções DB
def configurar_db():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj_cpf TEXT NOT NULL,
            endereco TEXT NOT NULL,
            bairro TEXT NOT NULL,
            uf TEXT NOT NULL,
            cep TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_cliente(nome, cnpj_cpf, endereco, bairro, uf, cep):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO clientes (nome, cnpj_cpf, endereco, bairro, uf, cep)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, cnpj_cpf, endereco, bairro, uf, cep))
    conexao.commit()
    conexao.close()

def buscar_clientes():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()
    return clientes

def coletar_dados_cliente():
    """Coleta dados do cliente com mensagens claras."""
    clientes = buscar_clientes()
    if clientes:
        print("\n=== Clientes Cadastrados ===")
        for idx, cliente in enumerate(clientes, start=1):
            print(f"{idx}. {cliente[1]}")  # Exibe o nome do cliente
        escolha = input("\nSelecione um cliente pelo número ou pressione ENTER para adicionar um novo: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(clientes):
            cliente = clientes[int(escolha) - 1]
            print(f"✅ Cliente selecionado: {cliente[1]}")
            return cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6]
        else:
            print("⚠️ Entrada inválida ou cliente não encontrado. Vamos cadastrar um novo cliente.")
    
    print("\n=== Cadastro de Novo Cliente ===")
    nome = input("Nome do cliente: ").strip()
    cnpj_cpf = input("CNPJ/CPF do cliente: ").strip()
    endereco = input("Endereço do cliente: ").strip()
    bairro = input("Bairro do cliente: ").strip()
    uf = input("UF (Estado): ").strip()
    cep = input("CEP do cliente: ").strip()
    adicionar_cliente(nome, cnpj_cpf, endereco, bairro, uf, cep)
    print(f"✅ Cliente '{nome}' cadastrado com sucesso!")
    return nome, cnpj_cpf, endereco, bairro, uf, cep

def coletar_produtos():
    """Coleta os produtos desejados pelo usuário."""
    produtos_selecionados = {}

    # Buscar produtos disponíveis
    produtos_disponiveis = buscar_produtos()
    if not produtos_disponiveis:
        print("⚠️ Não há produtos cadastrados no sistema. Cadastre produtos antes de gerar um recibo.")
        return {}, 0, None

    # Exibir a tabela de produtos uma única vez
    print("\n=== Produtos Disponíveis ===")
    for produto in produtos_disponiveis:
        print(f"{produto[0]}. {produto[1]} - R$ {produto[2]:.2f}")
    print("\nDigite o número do produto para adicioná-lo ao recibo. Pressione ENTER para finalizar.")

    # Coleta dos produtos
    while True:
        escolha = input("Digite o número do produto: ").strip()
        if not escolha:  # Finaliza se o usuário pressionar ENTER
            break

        if escolha.isdigit():
            escolha = int(escolha)
            produto = next((p for p in produtos_disponiveis if p[0] == escolha), None)
            if produto:
                try:
                    quantidade = int(input(f"Digite a quantidade de {produto[1]}: ").strip())
                    if quantidade <= 0:
                        print("⚠️ Quantidade inválida. Por favor, insira um número positivo.")
                        continue
                    produtos_selecionados[produto[1]] = (quantidade, produto[2])
                    print(f"✅ {quantidade} '{produto[1]}' adicionados ao recibo.")
                except ValueError:
                    print("⚠️ Quantidade inválida. Por favor, insira um número.")
            else:
                print("⚠️ Produto não encontrado. Tente novamente.")
        else:
            print("⚠️ Entrada inválida. Digite um número correspondente a um produto listado.")

    if produtos_selecionados:
        total = sum(qtd * preco for qtd, preco in produtos_selecionados.values())
        print(f"\n💰 Total dos produtos selecionados: R${total:.2f}")
        pagamento = input("Digite a forma de pagamento (Ex.: Dinheiro, Cartão): ").strip()
        return produtos_selecionados, total, pagamento
    else:
        print("⚠️ Nenhum produto foi selecionado.")
        return {}, 0, None

def criar_pasta_cliente(cliente):
    """Cria uma pasta para armazenar recibos de um cliente específico."""
    # Define o diretório principal para os recibos
    pasta_recibos = "Recibos"
    if not os.path.exists(pasta_recibos):
        os.mkdir(pasta_recibos)
        print(f"📁 Diretório '{pasta_recibos}' criado com sucesso.")

    # Cria a subpasta para o cliente dentro de 'Recibos'
    pasta_cliente = os.path.join(pasta_recibos, cliente.replace(" ", "_"))
    if not os.path.exists(pasta_cliente):
        os.mkdir(pasta_cliente)
        print(f"📂 Subpasta para o cliente '{cliente}' criada com sucesso.")

    return pasta_cliente

def configurar_db_produtos():
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

# Estrutura do menu baseada em dicionário
MENU_OPCOES = {
    "1": ("Adicionar produtos", lambda: menu_adicionar_produtos()),
    "2": ("Gerar recibo", lambda: gerar_recibo()),
    "3": ("Gerar recibo com desconto", lambda: gerar_recibo_com_desconto()),
    "4": ("Sair", lambda: print("Saindo do programa...") or exit()),
}

def exibir_menu():
    """Exibe o menu principal com mensagens melhoradas."""
    print("\n=== Menu Principal ===")
    for key, (descricao, _) in MENU_OPCOES.items():
        print(f"{key}. {descricao}")
    escolha = input("Digite o número correspondente à sua escolha: ").strip()
    return escolha

def menu_principal():
    """Controla o fluxo principal do programa baseado no menu com mensagens melhoradas."""
    while True:
        escolha = exibir_menu()
        if escolha in MENU_OPCOES:
            acao = MENU_OPCOES[escolha][1]
            acao()
        else:
            print("⚠️ Opção inválida. Por favor, escolha um número entre as opções listadas.")

def gerar_recibo():
    recibo = Recibo()
    recibo.add_page()

    # Adicionar dados fixos da empresa
    recibo.dados_empresa()

    # Coletar dados do cliente
    cliente, cnpj_cpf, endereco, bairro, uf, cep = coletar_dados_cliente()
    recibo.dados_cliente(cliente, cnpj_cpf, endereco, bairro, uf, cep)

    # Coletar produtos e calcular o total
    produtos, total, pagamento = coletar_produtos()
    if not produtos:
        print("Nenhum produto foi selecionado. Recibo não gerado.")
        return

    recibo.descricao_produtos(produtos, total, pagamento)

    # Adicionar dados bancários
    recibo.dados_bancarios()

    # Criar pasta do cliente e salvar o recibo
    pasta_cliente = criar_pasta_cliente(cliente)
    arquivo = os.path.join(pasta_cliente, f"recibo_{datetime.now().strftime('%d%m%y_%H%M%S')}.pdf")
    recibo.output(arquivo)

    print(f"Recibo gerado com sucesso! Arquivo salvo em: {arquivo}")

def gerar_recibo_com_desconto():
    recibo = Recibo()
    recibo.add_page()

    # Adicionar dados fixos da empresa
    recibo.dados_empresa()

    # Coletar dados do cliente
    cliente, cnpj_cpf, endereco, bairro, uf, cep = coletar_dados_cliente()
    recibo.dados_cliente(cliente, cnpj_cpf, endereco, bairro, uf, cep)

    # Coletar produtos e calcular o total
    produtos, total, pagamento = coletar_produtos()
    if not produtos:
        print("Nenhum produto foi selecionado. Recibo não gerado.")
        return

    print(f"Total antes do desconto: R${total:.2f}")
    desconto = input("Digite o valor do desconto (R$): ").replace(",", ".")
    try:
        desconto = float(desconto)
        if desconto < 0 or desconto > total:
            print("Desconto inválido. Deve ser positivo e menor ou igual ao total.")
            return
    except ValueError:
        print("Erro: Insira um valor válido para o desconto.")
        return

    total_com_desconto = total - desconto
    print(f"Total com desconto: R${total_com_desconto:.2f}")

    recibo.descricao_produtos(produtos, total_com_desconto, pagamento)

    # Adicionar dados bancários
    recibo.dados_bancarios()

    # Criar pasta do cliente e salvar o recibo
    pasta_cliente = criar_pasta_cliente(cliente)
    arquivo = os.path.join(pasta_cliente, f"recibo_com_desconto_{datetime.now().strftime('%d%m%y_%H%M%S')}.pdf")
    recibo.output(arquivo)

    print(f"Recibo com desconto gerado com sucesso! Arquivo salvo em: {arquivo}")

# Iniciar o menu principal
if __name__ == "__main__":
    menu_principal()