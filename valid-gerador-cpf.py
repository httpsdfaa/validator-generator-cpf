import re, sys, random # RE faz uso para ter utilização de somente números

def menu():
    input_menu = input('-1 VALIDAR CPF \n-2 GERAR CPF \n-S SAIR\n\n--> ')

    while True:
        if input_menu == '1':
            return '1'
        elif input_menu == '2':
            return '2'
        elif input_menu == 's' or input_menu == 'S':
            print('Saindo do programa, até logo!')
            sys.exit()
        else:
            print('\nENTRADA INVÁLIDA\n')
            break
            
            


def cpf_validation():
    cpf_user_validation = input('Digite seu CPF para validação: ')
    cpf_user_validation = re.sub(r'[^0-9]', '', cpf_user_validation)

    cpf_complete_calculation = cpf_calculation(cpf_user_validation, None) # calculando os dígito do CPF

    digit_repetitive = (cpf_user_validation[0] * len(cpf_user_validation)) == cpf_user_validation # tratando digitos repetivos

    if len(cpf_user_validation) < 11:
        main()
    elif digit_repetitive:
        main()
    elif cpf_user_validation == cpf_complete_calculation:
        return cpf_complete_calculation
    else:
        main()


def cpf_generator():
    cpf_generator_nine_digit = ''
    for _ in range(9):
        cpf_generator_nine_digit += str(random.randint(0, 9))
    
    cpf_complete_calculation = cpf_calculation(None, cpf_generator_nine_digit)
    return cpf_complete_calculation


def cpf_calculation(cpf_user_param, cpf_developer_generator):
    REGRESSION_TEN = 10
    REGRESSION_ELEVEN = 11
    
    cpf_user = cpf_user_param or cpf_developer_generator # cpf do usuário ou cpf gerado automaticamente atráves do random na funcao cpf_generator
    cpf_user = re.sub(r'[^0-9]', '', cpf_user)
    cpf_user_nine_digit = cpf_user[:9]

    def calculation_digit(cpf_user_nine_digit, regression):
        soma = 0

        for digit in cpf_user_nine_digit:
            digit = int(digit)

            #calculo do décimo e décimo primeiro dígito
            calculation_digit = digit * regression
            soma += calculation_digit

            regression -= 1
    
        result_digit = (soma * 10) % 11

        inferior_ten = result_digit <= 9 

        if inferior_ten:
            return result_digit
        else: 
            return '0'
    

    result_digit_ten = cpf_user_nine_digit + str(calculation_digit(cpf_user_nine_digit, REGRESSION_TEN)) # descobrindo o décimo dígito
    cpf_complete = result_digit_ten + str(calculation_digit(result_digit_ten, REGRESSION_ELEVEN)) # descobrindo o décimo primeiro dígito
    
    if cpf_complete == cpf_user or cpf_developer_generator: # cpf do usuário ou cpf gerado automaticamente pelo random na funcao cpf_generator
        return cpf_complete
    else:
        return print('\nCPF INVÁLIDO\n')


def main():

    cpf_validation_var = '1'
    cpf_generator_var = '2'

    user_choice = menu() # armazena o valor de menu

    if user_choice == cpf_validation_var:
        cpf_validation_func = cpf_validation()
        if cpf_validation_func != None:
            print(f'CPF {cpf_validation_func} VÁLIDO')
    elif user_choice == cpf_generator_var:
        if cpf_generator() != None:
            print(f'CPF gerado: {cpf_generator()}')
    else:
        print('Algo de errado aconteceu')

main()