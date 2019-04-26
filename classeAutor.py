from datetime import datetime
import psycopg2

class Autor:
    def __init__(self,nome,email):

        self._nome = nome
        self._email = email
        self._trabalhos = []

    
    def _get_nome(self):
        return self._nome
    
    def _get_email(self):
        return self._email
    
    def _get_trabalhos(self):
        return self._trabalhos

    def _get_cod(self):
        return int(self._cod)
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_email(self, email):
        self._email = email
    
    def _set_cod(self, cod):
        self._cod = int(cod)
    
    def _set_trabalhos(self, t):
        try:
            self._trabalhos.append(t)
        except:
            self._trabalhos = []
            self._trabalhos.append(t)
        

    nome = property(_get_nome,_set_nome)
    email = property(_get_email,_set_email)
    cod = property(_get_cod,_set_cod)
    trabalhos = property(_get_trabalhos,_set_trabalhos)




class Trabalho:
    def __init__(self,conteudo,nota,dataEntrega,titulo):
        self._conteudo = conteudo
        self._nota = nota
        self._dataEntrega = dataEntrega
        self._titulo = titulo
    
    def _get_cod(self):
        return self._cod
    
    def _get_conteudo(self):
        return self._conteudo
    
    def _get_nota(self):
        return self._nota
    
    def _get_dataEntrega(self):
        return self._dataEntrega
    
    def _get_dtHoraAtualizacao(self):
        return self._dtHoraAtualizacao


    
    def _set_cod(self,cod):
         self._cod = cod
    
    def _set_conteudo(self,conteudo):
        self._conteudo = conteudo
    
    def _set_nota(self,nota):
        self._nota = nota
    
    def _set_dataEntrega(self,data):
        self._dataEntrega = data
    
    def _set_dtHoraAtualizacao(self,data):
        self._dtHoraAtualizacao = data
    

    cod = property(_get_cod,_set_cod)
    conteudo = property(_get_conteudo,_set_conteudo)
    nota = property(_get_nota,_set_nota)
    dataEntrega = property(_get_dataEntrega,_set_dataEntrega)
    dtHoraAtualizacao = property(_get_dtHoraAtualizacao,_set_dtHoraAtualizacao)



t1 = Trabalho("fazer pao",10,"25/04/2019","cacetinho")
t2 = Trabalho("refutar professor de historia",0,"25/04/2019","vc ta rindo?")
t3 = Trabalho("assar pao",10,"25/04/2019","cacetinho")
a1 = Autor("nando moura", "nando_cnoura@gmail.com")
#a1.trabalhos=t3

#t1.cod=1
a1._set_trabalhos(t1)
#a1._set_trabalhos(t2)
#a1._set_trabalhos(t3)


#print((a1.trabalhos[0]).conteudo)
#print((a1.trabalhos[1]).conteudo)
#print((a1.trabalhos[2]).conteudo)





class Dao:

    def __init__(self):
        self._conexao = "dbname=trabalhoAutor user=postgres password=postgres host=localhost port=5432"




class AutorDao(Dao):

    def __init__(self):
        #super().__init__(self)
        self._conexao = "dbname=trabalhoAutor user=postgres password=postgres host=localhost port=5432"


    def salvar(self, autor):

        verifica=hasattr(autor, 'cod')

        if (verifica):
            print("to verificando heinkkkk")
            con = psycopg2.connect(self._conexao)
            cursor = con.cursor()
            cursor.execute('UPDATE "Autor" SET nome = %s, email = %s WHERE cod = %s',(autor.nome,autor.email,int(autor.cod)))
            con.commit()
            cursor.close()


        else:
            print("coékkk")
            con = psycopg2.connect(self._conexao)
            cursor = con.cursor()
            cursor.execute('insert into "Autor" (nome,email) values (%s,%s) RETURNING cod', (autor.nome, autor.email))
            codigo = (cursor.fetchone())[0]
            con.commit()
            autor.cod = int(codigo)
            cursor.close()
        
    
    def buscar(self,cod):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM "Autor" WHERE cod = %s',[cod])
        b = cursor.fetchone()
        cursor.close()
        return b


    def excluir(self,cod):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('DELETE FROM "Autor" WHERE cod = %s',[cod])
        con.commit()
        cursor.close()
    

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from "Autor"')
            for linha in cursor.fetchall():
                v.append(linha)
        
        cursor.close()
        return v
        










            
    


#a2 = Autor("to com raiva","GRRRR@gmail")
#adao = AutorDao()
#adao.salvar(a2)
#print(a2.cod)
#print("autor antes: ",a2.nome)


#a3 = Autor("borboleta","borboleta@gmail")
#a3.cod=756
#print("autor antes: ",a3.nome)

#a2.nome="eh os guri"
#a2.email="kkk@gmail"
#print("autor DEPOIS : ",a3.nome)

adao = AutorDao()
#print(adao.buscar(756))
#adao.excluir(737)
print(adao.listar())


"""

f= F ("press F to jailson mendes",  )
f= F ("press F to jailson mendes",69)

f1 = F("press F to hater of raffa moreira",777)

fdao = salvar(f)
if f nao tem codigo, entao é pq ele nunca foi inserido

if f tem codigo, entao é pq ele ja foi inserido, talvez o usuario queira 
modificar ele. aaaah para ne 
"""





#select dao antes de inserir 
#salvar, conferir se o codigo de um deles foi passado




    

"""
    def salvar(self,autor):

        i=0
        l = len(autor.trabalhos)-1
        while(i<=l):
            verifica=hasattr(autor.trabalhos[i], 'cod')

            if (verifica):
                print("caraio deu tudo errado vai arrumar isso dai")
            else:
                print("coékkk")
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('insert into "Autor" (nome,email) values (%s,%s)',[autor.nome,autor.email])
        

        cursor.close()
        i=i+1
"""
    



