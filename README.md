# Multilingual Greeter

A simple Python function that prints a greeting in different languages based on a language code.

## How it works

- Takes a language code as input (`'es'`, `'fr'`, `'de'`, `'it'`, `'pt'`, or defaults to English)
- Looks up the greeting in a dictionary and prints it: "Hola" (Spanish), "Bonjour" (French), "Hallo" (German), "Ciao" (Italian), "Olá" (Portuguese), or "Hello" (default/English)

## How to run
```bash
python greeter.py
```
The script demos the function with six calls: `greet('es')`, `greet('fr')`, `greet('de')`, `greet('it')`, `greet('pt')`, and `greet('en')`.

## What I learned

- Writing a function with a single parameter
- Using a dictionary lookup instead of `if / elif / else` chains for cleaner branching
- Using `.get()` with a default value as a sensible fallback rather than requiring every case to be listed
