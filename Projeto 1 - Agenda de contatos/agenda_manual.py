# Variáveis em maiusculas são constantes ou variáveis globais

agenda = {
    "guilherme":
        {
            "tel": "99999-1010",
            "email": "contato@solyd.com.br",
            "endereco": "Av.1"
        },
    "maria":
        {
            "tel": "99999-1212",
            "email": "maria@solyd.com.br",
            "endereco": "Av.2"
        },
    "joao":
        {
            "tel": "99999-1515",
            "email": "joao@solyd.com.br",
            "endereco": "Av.1"
        }
}

agenda['guilherme']['endereco'] = "Rua das nações"  # Alterar um valor do dicionario

agenda['lucas'] = {
    'tel': "99999-2525",
    'email': 'lucas@solyd.com.br',
    'endereco': 'Av. josé bonifacio'
}

agenda.pop('guilherme')  # Remover items do dicionario

for contato in agenda.items():
    print(contato)

print()
print(agenda['lucas'])
