import pandas

# Lê o Excel
dataframe = pandas.read_excel('./redes_sociais.xlsx')

# Mostrando todos os dados
print(f'\nTodos os dados do Execel: \n{dataframe}\n')

# Mostrando coluna Donos
print(f'Coluna Donos: \n{dataframe["Donos"]}\n')

# Mostrando coluna Redes
print(f'Coluna Redes: \n{dataframe["Redes"]}\n')

# Mostrando coluna Fundação
print(f'Coluna Fundação: \n{dataframe["Fundação"]}\n')