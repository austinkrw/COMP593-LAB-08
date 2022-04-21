import requests

def retrievePokeDic(pokeName):

    """
    :param name: Pokemon's name/Poke index #
    """
    # removes leading and trailing spaces and converts the pokeName to lowercase
    pokeName = pokeName.lower().strip()

    # connects to the PokeAPI page for the pokemon specified as a command line parameter for main()
    # and makes a GET request    
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokeName)

    print("Connecting to PokeAPI . . .", end = "")
    
    # if connection is successful assign the pokemon info to a dictionary
    if response.status_code == 200:
        print(' Success!')
        pokeInfo = response.json()
        return pokeInfo
    else:
        print(' Error', sep = "")