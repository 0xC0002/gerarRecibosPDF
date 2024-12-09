# gerarRecibosPDF

Um sistema simples e eficiente para geração de recibos em formato PDF, ideal para pequenos negócios que precisam organizar suas vendas e gerar recibos de forma profissional.

FUNCIONALIDADES

Cadastro de Clientes: Armazene informações dos seus clientes em um banco de dados.
Cadastro de Produtos: Gerencie produtos disponíveis para venda, com preços definidos.
Geração de Recibos: Crie recibos em PDF com informações detalhadas do cliente, produtos e forma de pagamento.
Aplicação de Descontos: Permite gerar recibos com descontos personalizados.
Pasta de Recibos: Salva os recibos automaticamente em pastas organizadas por cliente.
Customização de Logo: Insira a logo da sua empresa no cabeçalho do recibo.

Pré-visualização do Recibo

Aqui está um exemplo de como um recibo gerado pelo sistema pode se parecer:

Nome da sua empresa
Dados da empresa (CNPJ, endereço, telefone, etc.)
Dados do cliente
Produtos adquiridos
Total a pagar e forma de pagamento
Dados bancários (ex.: chave PIX)

Como Usar

1. Clone este repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Instale os requisitos
Certifique-se de que o Python esteja instalado no sistema. Depois, instale as dependências:
pip install fpdf sqlite3

3. Configure o sistema
Logo: Substitua o arquivo logo.png pelo logo da sua empresa. O arquivo deve estar no mesmo diretório do código, ou ser alterado na source.
Banco de dados: O sistema cria automaticamente os bancos de dados clientes.db e produtos.db se não existirem.

4. Execute o programa
Abra um CMD no local do programa, e digite:
python sistema_recibos.py
ou, instale a biblioteca pyinstaller e execute o arquivo .exe gerado pelo pyinstaller.

5. Opções do Menu
Adicionar Produtos: Insira novos produtos no banco de dados.
Gerar Recibo: Selecione um cliente, produtos e forma de pagamento para criar um recibo.
Gerar Recibo com Desconto: Adicione um desconto personalizado antes de gerar o recibo.

ESTRUTURA DE PASTAS
Recibos: Os recibos são salvos em PDF dentro de uma pasta específica para cada cliente.
Banco de Dados:
clientes.db: Informações dos clientes.
produtos.db: Produtos disponíveis para venda.

TECNOLOGIAS UTILIZADAS
Python: Linguagem principal.
FPDF: Para geração dos arquivos PDF.
SQLite3: Para armazenamento de dados.

PERSONALIZAÇÕES
Atualize os dados da sua empresa no método dados_empresa da classe Recibo.
Personalize o menu principal para adicionar funcionalidades adicionais.

🤝 Contribuição

Faça um fork do repositório.
Crie uma nova branch para suas alterações: git checkout -b minha-nova-funcionalidade.
Commit suas alterações: git commit -m 'Adicionei uma nova funcionalidade'.
Faça push para a branch: git push origin minha-nova-funcionalidade.
Abra um Pull Request.
