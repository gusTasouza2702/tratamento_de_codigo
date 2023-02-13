try:
    a = 1
    b = int(input('denominador: '))
    r = a / b

except ZeroDivisionError:
    print('Não é possível dividir por zero')

except (ValueError, TypeError):
    ('tivemos um problema com o tipo de dados que você digitou')

else:
    print(f'o resultado é {r:.1f}')

finally:
    print('o programa acabou! agradeço por ter usado!\n meu nome é: Gustavo! e obg!')
    
