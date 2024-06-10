# SubdT
subdt: subdomain-tracker - Python scrypt to search and find subdomains

O script visa realizar uma busca de subdomínios em um site especificado pelo usuário. Ele utiliza uma técnica de brute force para verificar a existência de diretórios comuns, como "www", "wiki", "mail", entre outros. 

(!> futuramente a ideia de add uma wordlist será implementada).

Para utilizar o script, basta executá-lo como qualquer script python3 e inserir a URL do site que deseja verificar. 
O script então realizará a busca nos diretórios e informará se cada diretório existe ou não no site dependendo do status code.

```bash
python3 subdt.py
```
