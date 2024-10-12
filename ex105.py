def notas(*notas, sit=False):
    resposta={}
    resposta['total']=len(notas)
    resposta['maior']=max(notas)
    resposta['menor']=min(notas)
    resposta['média']=sum(notas)/len(notas)

    if sit==True:
        if resposta['média']<=5:
            situação='RUIM'
        elif resposta['média']<=6.9:
            situação='REGULAR'
        else:
            situação='BOA'
        resposta['situação']=situação
    return resposta

notasalunos=(1,5.4,6.2,6)
resposta=notas(*notasalunos,sit=True)
print(resposta)



        




# def notas(*notas,sit=False):
#     resposta={}
#     maior=notas[0]
#     menor=notas[0]
#     soma=0
    
#     for x in notas:
#         if x>maior:
#             maior=x
#         elif x<menor:
#             menor=x
#         soma+=x
    
#     med=soma/len(notas)
    
#     resposta['total']=len(notas)
#     resposta['maior']=maior
#     resposta['menor']=menor
#     resposta['média']=med


#     if sit==True:
#         if med<=5:
#             situação='RUIM'
#         elif med<=6.9:
#             situação='REGULAR'
#         else:
#             situação='BOA'
#         resposta['situação']=situação     
#     return  resposta

