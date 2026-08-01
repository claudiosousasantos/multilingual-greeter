# Multilingual Greeter

A simple Python function that prints a greeting in different languages based on a language code.

## How it works
- Takes a language code as input (`'es'`, `'fr'`, or defaults to English)
- Prints the corresponding greeting: "Hola" (Spanish), "Bonjour" (French), or "Hello" (default/English)

## How to run
```bash
python greeter.py
```
The script demos the function with three calls: `greet('es')`, `greet('fr')`, and `greet('en')`.

## What I learned
- Writing a function with a single parameter
- Using `if / elif / else` to branch behavior based on input
- Using a fallback (`else`) as a sensible default rather than requiring every case to be listed
