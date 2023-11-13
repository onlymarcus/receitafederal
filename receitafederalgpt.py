import pandas as pd

# Função para formatar a quantidade com dez casas decimais


def format_crypto_quantity(value):
    value_str = str(value)
    value_str = value_str.ljust(12, '0').replace('.', '').replace(',', '')
    return value_str[-11:]

# Função para formatar o CPF ou CNPJ com base no tipo indicado


def format_cpf_cnpj(number, tipo):
    return str(number).rjust(14, '0') if tipo == 'CNPJ' else str(number).rjust(11, '0')


# Função para formatar a data
def format_date(date):
    return pd.to_datetime(date).strftime('%d%m%Y')


# Carregar a planilha Excel
df = pd.read_excel('nov23.xlsx', sheet_name='PF PJ Sem Exchange')


# Formatar as colunas
df['Data'] = df['Data'].apply(format_date)
df['Quantidade'] = df['Quantidade'].apply(format_crypto_quantity)
# Supondo que a coluna 'TipoNI' indique se o número é CPF ou CNPJ
df['Comprador ou Vendedor - CPF ou CNPJ'] = df.apply(lambda row: format_cpf_cnpj(
    row['Comprador ou Vendedor - CPF ou CNPJ'], row['TipoNI']), axis=1)
df['Comprador ou Vendedor - País'] = 'BR'

# Definir o tipo de registro com base no tipo de operação
df['Tipo de Registro'] = df['Tipo de Registro'].apply(
    lambda x: '0110' if x == 'Compra' else '0120')

# Selecionar e ordenar as colunas conforme a ordem do arquivo TXT
df_txt = df[['Tipo de Registro', 'Data', 'OperacaoCodigo', 'Valor', 'Taxas', 'Moeda',
             'Quantidade', 'TipoNI', 'Comprador ou Vendedor - País', 'Comprador ou Vendedor - CPF ou CNPJ',
             'Comprador ou Vendedor - NI', 'Comprador ou Vendedor - Nome']]

# Substituir 'CPF' por 1 e 'CNPJ' por 2 na coluna 'TipoNI'
df['TipoNI'] = df['TipoNI'].replace({'CPF': 1, 'CNPJ': 2})

# Converter o DataFrame para o formato de texto
txt_output = df_txt.apply(lambda x: '|'.join(
    x.astype(str)), axis=1).str.cat(sep='\n')

# Caminho para salvar o arquivo TXT
output_txt_path = 'C:\dev\IN1888\teste.txt'

# Salvar o texto no arquivo TXT
with open(output_txt_path, 'w') as file:
    file.write(txt_output)

# O caminho do arquivo TXT será retornado para que você possa verificar ou baixar o arquivo.
output_txt_path
