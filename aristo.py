from collections import Counter
from string import ascii_lowercase, ascii_uppercase
from copy import deepcopy

with open("C:\\Users\\cl140\\OneDrive\\puzzling\\enigmas\\2024-03\\family_ties.txt") as inst:
    h = inst.read()


class Aristo:
    def __init__(self, ciphertext, name=None):
        self.__ctext__ = ciphertext
        self.__ptext__ = deepcopy(ciphertext)
        self.__trdict__ = {}
        self.__myname__ = str.strip(ciphertext[:8]) if name is None else name
        self.__solno__ = 0

    def print_freqs(self):
        print(Counter(self.__ctext__))
        return

    def guess_letters(self, guess_dict):
        poss_dict = {}
        # zip guess dictionary into a character-by-character table
        for k,v in guess_dict.items():
            if k not in poss_dict and k not in self.__trdict__:
                poss_dict.update(dict(zip(k,v)))
        # check keys against existing trdict
        
        # display string with substitutions
        temp_tr = poss_dict | self.__trdict__
        
        temp_trtb = str.maketrans(temp_tr)
        print(self.__ptext__.translate(temp_trtb))
        # get user input on quality
        input_choice = input("Keep this guess Y/N?")
        if input_choice.lower() == "y":
            self.__trdict__ |= poss_dict
            self.update_trtable()
        return(poss_dict)
    
    def update_trtable(self):
        # update internal trdict, trtable, and plain text from "good" guess
        # 
        self.__trtab__ = str.maketrans(self.__trdict__)
        pass

    def show_current_solution(self):
        print(self.__ptext__.translate(self.__trtab__))
        pass
    
    def save_solution(self):
        with open(f"sol_no{self.__solno__}_{self.__myname__}.txt", "w") as outf:
            print(self.__ptext__.translate(self.__trtab__), file=outf)
            print(self.__trdict__, file=outf)
        self.__solno__ += 1 
        return
    
        
