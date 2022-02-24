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

a. Llegir la llista d'amics
b. Per cada amic:
   Crear la seva invitació
c. Creació d'invitacions
   d. Posar el nom de l'amic a la plantilla
   e. Guardar el text en un fitxer amb el nom de l'amic.

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
# - No hi ha paràmetre de sortida. S'escriu directament a disc.
# - Posar el nom de l'amic a la plantilla.
# - Guardar el text en un fitxer que es digui "nom de l'amic".txt
# -----------------------------------------------------------------------------
def write_invitation(friend: str, letter_template_filename: str):

    template_dir: Path = Path('.')
    vars_dict:    dict = {'friend': friend}

    invitation:   str  = engine.fill_template(template_dir, letter_template_filename, vars_dict)

    invitation_filename: str  = f"{friend}.txt"
    invitation_filepath: Path = Path(invitation_filename)
    invitation_filepath.write_text(invitation)


# - friends_list té els noms dels amics.
# - letter_template_filename ha d'existir al directori actual i ser llegible.
# - No hi ha paràmetre de sortida. S'escriu directament a disc.
# - Per cada amic:
#    - Posar el seu nom a la plantilla
#    - Guardar el text en un fitxer amb el nom de l'amic.
# -----------------------------------------------------------------------------
def write_invitations(friends_list: list[str], letter_template_filename: str):

    for friend in friends_list:
        write_invitation(friend, letter_template_filename)


# Main
# -----------------------------------------------------------------------------
friends_list: list[str] = read_friends('friends.txt')
write_invitations(friends_list, 'letter.txt')
# -----------------------------------------------------------------------------
