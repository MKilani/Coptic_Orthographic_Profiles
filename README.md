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

### Sahidic profile

Version 1.0

Date of publication: 14.10.2019

For details, see:

[Sahidic Profile - Read me](parsers/Sahidic)

#### How to cite

Kilani Marwan, 2019, Coptic Orthographic Profiles - Sahidic profile, https://github.com/MKilani/Coptic_Orthographic_Profiles

#### Phonetic equivalences:

|   |   |   |   |
|---|---|---|---|
| ⲃ = b | ⲕ = k | ⲣ = r | ϣ = ʃ | 
| ⲅ = g | ⲗ = l | ⲥ = s | ϥ = f |
| ⲇ = d | ⲙ = m | ⲧ = t | ϧ = x | 
| ⲋ = s | ⲛ = n | ⲫ = pʰ | ϩ = h | 
| ⲍ = z | ⲝ = ks | ⲭ = kʰ | ϫ = c |
| ⲑ = tʰ | ⲡ = p | ⲯ = ps | ϭ = kʲ |  

|   |   |   |
|---|---|---|
| ⲁ = ă / a | ⲉ = ə / e | ⲟ = o |
| ⲁⲩ = aw | ⲏ = ē | ⲱ = ō |
| ⲉⲩ = ew | ⲓ / ⲉⲓ = j / ī | ⲟⲩ = w / ū |

ⲓⲉⲓ / ⲓⲓ = ij

double vowel = vowel + ʔ

0 stressed vowel in words spelled only with consonant = e ( e.g. ⲧⲃⲧ = tebt )

#### Format of the output

The output is a dictionary with the following entries:

```
* CopticForm : word to be barsed (spelled in unicode) - string
* Phonemes : phonetic transcription - string
	* phonemes are divided by . (dot)
	* long vowels are marked by a macron
	* pretonic unstressed /a/ is marked with <ă>
	* in ambigous cases, alternative options are separated by the sign |
* NrVowels : number of vowels identified in the word - integer
* NrConsonants : number of vowels identified in the word - integer
* PhonemeClasses : analysis of the phonemes in the word - string
	* C = consonant
	* V = vowel
	* W = ambigous cases (j|ī and w|ū)
	* v = ambigous cases in which the presence of the vowel is not certain
* Stress : analysis of the stress position - string
	* 0 = consonant (no stress)
	* S = stressed vowel
	* U = unstressed vowel
	* u = ambigous cases
* VowelLength : analysis of the length of the vowels - string
	* 0 = consonant (no vocalic length)
	* L = stressed long vowel
	* S = stressed short vowel
	* u = unstressed vowel (reduced, so no length)
	* l = ambigous cases (j|ī and w|ū)
```

## Authors

* **Marwan Kilani** - Swiss National Science Foundation (Mobility Grant) - Freie Universität Berlin (2019)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

