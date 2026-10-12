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

<<<FENCE 0>>>

## चलाना {#running}

<<<FENCE 1>>>
