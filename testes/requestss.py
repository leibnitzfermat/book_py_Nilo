import requests

cep = input('Digite o CEP: ')

r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

print(r.json()) #{'cep': '68181-390', 'logradouro': 'Travessa Segunda', 'complemento': '', 'bairro': 'Floresta', 'localidade': 'Itaituba', 'uf': 'PA', 'unidade': '', 'ibge': '1503606', 'gia': ''}

print(r['bairro'].text)

print(r.text)
'''
{
  "cep": "68181-390",
  "logradouro": "Travessa Segunda",
  "complemento": "",
  "bairro": "Floresta",
  "localidade": "Itaituba",
  "uf": "PA",
  "unidade": "",
  "ibge": "1503606",
  "gia": ""
}
'''