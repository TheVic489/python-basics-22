from dataclasses import replace
from pathlib import Path
import utils


# Student name: WRITE YOUR NAME BELOW
# -----------------------------------------------------------------------------
name:    str = "Victor"
surname: str = "Piñana"
assert name and surname, 'Error: Please write your name and surname.'
# -----------------------------------------------------------------------------

# E1
# -----------------------------------------------------------------------------
# 1. Fes quatre classes: Seq, DNASeq, RNASeq, Protein.
# 2. DNASeq, RNASeq i Protein han d'heretar de Seq.
# 3. Codifica els atributs i els mètodes necessaris per tal que
#   passin tots els tests que hi ha a l'arxiu 'e1_test.py'.
# 4. Executeu els tests amb l'ordre: pytest -v
# 5. A l'arxiu 'utils.py' teniu codi que us pot ajudar.
# 6. Tot el codi ha d'estar a les classes o a utils.py.
# 7. En cap cas poseu codi a la secció Main. Us donarà problemes en executar pytest.
# -----------------------------------------------------------------------------


# Classes
# -----------------------------------------------------------------------------
# WRITE YOUR CODE HERE

class Seq:
    def __init__(self, seq:str):
        self.seq: str = seq
    
    def __str__(self) -> str:
        return f"{self.seq}"
    
    def __len__(self):
        return len(self.seq)

    @classmethod
    def from_fasta(cls, fasta_file_path: str):
        
        fasta_text:      str  = Path(fasta_file_path).read_text()
        line_list:  list[str] = fasta_text.strip().splitlines()
        body:   list[str] = line_list[1:]

        seq: str  = ''.join(body)

        return cls(seq)

class Protein(Seq):
    def __init__(self, seq: str):
        super().__init__(seq)
        
        for base in range(len(self.seq)):
            if self.seq[base] not in utils.AA_LETTERS:
                raise Exception


class RNASeq(Seq):
    def __init__(self, seq: str):
        super().__init__(seq)
       
        try:
            T_excp: Exception("Hay T en el RNA recibido")
            if "T" in self.seq:
                raise T_excp
        except:
             self.seq.replace('T', 'U')

    def translate(self):
        # NO VA
        a = 0
        for key, value in utils.AMINO.items():
            if self.seq[a:] == key: 
                result_1: str = self.seq.replace(self.seq[a:], value, 3)
                result_2: str = "".join(result_1)
                a + 4
        return result_2


class DNASeq(Seq):
    def __init__(self, seq: str):
        super().__init__(seq)    
        try:
            T_excp: Exception("Hay T en el RNA recibido")
            if "U" in self.seq:
                raise T_excp
        except:
             self.seq.replace('U', 'A')
            
    
    def transcribe(self):
        return self.seq.replace('T','U')


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    RNA: RNASeq = RNASeq("ASDASDASDT")
    DNA: DNASeq = DNASeq("ASDASDADT")

    print(RNA, DNA, sep="\n")
    # Write your solution inside classes.
    # Code here is NOT evaluated.

# -----------------------------------------------------------------------------
