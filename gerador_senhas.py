import random
import string

def gerar_senha(tamanho=12):
    letras_maiusculas = string.ascii_uppercase  
    letras_minusculas = string.ascii_lowercase  
    numeros = string.digits  
    simbolos = string.punctuation  

    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (mínimo 8): "))
            if tamanho < 8:
                print("O tamanho deve ser pelo menos 8 caracteres. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número.")

    senha = gerar_senha(tamanho)
    print(f"Sua senha gerada é: {senha}")

    continuar = input("Deseja gerar outra senha? (s/n): ").lower()
    if continuar == 's':
        main()  
    else:
        print("Obrigado por usar o Gerador de Senhas!")

if __name__ == "__main__":
    main()