# Important
import requests
import re
from colorama import init
from colorama import Fore, Back, Style

# Inputs
Mobile = input(str("Enter Your Targets Number: "))
Key1 = input(str("Enter your Phone Validator API Key: "))
Key2 = input(str("Enter your NumVerify API Key: "))



# Verification
class Verification:
    Regex = "^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
    Match = re.match(Regex, Mobile)
    if Match == None:
        print("Bad Syntax.")
        exit()
    else:
        print("[+] Valid Syntax")



class OSint:



  class Pvalidator:



    User = "https://www.phonevalidator.com/api/v2/phonesearch?apikey=" + Key1 + "&phone=" + Mobile + "&type=basic,detail,deactivation"

    print("$ Looking " + Mobile + " Up...")
    Info = requests.get(User)

    if Info.status_code == 200:
        print("[+] Data Found\n" + Fore.RED + "https://www.phonevalidator.com/api/v2/phonesearch?apikey=" + Key1 + "&phone=" + Mobile + "&type=basic,detail,deactivation" + Style.RESET_ALL)
    else :
        print("None found for Phone Validator.")
        exit()



    class Numverify:
        
        
        
        User2 = "http://apilayer.net/api/validate?access_key=" + Key2 + "8&number=" + Mobile + "&country_code=US&format=1"
        Info2 = requests.get(User2)
        
        if Info2.status_code == 200:
            print("\n[+] Data Found\n" + Fore.RED + "http://apilayer.net/api/validate?access_key=" + Key2 + "8&number=" + Mobile + "&country_code=US&format=1")
        
        else:
            print("No data found for Numverify.")
    