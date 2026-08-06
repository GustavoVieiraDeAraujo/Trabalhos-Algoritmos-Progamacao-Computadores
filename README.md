# Trabalhos de Algoritmos e Programacao de Computadores

Dois projetos maiores da disciplina **Algoritmos e Programacao de Computadores (APC)** do Departamento de Ciencia da Computacao da Universidade de Brasilia. Diferente dos exercicios individuais do repositorio irmao, cada um destes e um programa completo, operado por linha de comando, que integra varios topicos da materia (condicionais, funcoes, listas, dicionarios, leitura de arquivos) para resolver um problema realista de gestao academica inspirado no SIGAA.

> Os 90 exercicios individuais da mesma disciplina estao em [Exercicios-Algoritmos-Progamacao-Computadores](https://github.com/GustavoVieiraDeAraujo/Exercicios-Algoritmos-Progamacao-Computadores).

---

## Sumario

- [Trabalhos de Algoritmos e Programacao de Computadores](#trabalhos-de-algoritmos-e-programacao-de-computadores)
  - [Sumario](#sumario)
  - [Participantes](#participantes)
  - [Tecnologias](#tecnologias)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Diferenca Entre as Versoes](#diferenca-entre-as-versoes)
  - [Requisitos](#requisitos)
  - [Como Executar](#como-executar)
  - [Projeto 1: Grade Horaria](#projeto-1-grade-horaria)
  - [Projeto 2: Lista de Oferta](#projeto-2-lista-de-oferta)

---

## Participantes

| Nome | Matricula |
|---|---|
| Gustavo Vieira de Araujo | 211068440 |

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem de implementacao dos dois projetos |
| `csv` (biblioteca padrao) | Leitura e parsing dos arquivos CSV de oferta de disciplinas no Projeto 2 |

---

## Estrutura do Projeto

| Diretorio | Descricao |
|---|---|
| `Projeto 1/` | Versao original entregue, tal como submetida (`( 70% funcional )`) |
| `Projeto 2/` | Versao original entregue, ja com o bug de busca por nome de docente corrigido (ver [Bugs Corrigidos](#bugs-corrigidos)) |
| `Projeto 1 Corrigido/` | Versao corrigida do Projeto 1, sem a limitacao estrutural da versao original |
| `Projeto 2 Corrigido/` | Copia validada do Projeto 2, com o mesmo comportamento de `Projeto 2/` |

Cada pasta contem o `Enunciado.PNG` (especificacao completa do problema), um ou mais `Exemplos.PNG` (casos de teste oficiais) e o `Resposta.py` com a solucao. As pastas do Projeto 2 tambem incluem `arquivos_csv.zip`, com os datasets reais de oferta de disciplinas usados nos exemplos.

---

## Diferenca Entre as Versoes

O repositorio mantem as duas versoes lado a lado de proposito: as pastas sem sufixo sao a entrega original, preservadas como historico; as pastas `Corrigido` sao a correcao feita depois.

| | `Projeto 1/` | `Projeto 1 Corrigido/` |
|---|---|---|
| Passa nos exemplos do enunciado | Sim, todos | Sim, todos |
| Remocao parcial de disciplina multi-dia | **Falha**: remove o dia todo em vez de so o dia pedido (ver explicacao abaixo) | Corrigida: remove exatamente o(s) dia(s) pedido(s) |
| Modelo interno de dados | Agrupa horarios por turno compartilhado entre dias (uma unica entrada para "terca+quinta", por exemplo) | Um dicionario `grade[(dia, horario)] = codigo`, uma entrada por posicao real da tabela |
| Comportamento externo (comandos, formato de saida) | - | Identico ao original |
| Rotulo do proprio autor | `( 70% funcional )` | - |

| | `Projeto 2/` | `Projeto 2 Corrigido/` |
|---|---|---|
| Passa nos exemplos do enunciado | Sim, todos | Sim, todos |
| Bugs conhecidos | Nenhum (bug de busca por nome parcial de docente ja foi corrigido nesta pasta) | Nenhum |
| Codigo | Igual ao `Corrigido` | Igual ao original |

Ou seja: para o Projeto 2 as duas pastas sao equivalentes (o codigo ja estava correto). Para o Projeto 1, a diferenca e real: a pasta sem sufixo reproduz fielmente o bug estrutural da entrega original (documentado abaixo), e a pasta `Corrigido` o corrige de verdade.

**Por que a versao original ainda existe, com o bug**: para preservar o historico real da entrega, com o rotulo `( 70% funcional )` no nome do arquivo original e do proprio autor, reconhecendo a limitacao na epoca da entrega. Apagar ou sobrescrever essa versao apagaria esse registro.

---

## Requisitos

| Dependencia | Versao | Instalacao |
|---|---|---|
| Python | 3.8+ | `sudo apt install python3` (ou equivalente da distribuicao) |

Nenhuma dependencia externa (`pip`) e necessaria: ambos os projetos usam apenas a biblioteca padrao.

---

## Como Executar

Cada projeto e executado a partir de dentro da propria pasta (para que os arquivos auxiliares que ele le sejam encontrados). Versao original, como entregue:

```bash
cd "Projeto 1"
python3 "Resposta Projeto 1 ( 70% funcional ).py"

cd "Projeto 2"
unzip -o arquivos_csv.zip   # extrai os CSVs de exemplo citados no Enunciado
python3 "Resposta Projeto 2.py"
```

Versao corrigida:

```bash
cd "Projeto 1 Corrigido"
python3 "Resposta Projeto 1.py"

cd "Projeto 2 Corrigido"
unzip -o arquivos_csv.zip
python3 "Resposta Projeto 2.py"
```

---

## Projeto 1: Grade Horaria

Simulador de um sistema de gerenciamento de grade horaria semanal (apelidado no enunciado de "SAD: Sistema de Apoio ao Discente"), operado por comandos de texto lidos linha a linha via `stdin`:

| Comando | Efeito |
|---|---|
| `+ COD DTH1 ... DTHn` | Adiciona a disciplina `COD` nos horarios informados |
| `- COD DTH1 ... DTHn` | Remove a disciplina `COD` dos horarios informados |
| `?` | Imprime a grade horaria semanal atual, formatada como tabela |
| `Hasta la vista, beibe!` | Encerra o programa |

**Formato de codigo de disciplina (`COD`)**: `xxx####Y`, onde `xxx` identifica a unidade responsavel (ex.: `CIC` = Departamento de Ciencia da Computacao), `####` e o codigo numerico da disciplina, e `Y` a turma. Exemplo: `CIC0004B`.

**Formato de horario (`DTH`)**: `DTH` onde `D` sao os dias da semana (`2`=segunda, `3`=terca, `4`=quarta, `5`=quinta, `6`=sexta, `7`=sabado, podendo haver mais de um digito para o mesmo horario), `T` e o turno (`M`=matutino, `T`=vespertino, `N`=noturno) e `H` sao os creditos/horarios dentro daquele turno. Exemplo: `35M12` significa terca e quinta (`3` e `5`), no periodo da manha (`M`), nos horarios 1 e 2 (08:00–09:50).

Exemplo de interacao completa:

```
→ + CIC0004B 35M12
→ ?
← +---------------+----------+----------+----------+----------+----------+----------+
← |               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |
← +---------------+----------+----------+----------+----------+----------+----------+
← | 08:00 - 08:55 |          | CIC0004B |          | CIC0004B |          |          |
← +---------------+----------+----------+----------+----------+----------+----------+
← | 08:55 - 09:50 |          | CIC0004B |          | CIC0004B |          |          |
← +---------------+----------+----------+----------+----------+----------+----------+
→ + MAT0025B 3M12
← !(+ MAT0025B 3M12)
→ Hasta la vista, beibe!
```

(A segunda tentativa de adicionar `MAT0025B` no mesmo horario de terca 08:00–09:50 e rejeitada com `!(instrucao)`, por conflito de horario com `CIC0004B`.)

**O bug corrigido, na pratica** (`Projeto 1/` vs. `Projeto 1 Corrigido/`):

```
→ + CIC0004B 35M12        (cadastra terca e quinta)
→ - CIC0004B 3M12         (pede para remover so a terca)
→ ?
```

Na versao original, esse `?` mostra a grade **vazia**: a remocao de "so terca" removeu a disciplina inteira, inclusive a quinta-feira que nao foi pedida. Na versao corrigida, o mesmo `?` mostra **quinta-feira ainda ocupada por `CIC0004B`**, e so a terca foi liberada, o comportamento correto segundo o enunciado.

---

## Projeto 2: Lista de Oferta

Sistema de consulta da oferta de disciplinas de um departamento a partir de arquivos CSV exportados do SIGAA (apelidado no enunciado de "SAAD: Sistema de Acompanhamento e Analise Docente"), operado por comandos de texto:

| Comando | Efeito |
|---|---|
| `leia ARQ` | Carrega um arquivo CSV de oferta na memoria, somando-o aos ja lidos anteriormente |
| `carga DOCENTE` | Lista a carga horaria total de um docente, por disciplina e turma, considerando apenas turmas com pelo menos 6 alunos matriculados |
| `disciplina D` | Lista disciplinas com pelo menos `D` (`D ≥ 0`) docentes responsaveis distintos |
| `matriculas COD1 COD2 ... CODn` | Soma o total de alunos matriculados por disciplina informada, em ordem decrescente |
| `FIM` | Encerra o programa |

**Formato do CSV de entrada**: cada linha representa uma turma ofertada, com as colunas `Código, Nome, Turma, Ano-Período, Docente, Horário, Qtde Vagas Ofertadas, Qtde Vagas Ocupadas, Local`. O campo `Docente` inclui a carga horaria entre parenteses (ex.: `JORGE CARLOS LUCERO (60h)`).

Exemplo de interacao (a partir do dataset `CIC20211.csv` incluso em `arquivos_csv.zip`):

```
→ leia CIC20211.csv
→ carga DIBIO LEANDRO BORGES
← DIBIO LEANDRO BORGES:
←  * INTRODUCAO A INTELIGENCIA ARTIFICIAL (CIC0135):
←      Turma A: 60h (33 alunos)
←  * TEORIA E APLICAÇÃO DE GRAFOS (CIC0199):
←      Turma 02: 60h (1 alunos)
←      Turma A: 60h (27 alunos)
← [Carga total considerada: 120h (2.00h/aluno)]
→ FIM
```

Todos os 5 exemplos fornecidos no enunciado foram executados e conferidos caractere a caractere contra a saida esperada, alem de casos extras (arquivo inexistente, codigo de disciplina desconhecido, `disciplina 0`, busca por nome parcial de docente). Um bug real foi encontrado e corrigido, ver abaixo.

---

> Documentacao gerada com auxilio de IA.
