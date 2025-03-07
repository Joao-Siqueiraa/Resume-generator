from fpdf import FPDF

pdf= FPDF()

pdf.add_page()
pdf.set_font("arial")


nome=input("qual seu nome? ")
pdf.text(75, 15, nome)
endbr=input("qual seu endereço e bairro? ")
pdf.text(55, 20,"endereço: {} ".format(endbr))
cdcep=input("qual sua cidade e seu cep?  ")
pdf.text(75, 25, cdcep)
tel=input("qual seu numero de celular? ")
pdf.text(75, 30, "tel:{}".format(tel))
emai=input("qual seu email? ")
pdf.text(62, 35, "email:{}".format(emai))
pdf.text(20, 50, "DADOS PESSOAIS")
nac=input("qual sua nacionalidade ")
pdf.text(20, 55,"nacionalidade:{}".format(nac))
esc=input("qual seu estado civil? ")
pdf.text(20, 60,"estado civil:{}".format(esc))
ddn=input("qual sua data de nascimento? ")
pdf.text(20, 65,"data de nascimento {}".format(ddn))
pdf.text(20, 75,"FORMAÇAO ACADEMICA")
fa=input("sua formaçao academica?")
pdf.text(20, 85,fa)
psvt=(int(90))
psvt1=(int(100))
psvt2=(int(110))
psvt3=(int(120))
psvt4=(int(130))


while True:
    if1 = input("Tem algo a acrescentar na formação acadêmica? [S/N] ").upper()
    
    
    if if1 == "S":
        
        fa_add = input("Informe a informação adicional sobre sua formação acadêmica: ")
        pdf.text(20, psvt, fa_add)
        psvt += 5
        psvt1 += 5
        psvt2 += 5
        psvt3 += 5
        psvt4 += 5
        
    else:
        break
pdf.text(20, psvt1-5,"CURSOS COMPLEMENTARES")
cc=input("seus cursos? ")
pdf.text(20, psvt2-5,cc)
while True:
    cc1 = input("Tem algo a acrescentar na formação acadêmica? [S/N] ").upper()
    
    
    if cc1 == "S":
        psvt2 += 5
        psvt3 += 5
        psvt4 += 5
       
        cc_add = input("Informe a informação adicional sobre seus cursos: ")
        pdf.text(20, psvt2, cc_add)
        
        psvt2 += 5
        psvt3 += 5
        psvt4 += 5
        
    else:
        break
pdf.text(20, psvt3-5, "experiencia profissional")
ep=input("empresa em que trabalhou? ")
cg=input("cargo na empresa? ")
pdf.text(20, psvt4-5, 'empresa - {} cargo - {}'.format(ep,cg))
while True:
    ep1 = input("Tem algo a acrescentar na formação acadêmica? [S/N] ").upper()
    
    
    if ep1 == "S":
        psvt4 += 5
        ep_add = input("Informe a informação adicional sobre sua empresa: ")
        cg_add = input("Informe a informação adicional sobre seu cargo: ")
        pdf.text(20, psvt4, 'empresa - {} cargo - {}'.format(ep_add,cg_add))
        psvt4 += 5
        
    else:
        break
pdf.output("curriculo.pdf")
#pdf.output("curriculo{}.pdf".format(nome))
print("curriculo atualizado com sucesso")





