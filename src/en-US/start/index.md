+++
title = "Start"
section = "start"
order = 0
sources = []
+++

Faber is written by models, so you install it by handing your model a link.

::agent-pass::

## What your model does {#what-your-model-does}

1. Reads the lobby file at that link, which says what Faber is and where each step lives.
2. Downloads the current release for your machine and verifies its checksum.
3. Installs the `faber` command.
4. Writes a small hello program and runs `faber check` on it.

All of this happens on your own machine, and your model tells you when the
check passes.

## Then ask it for something {#then-ask}

Once the check passes, talk to your model the way you would to a colleague.
Each prompt below has a copy button.

Write a program and have it explained:

```text prompt
Write a small Faber program that prints the first ten square numbers. Check it with faber check, run it with faber run, then explain each line to me.
```

Bring in code you already have:

```text prompt
Here is a function I already have: <paste it here>. Translate it into Faber, check it, then build it for Rust with faber build -t rust and tell me what changed.
```

Read it in another language:

```text prompt
Make a copy of the hello program spelled in Thai with faber convert --to th-TH. Check the copy, then show me both versions side by side.
```

See what a compiler error says:

```text prompt
Break the hello program on purpose by giving a value the wrong type. Run faber check, read me the diagnostic, and use faber explain on its code so I can see what it means.
```

## Read along {#read-along}

You do not need to write Faber to read it. These pages show what your model
writes and why it looks the way it does.

- [Language overview](/language/overview.html): one real program, what the language gives you, and where it compiles.
- [Cheat sheet](/cheatsheet/): short examples of how Faber is written, and the `faber` commands, one page per topic.
- [Terms A–Z](/corpus/az.html): every keyword and term, with examples.
- [Reader locales](/language/reader-locales.html): the same program in eight language surfaces.
