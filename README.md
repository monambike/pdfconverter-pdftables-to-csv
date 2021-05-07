# PDFConverter
### (pdfconverter)

PDFConverter é um projeto desenvolvido Python que deve ser convertido para executável com o objetivo de converter um grande número de tabelas em PDF rapidamente e sem precisar de muitas ações por parte do usuário. O executável vai ser chamado por um aplicativo desenvolvido em C#.

## LINKS

- [Bibliotecas Utilizadas](#bibliotecas)
- [Formatações](#formatações)
    - [Dados Vazios no Cabeçalho](#dados-vazios-no-cabeçalho)
    - [Linhas Vazias ou Sem Aspas](#linhas-vazias-ou-sem-aspas)
    - [Dados Vazios no Cabeçalho](#dados-vazios-no-cabeçalho)
    - [Quebras de Linhas no Meio dos Dados](#quebras-de-linhas-no-meio-dos-dados)
    - [Ponto e Vírgula no Final da Linha](#ponto-e-vírgula-no-final-da-linha)
    - [Duas Colunas](#duas-colunas)
        - [tableWithBlankCells](#tableWithBlankCells)
    - [Dados Vazios](#dados-vazios)
    - [Aspas Duplas Adjacentes](#aspas-duplas-adjacentes)
    - [Espaço entre Separadores e Aspas Duplas (Quebra)](#espaço-entre-separadores-e-aspas-duplas-(quebra))
    - [Espaço no Início da Linha](#espaço-no-início-da-linha)
    - [Espaço entre Separadores e Aspas Duplas (Remoção)](#espaço-entre-separadores-e-aspas-duplas-(remoção))
    - [Aspas (Início e Final) e Ponto e Vírgula](#aspas-(início-e-final)-e-ponto-e-vírgula)
        - [main](#main)
    - [Aspas no Início](#aspas-no-início)
    - [Aspas no Final](#aspas-no-final)
    - [Linhas Vazias ou Sem Aspas (Segunda Verificação)](#linhas-vazias-ou-sem-aspas-(segunda-verificação))
    - [Três Colunas](#três-colunas)
        - [fullClear](#fullClear)

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
```
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

> **EXPORTAÇÃO**
>
> #### **tableWithBlankCells**
>
> [\\\\tableWithBlankCells]
>
>
> O arquivo 'tableWithBlankCells' é exportado nesse momento com todas as formatações realizadas acima.

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

### Espaço entre Separadores e Aspas Duplas (Remoção)
Remove os dados caso tenha espaço entre os separadores e as aspas.

Caso seja:
```
"<data>";"<data>"; "<Lorem ipsum>";"<Lorem ipsum>"
```
Fica como:
```
"<data>";"<data>"
```

### Espaço entre Separadores e Aspas Duplas (Quebra)
Pega os dados que possuem espaços entre o separadores e entre uma aspas dupla e coloca uma quebra de linha no lugar.

Caso seja:
```
"<data>";"<data>"; "<data>";"<data>"
```
Fica como:
```
"<data>";"<data>"
"<data>";"<data>"
```

> **EXPORTAÇÃO**
>
> #### **main**
>
> [\\\\main]
>
>
> O arquivo 'main' é exportado nesse momento com todas as formatações realizadas acima.


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

> **EXPORTAÇÃO**
>
> #### **fullClear**
>
> [\\\\fullClear]
>
>
> O arquivo 'main' é exportado nesse momento com todas as formatações realizadas acima.