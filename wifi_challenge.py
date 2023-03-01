from getmac import get_mac_address
### GLOBAL VARIABLES ###
props_dict = {}




### FUNCTIONS ###
def init(props):
    global props_dict
    print("Python: starting challenge init()")

    # Save properties in the global variable
    props_dict = props
    
    # Execute the challenge once during the init, so key is calculated from the beginning
    executeChallenge()
    return 0




def executeChallenge():
    print("Python: starting executeChallenge()")

    # The key will be 0000 or MAC depending on if the device is within the network or not
    cad = ""

    hostname=""
    ip="172.26.2.44"
    mac=get_mac_address(ip=ip,network_request=True)
    #mac=get_mac_address(hostname=hostname, network_request=True)

    if ("00:be:43:13:38:c8"==mac):
        cad=mac
    else:
        cad='0000'

    # Get key as UTF-8 and calculate its length
    key = bytes(cad, 'utf-8')
    key_size = len(key)

    # The result is a tuple (key, key_size)
    result = (key, key_size)
    print("Python:", result)

    return result


if __name__ == "__main__":
    # Use a dictionary as example of properties obtained from the json
    props_example_dict = {"param1": "hola", "param2": 3}
    init(props_example_dict)
    executeChallenge()








