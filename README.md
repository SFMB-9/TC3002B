# TC3002B
> Repository for the PLY Lexer/Parser.

Andrés Briseño Celada | Salvador Federico Milanés Braniff | Juan Muniain Otero

The use of translators aids in __automating and simplifying tasks__ for programmers across different domains. In this context, language and interpretation become the output of a project that assists developers themselves. The ability to implement a tool that receives commands and, in turn, generates __high-level views__ and __tailor-made processing pipelines__ not otherwise available constitutes a competitive and operational advantage.

## Prerequisites
- Make sure to have a __Python 3.11__ or later environment installed.
  
## Setup
Navigate to the root of the cloned repository and run the following command to install dependencies:
```cmd
pip install -r requirements.txt
```

## Usage
Once dependencies are installed, run the PLY parser by executing the main script:
```cmd
python lexer.py
```
Upon execution, two additional files will be generated in the directory: parsetab.py and parser.out (explanation).
## Folder Structure
```lua
TC3002B/
│
├── examples/
│   ├── conditions.lex
│   ├── conditions2.lex
│   └── test.lex
├── lex_runner.py
├── lexer.py
├── library.py
└── Rules.md
```
- __lexer.py__: Main script for the PLY Lexer/Parser
- __library.py__: Contains supporting functions and utilities.
- __examples/__: Directory containing sample input files for the parser.
- __Rules.md__: File detailing grammar rules and language specifications.

> Avoid modifying, running or deleting the `library.py` or the generated `parsetab.py` file as they have crucial functions and utilities for the lexer.
## References
[Evidencia Final Compiladores: Desarrollo de herramienta de soporte al proceso de análisis de imágenes](https://experiencia21.tec.mx/courses/481674/assignments/15414235=)
