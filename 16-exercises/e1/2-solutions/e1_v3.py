from   pathlib import Path
import engine

"""
Exercici 1:

- Fes un programa que enviï invitacions a una llista d'amics.
- Utilitza engine.py
- Utilitza els fitxers friends.txt i letter.txt
- Modifica letter.txt utilitzant Jinja.
"""


"""
1. Dividir el problema en subproblemes fàcils de resoldre.
   (Disseny Top-Down -> Disseny Bottom-Up)
   (Següent iteració: Més funcional)

a. Llegir la llista d'amics
b. Crear llista d'invitacions
c. Escriure cada invitació a un fitxer {amic}.txt

2. Escriure una funció que resoldrà cada subproblema.
   Escriure els paràmetres d'entrada i de sortida.

3. Escriure les precondicions i postcondicions
   de cada paràmetre per a cada funció.
"""



# - friends_file ha d'existir i ser llegible. Si no el programa fallarà.
# - friends_file ha de tenir el nom d'un amic a cada línia.
# - friends_list ha de tenir tots els noms que hi ha a friends_file.
# - friends_list no ha de tenir noms en blanc.
# -----------------------------------------------------------------------------
def read_friends(friends_filename: str) -> list[str]:

    friends_filepath: Path      = Path(friends_filename)
    friends_text:     str       = friends_filepath.read_text()
    friends_list:     list[str] = friends_text.split()

    return friends_list


# - letter_template_filename ha d'existir al directori actual i ser llegible.
# - Posar el nom de l'amic a la plantilla.
# - Retorna la invitació com a un string.
# -----------------------------------------------------------------------------
def make_invitation(friend: str, letter_template_filename: str) -> str:

    template_dir: Path = Path('.')
    vars_dict:    dict = {'friend': friend}
    invitation:   str  = engine.fill_template(template_dir, letter_template_filename, vars_dict)

    return invitation


# - friends_list i invitations_list tenen el mateix tamany.
# -----------------------------------------------------------------------------
def write_invitations(friends_list: list[str], invitations_list: list[str]):

    tuple_list: list[tuple[str, str]] = list(zip(friends_list, invitations_list))

    for friend, invitation in tuple_list:
        Path(f"{friend}.txt").write_text(invitation)


# Main
# -----------------------------------------------------------------------------
letter_template_fn: str       = 'letter.txt'
friends_list:       list[str] = read_friends('friends.txt')
invitations_list:   list[str] = [make_invitation(friend, letter_template_fn) for friend in friends_list]
write_invitations(friends_list, invitations_list)
# -----------------------------------------------------------------------------
