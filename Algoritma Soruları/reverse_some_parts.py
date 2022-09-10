'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):

    # Her bir kelimeyi (boşluk karakterine split edilmiş) ilk ve son karakterini kontrol ediyorum. 
    # "(..)" durumundaki kelimelerde parantezlerden kurtuluyorum. Diğer kelimelerin tersini alıyorum.
    clean_text = " ".join([i[1:-1] if ((i.startswith("(")) and (i.endswith(")"))) else i[::-1] for i in mystr.split()])
    print(clean_text)
    return clean_text

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
