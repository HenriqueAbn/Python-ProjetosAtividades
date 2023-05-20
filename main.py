print("Bem-Vindo ao qAcademicoLite")

nomeAluno = input(str("Qual é o seu nome completo? "))
matriculaAluno = input(int("Qual a sua Matrícula? "))

nota1 = float(input("Qual a n1 do Aluno? "))
nota2 = float(input("Qual a n2 do Aluno? "))

calcNotaFinal = float(((nota1 * 2) + (nota2 * 3)) / 5)

if(calcNotaFinal > 6.00):
    print(nomeAluno)
    print(matriculaAluno)
    print(calcNotaFinal)
    print("Você Passou!")
elif(calcNotaFinal < 6.00):
    print(nomeAluno)
    print(matriculaAluno)
    print(calcNotaFinal)
    print("Você não passou.")
else:
    print("Dados Inválidos")
