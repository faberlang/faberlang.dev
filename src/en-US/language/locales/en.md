+++
title = "English reader locale"
section = "locales"
order = 10
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**English** — the `en` reader pack. Script: Latin; direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `en` |
| **Native name** | English |
| **Script** | Latin |
| **Direction** | left-to-right |

A base surface: English keywords map to the English word, so its reader spelling is also what an English reader writes.

Because English is a base surface, this page's two columns carry the same spelling: the English reader word is the canonical pack value for English.

## English ↔ English {#mapping}

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          English
| ---------------  ---------------
| all              all
| and              and
| any              any
| argmax           argmax
| argmin           argmin
| args             args
| as               as
| assert           assert
| async            async
| async_generator  async_generator
| async_main       async_main
| async_setup      async_setup
| async_teardown   async_teardown
| at               at
| await            await
| await_const      await_const
| await_var        await_var
| before           before
| bench            bench
| between          between
| break            break
| call             call
| case             case
| catch            catch
| class            class
| cli              cli
| coalesce         coalesce
| column           column
| command          command
| comptime         comptime
| const            const
| continue         continue
| conversion       conversion
| —                —
| copy             copy
| count            count
| cursor           cursor
| debug            debug
| default          default
| describe         describe
| description      description
| do               do
| elif             elif
| else             else
| embed            embed
| empty            empty
| enum             enum
| errors           errors
| exit             exit
| expect_failure   expect_failure
| false            false
| flaky            flaky
| fn               fn
| for              for
| format           format
| fragment         fragment
| free             free
| from             from
| future           future
| generator        generator
| global           global
| guard            guard
| if               if
| implements       implements
| import           import
| interface        interface
| internal         internal
| is               is
| kernel           kernel
| lambda           lambda
| lane             lane
| let              let
| line             line
| long             long
| main             main
| match            match
| max              max
| min              min
| module           module
| mut              mut
| name             name
| nan              nan
| nihil            nihil
| not              not
| null             null
| only             only
| only_in          only_in
| operand          operand
| option           option
| optional         optional
| options          options
| or               or
| own              own
| panic            panic
| pass             pass
| per              per
| primus_quem      primus_quem
| print            print
| private          private
| product          product
| protected        protected
| public           public
| radix            radix
| range            range
| read             read
| readonly         readonly
| reduce           reduce
| ref              ref
| reject           reject
| rename           rename
| repeat           repeat
| require          require
| rest             rest
| return           return
| return_await     return_await
| schema           schema
| self             self
| setup            setup
| shared           shared
| short            short
| size             size
| skip             skip
| spread           spread
| static           static
| step             step
| sum              sum
| switch           switch
| tag              tag
| teardown         teardown
| test             test
| then             then
| thread           thread
| throw            throw
| throws           throws
| timeout          timeout
| todo             todo
| trap             trap
| true             true
| tuple            tuple
| type             type
| ubi              ubi
| union            union
| unstable         unstable
| until            until
| var              var
| variant          variant
| vertex           vertex
| via              via
| warn             warn
| while            while
| within           within
| wrapping         wrapping
| write            write
| yield            yield
```

### Types {#types}

```text locale=la
| English      English
| -----------  -----------
| any          any
| ascii        ascii
| atomic       atomic
| bool         bool
| byte         byte
| bytes        bytes
| census       census
| channel      channel
| char         char
| filter       filter
| float        float
| frame        frame
| instant      instant
| int          int
| intervallum  intervallum
| iterator     iterator
| json         json
| list         list
| map          map
| matrix       matrix
| never        never
| none         none
| object       object
| promise      promise
| queue        queue
| record       record
| recv         recv
| regex        regex
| saturating   saturating
| send         send
| series       series
| set          set
| sparsa       sparsa
| stack        stack
| string       string
| tensor       tensor
| trapping     trapping
| unknown      unknown
| value        value
| vector       vector
| void         void
| wrapping_ty  wrapping_ty
```

### Intrinsics {#intrinsics}

```text locale=la
| English               English
| --------------------  --------------------
| abs                   abs
| add                   add
| added                 added
| added_bias            added_bias
| all                   all
| any                   any
| append                append
| apply                 apply
| approx                approx
| argmax                argmax
| argmin                argmin
| at_least              at_least
| at_most               at_most
| bit_and               bit_and
| bit_and_assign        bit_and_assign
| bit_or                bit_or
| bit_or_assign         bit_or_assign
| ceiling               ceiling
| clamp                 clamp
| compare_exchange      compare_exchange
| complement            complement
| complemented          complemented
| contains              contains
| cos                   cos
| create                create
| cross                 cross
| cross_entropy         cross_entropy
| cumulate              cumulate
| cursor                cursor
| delete                delete
| densify               densify
| difference            difference
| divide                divide
| divide                divide
| divided               divided
| dot                   dot
| drop                  drop
| end                   end
| ends_with             ends_with
| escape                escape
| exchange              exchange
| exp                   exp
| fill                  fill
| filter                filter
| find                  find
| find_all              find_all
| first                 first
| flatten               flatten
| flip                  flip
| flipped               flipped
| floor                 floor
| formata               formata
| from_flat             from_flat
| gather                gather
| gelu                  gelu
| get                   get
| greater               greater
| group                 group
| has                   has
| intersect             intersect
| intersection          intersection
| invert                invert
| is_empty              is_empty
| is_subset             is_subset
| is_superset           is_superset
| keys                  keys
| last                  last
| layer_norm            layer_norm
| length                length
| less                  less
| ln                    ln
| load                  load
| log10                 log10
| lowercase             lowercase
| map                   map
| matches               matches
| materialize           materialize
| matmul                matmul
| maximum               maximum
| mean                  mean
| minimum               minimum
| modulo                modulo
| modulo_assign         modulo_assign
| multiplied            multiplied
| multiply              multiply
| named                 named
| negate                negate
| negated               negated
| nonzero_count         nonzero_count
| normalize             normalize
| power                 power
| put                   put
| reduce                reduce
| relu                  relu
| remove_first          remove_first
| remove_last           remove_last
| replace               replace
| reshape               reshape
| reverse               reverse
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 round
| set                   set
| shape                 shape
| shift_left            shift_left
| shift_right           shift_right
| shifted_left          shifted_left
| shifted_right         shifted_right
| sign                  sign
| silu                  silu
| sin                   sin
| slice                 slice
| softmax               softmax
| sort                  sort
| sorted                sorted
| split                 split
| sqrt                  sqrt
| start                 start
| starts_with           starts_with
| store                 store
| subtract              subtract
| subtracted            subtracted
| sum                   sum
| swizzle               swizzle
| symmetric_difference  symmetric_difference
| take                  take
| take_last             take_last
| tan                   tan
| text                  text
| transpose             transpose
| trim                  trim
| truncate              truncate
| union                 union
| union                 union
| uppercase             uppercase
| values                values
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
