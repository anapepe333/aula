#faça um codigo que receba o nome e as notas de um aluno (4 bimestres)
#depois de ter as 4 notas, faça a média aritmética das notas e diga se o aluno está reprovado ou passou de ano
print("Olá, sou um troço que calcula se voce passou de ano")

escolha =int(input('Escolha uma matéria: 1=matematica, 2= portugues, 3=ciencias, 4=ingles\n'))
if escolha == 1:
    materia = 'matematica'

elif escolha == 2:
    materia = 'portugues'

elif escolha == 3:
    materia = 'ciencias'

elif escolha == 4: 
    materia = 'ingles'
    
print(f"materia escolhida foi: {materia}")



bim1 = float(input("Sua nota do primeiro bimestre: \n"))
bim2 = float(input("Sua nota do segundo bimestre: \n"))
bim3 = float(input("Sua nota do terceiro bimestre: \n"))
bim4 = float(input("Sua nota do quarto bimestre: \n"))

notafinal = (bim1+bim2+bim3+bim4)/4

print(f"sua nota final em {materia} foi: {notafinal}")
if notafinal < 6 :print("voce foi reprovado :D \n")
if notafinal >= 6 :print("voce foi aprovado >:D \n")
 #eba