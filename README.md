# Coptic Orthographic Profiles

This collects python methods to automatically generate phonetic transcriptions of Coptic words.

## Getting Started

### Prerequisites

You need Python, of course ;-)

...and it has to be Python 3.

And you need unicode-based transcriptions of Coptic words to parse...


### Installing

Each orthographic profile is provided as a standalone python file containing a standrd python method. Just add it to your project and import the method as usual.

## Running the tests

The file tester.py provides an implementation of the available phonetic profiles

It can be run from command line with:

```shell
python tester.py
```

The results should look like this:

```shell
* =====
* Parse: ⲃⲣⲕⲟⲟⲩⲧ
* Parser: copticPanDialect_1_0
* =====


Results:

Coptic form: ⲃⲣⲕⲟⲟⲩⲧ
Phonemes: b.r.k.o.w.t
Nr of vowels: 1
Nr of consonants: 5
Phoneme classes: C.C.C.V.C.C
Stress: 0.0.0.S.0.0
Vowel Length: 0.0.0.S.0.0

As a dictionary:

{'CopticForm': 'ⲃⲣⲕⲟⲟⲩⲧ', 'Phonemes': 'b.r.k.o.w.t', 'NrVowels': 1, 'NrConsonants': 5, 'PhonemeClasses': 'C.C.C.V.C.C', 'Stress': '0.0.0.S.0.0', 'VowelLength': '0.0.0.S.0.0'}

------

* =====
* Parse: ϣⲓⲕⲉ
* Parser: copticSahidic_1_0
* =====


Results:

Coptic form: ϣⲓⲕⲉ
Phonemes: ʃ.ī.k.ə
Nr of vowels: 2
Nr of consonants: 2
Phoneme classes: C.V.C.V
Stress: 0.S.0.U
Vowel Length: 0.L.0.u

As a dictionary:

{'CopticForm': 'ϣⲓⲕⲉ', 'Phonemes': 'ʃ.ī.k.ə', 'NrVowels': 2, 'NrConsonants': 2, 'PhonemeClasses': 'C.V.C.V', 'Stress': '0.S.0.U', 'VowelLength': '0.L.0.u'}
```

The single profiles can be run from command line, from the folder in which they are located, using the following command:

```shell
python -c 'from copticPanDialect_1_0 import parseCopticPanDialect; parseCopticPanDialect(word_to_parse, True)'
```

where "word_to_parse" is the unicode Coptic word to parse.

## Profiles

### PanDialect profile

Version 1.0

Date of publication: 06.01.2020

For details, see:

[PanDialect Profile - Read me](parsers/PanDialect)

#### Description

General profile based on Shaidic orthography but able to recognize also non-Sahidic caracters (e.g. aspirated consonants) and which translate final unstressed ⲓ as j|ɨ, where the j reflecs dialects like Sahidic in which unstressed final ⲓ usually represent a glide, while the ɨ reflects dialects like Bohairic in which final ⲓ can represennt an unstressed reduced final vowel.

#### How to cite

Kilani Marwan, 2019, Coptic Orthographic Profiles - PanDialect profile, https://github.com/MKilani/Coptic_Orthographic_Profiles


### Sahidic profile

Version 1.0

Date of publication: 14.10.2019

For details, see:

[Sahidic Profile - Read me](parsers/Sahidic)

#### Description

Same as the PanDialect profile, except for final unstressed  ⲓ , which are always transcribed as j, rather than as j|ɨ , as expected in accurate Sahidic orthography.

#### How to cite

Kilani Marwan, 2019, Coptic Orthographic Profiles - Sahidic profile, https://github.com/MKilani/Coptic_Orthographic_Profiles

## Authors

* **Marwan Kilani** - Swiss National Science Foundation (Mobility Grant) - Freie Universität Berlin (2019)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

