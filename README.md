# PDFConverter
### (pdfconverter - v0.9)
<br>
PDFConverter é um projeto desenvolvido Python que deve ser convertido para executável com o objetivo de converter um grande número de tabelas em PDF rapidamente e sem precisar de muitas ações por parte do usuário. O executável vai ser chamado por um aplicativo desenvolvido em C#.

## LINKS

- [BIBLIOTECAS](#bibliotecas)
- [FORMATAÇÕES](#formatações)
    - [Linhas Vazias ou Sem Aspas](#linhas-vazias-ou-sem-aspas)
    - [Dados Vazios no Cabeçalho](#dados-vazios-no-cabeçalho)
    - [Quebras de Linhas no Meio dos Dados](#quebras-de-linhas-no-meio-dos-dados)
    - [Ponto e Vírgula no Final da Linha](#ponto-e-vírgula-no-final-da-linha)
    - [Espaço no Início da Linha](#espaço-no-início-da-linha)
    - [Duas Colunas](#duas-colunas)
        - [Exportar tableWithBlankCells](#exportar-tablewithblankCells)
    - [Dados Vazios](#dados-vazios)
    - [Aspas Duplas Adjacentes](#aspas-duplas-adjacentes)
    - [Espaço entre Separadores e Aspas Duplas](#espaço-entre-separadores-e-aspas-duplas)
        - [Exportar main](#exportar-main)
    - [Aspas no Início](#aspas-no-início)
    - [Aspas no Final](#aspas-no-final)
    - [Linhas Vazias ou Sem Aspas (Segunda Verificação)](#linhas-vazias-ou-sem-aspas-(segunda-verificação))
    - [Três Colunas](#três-colunas)
        - [Exportar fullClear](#exportar-fullclear)

## BIBLIOTECAS
### Python
Lista de bibliotecas utilizadas para que o script em Python fosse desenvolvido:
- **Glob**, para poder resgatar apenas arquivos com a extensão de PDF;
- **Pandas**, para realizar a conversão pra texto e para realizar a manipulação de DataFrames;
- **PyPDF2**, para poder pegar o número de páginas do PDF;
- **Tabula**, para poder fazer a leitura do arquivo PDF;
- E outras bibliotecas padrão da linguagem (Python) também foram utilizadas.

## FORMATAÇÕES
Tipos de formatações e para quais arquivos foram realizadas. Quando um arquivo for mostrado que foi exportado (nesse documento) todas as formatações acima da exportação serão realizadas.


#### **EXPORTAÇÃO [withoutFormatting]**
Começa a realizar a exportação do arquivo para segurar a exeção de quando for convertida uma tabela que possui células vazias.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORTAÇÃO</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>withoutFormatting</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\withoutFormatting"</td>
        </tr>
        <tr>
            <td>Descrição:</td>
            <td>
                 O arquivo 'withoutFormatting' <br>
                é exportado nesse momento <br>
                sem fomatação alguma.
            </td>
        </tr>
    </body>
</table>

### Linhas Vazias ou Sem Aspas
Linhas vazias que só possuem quebra de linha `'\n'` ou não possuem uma aspas dupla em nenhum lugar, serão excluídas.

Caso seja:
```



Lorem
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
Lorem ipsum

"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
"<data>";"<data>"
```

### Dados Vazios no Cabeçalho
Remove dados vazios no cabeçalho.

Caso seja:
```
"<data>";"Unnamed: 0";"<data>"
```\
Fica como:
```
"<data>";"<data>"
```

### Quebras de Linhas no Meio dos Dados
Remove quebras de linha caso elas ocorram no meio dos dados.

Caso seja:
```
"<data
data>"
```

Fica como:
```
"<data data>"
```

### Ponto e Vírgula no Final da Linha
Remove ponto e vírgula `';'` caso seja no final da linha.
    
Caso seja:
```
"<data>";"<data>";
```

Fica como:
```
"<data>";"<data>"
```

### Espaço no Início da Linha
Remove espaços no início das linhas.

Caso seja:
```
"<data>";"<data>"
 "<data>";"<data>"
"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>"
```

### Duas Colunas
Remove a linha caso ela possua duas colunas ou menos.

Caso seja:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
```

#### **EXPORTAÇÃO [tableWithBlankCells]**
Começa a realizar a exportação do arquivo para segurar a exeção de quando for convertida uma tabela que possui células vazias.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORTAÇÃO</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>tableWithBlankCells</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\tableWithBlankCells"</td>
        </tr>
        <tr>
            <td>Descrição:</td>
            <td>
                O arquivo 'tableWithBlankCells' <br>
                é exportado nesse momento <br>
                com todas as formatações <br>
                realizadas acima.
            </td>
        </tr>
    </body>
</table>

### Dados Vazios
Remove dados que estão vazios `"";` e `;""`.

Caso seja:
```
"";"<data>";"<data>";"<data>"
"<data>";"<data>";"";"<data>"
"<data>";"<data>";"<data>";""
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

### Aspas Duplas Adjacentes
Faz uma quebra de linha caso tenha aspas duplas uma do lado da outra.

Caso seja:
```
"<data>";"<data>""<data>";"<data>"
```
Fica como:
```
"<data>";"<data>"
"<data>";"<data>"
```

### Espaço entre Separadores e Aspas Duplas
Remove o conteúdo anterior caso tenha espaço entre os separadores e as aspas.

Caso seja:
```
"<Lorem ipsum>";"<Lorem ipsum>"; "<data>";"<data>"
```
Fica como:
```
"<data>";"<data>"
```

#### **EXPORTAÇÃO [main]**
Começa a realizar a exportação do arquivo principal.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORTAÇÃO</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>main</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\main"</td>
        </tr>
        <tr>
            <td>Descrição:</td>
            <td>
                O arquivo 'main' <br>
                é exportado nesse momento <br>
                com todas as formatações <br>
                realizadas acima.
            </td>
        </tr>
    </body>
</table>

### Aspas no Início
Caso a linha não comece com aspas deleta.

Caso seja:
```
"<data>";"<data>";"<data>"
<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

### Aspas no Final
Caso a linha não termine com aspas deleta.

Caso seja:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>
"<data>";"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
```

### Linhas Vazias ou Sem Aspas (Segunda Verificação)
Linhas vazias que só possuem quebra de linha `'\n'` ou não possuem uma aspas dupla em nenhum lugar, serão excluídas.

Caso seja:
```



Lorem
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
Lorem ipsum

"<data>";"<data>"
```
Fica como:
```
"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>"
"<data>";"<data>"
```

### Três Colunas
Só escreve a linha caso tenha pelo menos mais que três colunas.

Caso seja:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>
```
Fica como:
```
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
"<data>";"<data>";"<data>";"<data>"
```

#### **EXPORTAÇÃO [fullClear]**
Começa a realizar a exportação do arquivo principal com algumas modificações de formatação mais rígidas.
<table>
    <thead>
        <tr>
            <th colspan="2">EXPORTAÇÃO</th>
        </tr>
    </head>
    <body>
        <tr>
            <td>Folder Name:</td>
            <td>fullClear</td>
        </tr>
        <tr>
            <td>Folder Path:</td>
            <td>(lattice/stream) + "\\fullClear"</td>
        </tr>
        <tr>
            <td>Descrição:</td>
            <td>
                O arquivo 'fullClear' <br>
                é exportado nesse momento <br>
                com todas as formatações <br>
                realizadas acima.
            </td>
        </tr>
    </body>
</table>
