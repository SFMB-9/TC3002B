# TC3002B
> Repository for the PLY Lexer/Parser.

Andrés Briseño Celada | Salvador Federico Milanés Braniff | Juan Muniain Otero

The use of translators aids in __automating and simplifying tasks__ for programmers across different domains. In this context, language and interpretation become the output of a project that assists developers themselves. The ability to implement a tool that receives commands and, in turn, generates __high-level views__ and __tailor-made processing pipelines__ not otherwise available constitutes a competitive and operational advantage.

## Prerequisites
- Make sure to have a __Python 3.11__ or later environment installed.
- You will need to have the __Graphviz__ Software installed. Follow download instructions [here](https://graphviz.org/).
  
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
Upon execution, two additional files will be generated in the directory: `parsetab.py` and `parser.out`, parsetab.py contains additional dependencies for executing the parser, whilst parser.out will show the infered rules from the lexer script.

You can additionally run files through the lexer with the `.lex` file extension. Run the `lex_runner.py` script to select one of the example files. You can also run your own files by adding them to the `examples` directory.
## Folder Structure
```lua
TC3002B/
│
├── examples/
│   ├── conditions.lex
│   ├── conditions2.lex
│   └── test.lex
├── language.md
├── lex_runner.py
├── lexer.py
└── library.py
```
- __lexer.py__: Main script for the PLY Lexer/Parser
- __library.py__: Contains supporting functions and utilities.
- __lex_runner.py__: Script to load example files with the lexer.
- __examples/__: Directory containing sample input files for the lexer.
- __language.md__: File detailing language definition and demonstration. [[Link](language.md)]

> Avoid modifying or deleting the `library.py` or the generated `parsetab.py` file as they have crucial functions and utilities for the lexer.
## References
[Evidencia Final Compiladores: Desarrollo de herramienta de soporte al proceso de análisis de imágenes](https://experiencia21.tec.mx/courses/481674/assignments/15414235=)
