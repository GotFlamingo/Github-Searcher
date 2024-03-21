import requests
import os
from os import system
import time
from colorama import Fore
import ctypes


logo = f'''{Fore.LIGHTMAGENTA_EX}
   ___
 ,'   `.
/_. _,. \\
( /('   \ :
\\|    / ;
 `'   / /
     / /
    : :
    | :    {Fore.LIGHTYELLOW_EX}_______{Fore.LIGHTMAGENTA_EX}
    :  \\ {Fore.LIGHTYELLOW_EX},'       `-.{Fore.LIGHTMAGENTA_EX}
     '   {Fore.LIGHTYELLOW_EX}/    .  .  .  \\{Fore.LIGHTMAGENTA_EX}
      :  {Fore.LIGHTYELLOW_EX}`' ;  ;  ;  ; , :{Fore.LIGHTMAGENTA_EX}
       \\{Fore.LIGHTYELLOW_EX}\`./  /  /  / ; ;;{Fore.LIGHTMAGENTA_EX}
        `.{Fore.LIGHTYELLOW_EX}`'../__/ / ,.\\{Fore.LIGHTMAGENTA_EX}
           `'-.____;-'`\\\\\\{Fore.LIGHTMAGENTA_EX}
               \\ //   / '|{Fore.LIGHTMAGENTA_EX}
                ::\\    \\{Fore.LIGHTYELLOW_EX}
                ||\\\\{Fore.LIGHTYELLOW_EX}
                || \\
                ||  )){Fore.LIGHTYELLOW_EX}
                || //{Fore.LIGHTYELLOW_EX}
                ||//{Fore.LIGHTYELLOW_EX}
                ||/{Fore.LIGHTYELLOW_EX}
                ||
               /||
               `||-
             __,'; 
'''

logo2 = f'''{Fore.LIGHTMAGENTA_EX}            .-.
           ((`-)
            \\
             \\
      .="""==._))
     /  .,   .'
    /__(,_.-'
   `    /|
       /_|__
         | `))
         |
{Fore.LIGHTGREEN_EX}Made by GoT Flamingo
{Fore.LIGHTYELLOW_EX}GitHub: github.com/gotflamingo'''


# {
#  "login": "GotFlamingo",
#  "id": 126965713,
#  "node_id": "U_kgDOB5FX0Q",
#  "avatar_url": "https://avatars.githubusercontent.com/u/126965713?v=4",
#  "gravatar_id": "",
#  "url": "https://api.github.com/users/GotFlamingo",
#  "html_url": "https://github.com/GotFlamingo",
#  "followers_url": "https://api.github.com/users/GotFlamingo/followers",
#  "following_url": "https://api.github.com/users/GotFlamingo/following{/other_user}",
#  "gists_url": "https://api.github.com/users/GotFlamingo/gists{/gist_id}",
#  "starred_url": "https://api.github.com/users/GotFlamingo/starred{/owner}{/repo}",
#  "subscriptions_url": "https://api.github.com/users/GotFlamingo/subscriptions",
#  "organizations_url": "https://api.github.com/users/GotFlamingo/orgs",
#  "repos_url": "https://api.github.com/users/GotFlamingo/repos",
#  "events_url": "https://api.github.com/users/GotFlamingo/events{/privacy}",
#  "received_events_url": "https://api.github.com/users/GotFlamingo/received_events",
#  "type": "User",
#  "site_admin": false,
#  "name": "GoT Flamingo",
#  "company": null,
#  "blog": "",
#  "location": "Denmark",
#  "email": null,
#  "hireable": null,
#  "bio": null,
#  "twitter_username": null,
#  "public_repos": 5,
#  "public_gists": 0,
#  "followers": 2,
#  "following": 1,
#  "created_at": "2023-03-04T13:49:38Z",
#  "updated_at": "2024-01-02T09:35:47Z"
# }

def lookup(username):
    system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Github Searcher | Github.com/gotflamingo | Made By GoT Flamingo")
    print(" ")
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        return {
            "Username": username,
            "ID": data.get('id', "Not available"),
            "name": data.get('name', "Not available"),
            "Avatar": data.get('avatar_url', "Not available"),
            "Link": data.get('html_url', "Not available"),
            "location": data.get('location', "Not available"),  
            "Followers": data.get('followers', "Not available"),
            "Followings": data.get('following', "Not available"),
            "Type": data.get('type', "Not available"),
            "Admin": data.get('site_admin', "Not available"),
            "email": data.get('email', "Not available"),
            "Konto Lavet den": data.get('created_at', "Not available"),
            "Konto sidst updates": data.get('updated_at', "Not available"),
            "Followers Link": data.get('followers_url', "Not available"),
            "Repos Link": data.get('repos_url', "Not available"),
            "API": data.get('url', "Not available"),  
        }
    else:
        return {'Error': 'Failed to retrieve data'}

system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("Github Searcher | Github.com/gotflamingo | Made By GoT Flamingo")
print(logo)
name = input(f"{Fore.LIGHTGREEN_EX}Name:{Fore.LIGHTWHITE_EX} ")
result = lookup(name)

if 'Error' in result:
    print(logo)
    ctypes.windll.kernel32.SetConsoleTitleW("Github Searcher | Github.com/gotflamingo | Made By GoT Flamingo")
    print(f"{Fore.LIGHTCYAN_EX}Kunne ikke finde {Fore.LIGHTGREEN_EX}brugeren{Fore.LIGHTCYAN_EX} med navnet: {Fore.LIGHTWHITE_EX}{name}")
else:
    system('cls')
    print(logo2)
    ctypes.windll.kernel32.SetConsoleTitleW("Github Searcher | Github.com/gotflamingo | Made By GoT Flamingo")
    print(" ")
    print(f"{Fore.LIGHTRED_EX}Username:{Fore.LIGHTWHITE_EX}", result["Username"])
    print(f"{Fore.LIGHTRED_EX}ID:{Fore.LIGHTWHITE_EX}", result["ID"])
    print(f"{Fore.LIGHTRED_EX}Name:{Fore.LIGHTWHITE_EX}", result["name"])
    print(f"{Fore.LIGHTRED_EX}Avatar:{Fore.LIGHTWHITE_EX}", result.get('Avatar', "Not available"))
    print(f"{Fore.LIGHTRED_EX}Link:{Fore.LIGHTWHITE_EX}", result.get('Link', "Not available"))
    print(f"{Fore.LIGHTRED_EX}location:{Fore.LIGHTWHITE_EX}", result.get('location', "Not available"))
    print(f"{Fore.LIGHTRED_EX}Followers:{Fore.LIGHTWHITE_EX}", result.get('Followers', "Not available"))
    print(f"{Fore.LIGHTRED_EX}Followings:{Fore.LIGHTWHITE_EX}", result.get('Followings', "Not available"))
    print(f"{Fore.LIGHTRED_EX}Type:{Fore.LIGHTWHITE_EX}", result.get('Type', "Not available"))
    admin = result.get('site_admin')
    if admin is not None:
        print(f"{Fore.LIGHTRED_EX}Admin:{Fore.LIGHTWHITE_EX}", admin)
    else:
        print(f"{Fore.LIGHTRED_EX}Admin:{Fore.LIGHTWHITE_EX} No")
    email = result.get('email')
    if email is not None:
        print(f"{Fore.LIGHTRED_EX}Email:{Fore.LIGHTWHITE_EX}", email)
    else:
        print(f"{Fore.LIGHTRED_EX}Email:{Fore.LIGHTWHITE_EX} not found")
    print(f"{Fore.LIGHTRED_EX}Followers Link:{Fore.LIGHTWHITE_EX}", result.get('Followers Link', "Not available"))
    print(f"{Fore.LIGHTRED_EX}Repos Link:{Fore.LIGHTWHITE_EX}", result.get('Repos Link', "Not available"))
    print(f"{Fore.LIGHTRED_EX}Konto Lavet den:{Fore.LIGHTWHITE_EX}", result.get('created_at', "Not available"))
    print(f"{Fore.LIGHTRED_EX}Konto sidst updates:{Fore.LIGHTWHITE_EX}", result.get('updated_at', "Not available"))
    time.sleep(10)