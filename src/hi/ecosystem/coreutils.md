+++
translation_kind = "translated"

title = "Coreutils"
section = "ecosystem"
order = 3
sources = [
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]


prose_hash = "sha256:b413d7a121a8c7e90239de4231360a6ce0ed3d98da0d5752cc0e5bb53490c34d"
code_hash = "sha256:738161c1d064c275b5fb317f3dd18f6cf674c347cbf6d95b5a3e5edcf69af505"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Faber GNU coreutils को एप्लिकेशन-लेन प्रूफ के रूप में फिर से लागू करता है। ये वास्तविक CLI प्रोग्राम हैं, जो argv, stdio, exit codes और host I/O के साथ काम करने वाले बाइनरी बनाने की Faber की क्षमता प्रदर्शित करते हैं। इन्हें parity harness के माध्यम से host की GNU utilities के विरुद्ध सत्यापित किया गया है।

## लागू की गई utilities {#implemented-utilities}

**चरण 1 — scaffold + true/false**  
`true`, `false`

**चरण 2 — साझा common helpers + inline tests**  
`echo`, `basename`, `dirname`, `printf`, `seq`

**चरण 3 — nullable-stdin slices**  
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,  
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**Scaffolded — चरण 5+**  
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,  
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

## उदाहरण — echo {#example--echo}

`echo` पैकेज coreutils में पूरे प्रोजेक्ट में उपयोग किए जाने वाले Faber पैटर्न प्रदर्शित करता है: CLI annotations, option parsing, `probandum`/`proba`/`adfirma` के साथ inline tests और साझा common modules:

```faber locale=la
importa ex "norma:consolum" privata consolum
importa ex "../../../common/gnu/format" privata gnu_format

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

## चलाना {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
