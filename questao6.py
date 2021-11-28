nome = input('informe o nome do aluno: ')
aluno=nome
nota_materia1=input('informe a primeira nota:')
nota1 = int(nota_materia1)
nota_materia2=input('informe a segunda nota:')
nota2 = int(nota_materia2)
nota_materia3=input('informe a terceira nota:')
nota3 = int(nota_materia3)
media=((nota1+nota2+nota3)/3)
if media>=7:
    print('Aluno:',aluno,' foi aprovado com media: %.2f'%media)
elif (media < 7) and(media>4):
    print('Aluno:',aluno,' esta na final')
else:
    print('Aluno:',aluno,' reprovado')
