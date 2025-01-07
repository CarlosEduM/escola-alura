from validate_docbr import CPF
import re

def cpf_invalido(cpf):
    return not CPF().validate(cpf)

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    resposta = re.findall('[0-9]{2} [0-9]{5}-[0-9]{4}', celular)
    return not resposta