from Translator_bilingue import TranslatorBilingue

if __name__== "__main__":

    machine = TranslatorBilingue("cc.ar.300.vec","cc.en.300.vec","arabic" ,"english")

    data1 = machine.load_vectors()