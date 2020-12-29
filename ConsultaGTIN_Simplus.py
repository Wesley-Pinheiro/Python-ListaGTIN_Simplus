
import requests
import json

iEAN = "7896090704460" #INFORME AQUI O EAN DO PRODUTO
iTOKEN = "AQUI SEU TOKEN" #AQUI O TOKEN INFORMADO PELA SIMPLUS

url = "https://prod.simplustec.com.br/api/v3/itemResend"

payload= ("{\r\n  \"gtin\": 0,\r\n  \"productCode\": \"EAN" + 
str(iEAN) + 
"\"\r\n}")

headers = {
  'Accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + str(iTOKEN) + ''
        }

response = requests.request("POST", url, headers=headers, data=payload)

#AQUI MOSTRA OS RESULTADOS DA CONSULTA
print(response.text)

