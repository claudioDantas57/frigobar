import sqlalchemy as db
import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.sql import functions


engine = db.create_engine("mysql+pymysql://root:admin@localhost:3306/frigobar")
Base = declarative_base()

class Frigobar(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    quantidade = Column(Numeric)
    preco = Column(Numeric (6,2))


Base.metadata.create_all(engine)

i1 = Frigobar(nome = "água", quantidade = 2, preco = 4.00)
i2 = Frigobar(nome = "refrigerante", quantidade  = 2, preco = 5.00)
i3 = Frigobar(nome = "cerveja", quantidade  = 2, preco =  10.00)
i4 = Frigobar(nome = "amendoim", quantidade  = 2, preco = 4.50)

Session = sessionmaker(bind=engine)
session = Session()

#session.add_all([i1, i2, i3, i4])
#session.commit()

print("MENU DE OPÇÕES:\n"
      "- Digite 1 para consultar\n"
      "- Digite 2 para alterar\n"
      "- Digite 3 para deletar\n"
      "- Digite 4 para inserir\n")

opcao = int(input("Informe a opção desejada: "))


def consumo():
    item = session.query(Frigobar).all()
    for itens in item:
        print(itens.id,itens.nome)
    itens_cons_nome = []
    itens_cons_preco = []
    conta ={}
    op = 0
    while True:
        if op == 0:
            consumo = int(input("Informe o id do produto consumido: "))
            impressao_consumo = session.query(Frigobar).filter(Frigobar.id == consumo).first()
            itens_cons_nome.append(impressao_consumo.nome)
            itens_cons_preco.append(impressao_consumo.preco)

            resposta = input("Deseja continuar? [N] não, [S] sim").upper()
            if resposta == "Y":
                op = 0
            elif resposta == "N":
                op = 1

        elif op == 1:

            conta = {[itens_cons_nome],[itens_cons_preco]}

            print(conta)
            break


'''soma = session.query(
                functions.sum(Frigobar.id)).scalar()
            print(soma)'''



def alterar():
    consumo()
    id_item = int(input("Digite o item reposto: "))
    itens = session.query(Frigobar).filter(Frigobar.id == id_item).one()
    Quantidade = int(input("Informe a quantidade de itens repostos: "))
    itens.quantidade = Quantidade
    session.add(itens)
    session.commit()

'''def deletar():
    produtos = session.query(Produtos).filter(Produtos.id == 4).one()
    session.delete(produtos)
    session.commit()

def inserir():
    N_produto =input('digite o nome')
    preco = int(input('digite o preço'))
    new_produto = Produtos(nome=N_produto, preco=preco)
    session.add(new_produto)
    session.commit()'''


if opcao == 1:
    print("Você quer ver o item consumido.")
    consumo()

elif opcao == 2:
    print("Você quer alterar.")
    alterar()
elif opcao == 3:
    print("Você quer deletar.")
    deletar()
elif opcao == 4:
    print("Você quer inserir.")
    inserir()
