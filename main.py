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

    
 print("Crie sua própria Máfia!")

print("Modelos de Máfia:")
print("1 - Máfia Italiana")
print("2 - Cartel Mexicano")
modeloEscolhido = int(input("Qual modelo você deseja? (Escolha pelo número correspondente) "))

if (modeloEscolhido == 1):
    nomeFamiliaMafia = input(str("Qual é o nome da sua família? "))
    don = str(input("Quem será o Don? "))
    valorProtecao = float(input("Qual o valor que a Mafia vai cobrar por Proteção?"))
    print(f"Sua família é {nomeFamiliaMafia} e seu Don é {don}")
    print(f"Você vai cobrar ${valorProtecao} por 'proteção' ")
elif (modeloEscolhido == 2):
    nomeFamiliaCartel = input(str("Qual é o nome da sua família? "))
    chefe = str(input("Quem será o chefe? "))
    alucinate = str(input("Qual o alucinante que você vai produzir"))
    valorAlucinante = float(input("Qual o valor cobrado pelo alucinate? "))
    print(f"Sua família é {nomeFamiliaCartel} e seu Don é {chefe}")
    print(f"O alucinate produzido será {alucinate} e custará {valorAlucinante}")
else:
    print("Dados Inválidos")
