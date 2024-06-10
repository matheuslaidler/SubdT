#subdt v0.0.1 -> subdomain tracker -> a subdomain finder
import time
import requests

def subdomain_search():
    '''
    This function performs a brute force search on a specified website to check
    for the existence of certain sub-domains

    Função que faz uma varredura, por força bruta, da existência de subdomínios 
    de um site especificado
    '''
    print("  ./subdt by matheuslaidler \n Type the website without protocol like 'https://'  \n  ( e.g. matheuslaidler.github.io )\n")
    site = input(" Enter a valid URL> ")

    subs = ["admin", "www", "m", "mail", "blog", "shop", "forums", "forum", "wiki", "community", "ww1"]

    for subdomain in subs:
        url = "http://" + subdomain + "." + site
        # Send a GET request to the URL || Realiza a requisição GET ao site
        response = requests.get(url)
        # Check the status code of the response || Verifica o código de status da resposta
        status = response.status_code
        if status < 200:
            print(f" * {subdomain} received the request => [status code {status} - informational response] - {url}")
        elif 199 < status < 300:
            print(f" * {subdomain} exists => [status code {status} - successful!!]")
            print(f"  {url}")
        elif 299 < status < 400:
            print(f" * {subdomain} is redirecting => [status code {status} - redirection] - {url}")
        elif 399 < status < 500:
            print(f" * {subdomain} was not found => [status code {status} - client error]")
        else:
            print(f" * {subdomain} was inaccessible => [status code {status} - server error] - {url}")

    # Delay / Wait for X second(s) before continuing || Aguarda X segundo(s) antes de continuar
    time.sleep(1)
    print("                         ")
    return leave()

def leave():
    '''
    Function to ask user whether to exit the program or continue.

    Função para solicitar ao usuário se deseja sair do programa ou continuar.
    '''
    response = input(" Do you want to exit? (yes/no): ")
    if response.lower() == "yes":
        print("Program terminated.")
        exit()
    else:
        subdomain_search()

# Call the main function
# Chamada da função principal
subdomain_search()

"""

fzr a chamada da função principal correta dps
colocar opção para uso de wordlist no script no lugar da array
colocar o "#type: ignore" qnd precisar - 'erro' vstudio
"""
