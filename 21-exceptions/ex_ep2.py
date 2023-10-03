

def get_seq():
    input_adn: str = input('Put a ADN sequence: ')
    
    try:
        if len(input_adn) % 3 == 0:
            print(f"Sequence succesfuly Inputted \n ADN sequence: {input_adn}")
            
        else :
            raise Exception
        
    except: raise Exception('Invalid ADN seq, try again.')


if __name__ == "__main__":

    get_seq()