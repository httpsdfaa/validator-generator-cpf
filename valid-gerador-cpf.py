import re, sys, random# fazer uso para ter utilização de somente números


def calculo_digito(conta_regressiva, cpf_nove_dez):
    conta_regressiva = conta_regressiva
    soma = 0

    for digito in cpf_nove_dez:
        digito = int(digito)
        
        calculo_multiplicacao = digito * conta_regressiva # calculo da multiplicacao
        soma += calculo_multiplicacao # calculo da soma

        conta_regressiva -= 1 # fazendo a regressiva
    
    resultado_digito = (soma * 10) % 11 # calculo final

    superior_9 = resultado_digito >= 10 # maior que 9
    inferior_10 = resultado_digito <= 9 # menor ou igual que 9

    resultado_digito if superior_9 else inferior_10
    return str(resultado_digito)

def cpf_completo(cpf_nove_digitos):
    # concatenando os nove com os decimo e o decimo primeiro digito
    cpf_dez_digito = cpf_nove_digitos + calculo_digito(10, cpf_nove_digitos) # concatenando os 9 digitos com o decimo
    cpf_completo = cpf_dez_digito + calculo_digito(11, cpf_dez_digito) # concatenando os 10 digitos com o decimo primeiro
    
    return cpf_completo

def main():
    entrada_um = input(f'({1}) VALIDAR CPF \n\
({2}) GERAR CPF \n\n-->')
    
    cpf_nove_digitos = ''
    if(entrada_um == '1'):
        cpf_usuario = input('Digite seu CPF para validação: ')
        cpf_usuario = re.sub(r'[^0-9]', '', cpf_usuario) # aceita somente números

        cpf_nove_digitos = str(cpf_usuario[:9])

        cpf_completo(cpf_nove_digitos)

        """ 
            CONFERIR NÚMEROS REPETIVOS E VALIDANDO ENTRADA    
        """
        char_usuario_repet = cpf_usuario[0] * len(cpf_usuario) # checando se os digitos são repetitivos
        if(char_usuario_repet == cpf_usuario):
            print("CPF INVÁLIDO")
            sys.exit()
        elif(cpf_usuario == cpf_completo(cpf_nove_digitos)):
            print(f'CPF {cpf_usuario} VÁLIDO')
        else:
            print('O CPF é inválido')
    elif(entrada_um == '2'):
        for _ in range(9):
            cpf_nove_digitos += str(random.randint(0, 9))
        cpf_gerado = cpf_completo(cpf_nove_digitos)

        print(f'CPF GERADO: {cpf_gerado}')
    else:
        print('Opção inválida')

main()