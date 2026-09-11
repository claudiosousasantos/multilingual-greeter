def greet(lang):
    greetings = {
        'es': 'Hola',
        'fr': 'Bonjour',
        'de': 'Hallo',
        'it': 'Ciao',
        'pt': 'Olá',
    }
    print(greetings.get(lang, 'Hello'))

greet('es')
greet('fr')
greet('de')
greet('it')
greet('pt')
greet('en')
