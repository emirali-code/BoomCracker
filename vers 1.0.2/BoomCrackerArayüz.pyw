import tkinter as tk
import os

root=tk.Tk()
root.title("BoomCracker")
root.configure(background="Black")
root.geometry("600x845+10+10")

tank=tk.PhotoImage(file = "indir.gif")
pack=tk.Label(root,image=tank)
pack.pack()

giriş=tk.Label(text="BoomCracker",bg="black",fg="green",font="Roman")
giriş.pack()

giriş1=tk.Label(text="""Turkish Hack Tools
--Coded By Emyounoone--""",bg="black",fg="red",font="Roman")
giriş1.pack()

ad=tk.Label(text=("World List İsmi (Oluşturmak İstediğiniz Dosya Uzantısıyla ÖR :'deneme.txt'): "),bg="black",fg="blue",font="Verdana 11")
ad.pack()
           
isim=tk.Entry(bg="white",fg="black",font="Verdana 10")
isim.pack()

def fonk1():
    giriş=isim.get()
    file=open(giriş,"w")
    #ad
    soru1=s1.get()
    
    #soy ad
    soru2=s2.get()
    
    #Doğum Tarihinin Son İki Hanesi
    soru11=s11.get()
    
    #Doğum Yıl
    soru3=s3.get()
    
    #Yakın İsmi
    soru4=s4.get()
    
    #Özel Sayı
    soru6=s6.get()
    
    #Memleket Plaka Kodu
    soru7=s7.get()
    
    #Doğum Tarihi 
    soru8=s8.get()
    
    #Eklemek İstediğiniz Kelime grubu
    soru9=s9.get()
    
    #Sonuna Eklemek İstediğiniz Özel Karakter
    soru10=s10.get()
    
    #algoritmalar
    file.write("""!'#''#'
!'#''#'
$'#''#'
$'#''#'
%'#''#'
%'#''#'
&'#''#'
&'#''#'
'#'!'#'
'#'!'#'
'#'$'#'
'#'$'#'
'#'%'#'
'#'%'#'
'#'&'#'
'#'&'#'
'#''#'
'#''#'
'#''#'!
'#''#'!
'#''#'$
'#''#'$
'#''#'%
'#''#'%
'#''#'&
'#''#'&
'#''#''#'
'#''#''#'
'#''#'*
'#''#'*
'#''#'@
'#''#'@
'#'*'#'
'#'*'#'
'#'@'#'
'#'@'#'
*'#''#'
*'#''#\n""")
    file.write(soru1+soru8+soru9+soru10+"\n")
    file.write(soru1+soru8+soru9+"\n")
    file.write(soru1+soru8+soru10+"\n")
    file.write(soru1+soru8+"\n")
    file.write(soru8+"\n")
    file.write(soru3+soru11+"\n")
    file.write(soru11+soru3+"\n")
    file.write(soru11+soru11+"\n")
    file.write(soru3+soru3+soru3+"\n")
    file.write(soru11+soru3+soru10+"\n")
    file.write(soru11+soru3+soru9+soru10+"\n")
    file.write(soru3+soru11+soru9+soru10+"\n")
    file.write(soru3+soru11+soru10+"\n")
    file.write(soru1+soru2+"\n")
    file.write(soru1+soru2+soru10+"\n")
    file.write(soru1+soru2+soru9+"\n")
    file.write(soru1+soru2+soru9+soru10+"\n")
    file.write(soru1+"_"+soru3+"\n")
    file.write(soru1+"_"+soru3+soru10+"\n")
    file.write(soru1+"_"+soru3+soru9+"\n")
    file.write(soru1+"_"+soru3+soru9+soru10+"\n")
    file.write(soru1+"_"+soru2+"\n")
    file.write(soru1+"_"+soru2+soru10+"\n")
    file.write(soru1+"_"+soru2+soru9+"\n")
    file.write(soru1+"_"+soru2+soru9+soru10+"\n")
    file.write(soru1+"11\n")
    file.write(soru1+"22\n")
    file.write(soru1+"33\n")
    file.write(soru1+"44\n")
    file.write(soru1+"55\n")
    file.write(soru1+"66\n")
    file.write(soru1+"77\n")
    file.write(soru1+"88\n")
    file.write(soru1+"99\n")
    file.write(soru1+"00\n")
    file.write(soru1+"11"+soru10+"\n")
    file.write(soru1+"22"+soru10+"\n")
    file.write(soru1+"33"+soru10+"\n")
    file.write(soru1+"44"+soru10+"\n")
    file.write(soru1+"55"+soru10+"\n")
    file.write(soru1+"66"+soru10+"\n")
    file.write(soru1+"77"+soru10+"\n")
    file.write(soru1+"88"+soru10+"\n")
    file.write(soru1+"99"+soru10+"\n")
    file.write(soru1+"00"+soru10+"\n")
    file.write(soru1+"1\n")
    file.write(soru1+"2\n")
    file.write(soru1+"3\n")
    file.write(soru1+"4\n")
    file.write(soru1+"5\n")
    file.write(soru1+"6\n")
    file.write(soru1+"7\n")
    file.write(soru1+"8\n")
    file.write(soru1+"9\n")
    file.write(soru1+"0\n")
    file.write ("123456789"+soru1+"123456789\n")
    file.write ("12345678"+soru1+"12345678\n")
    file.write ("1234567"+soru1+"1234567\n")
    file.write ("123456"+soru1+"123456\n")
    file.write ("12345"+soru1+"12345\n")
    file.write ("1234"+soru1+"1234\n")
    file.write ("123456789"+soru1+"123456789\n")
    file.write ("123"+soru1+"123456789\n")
    file.write ("123"+soru1+"12345678\n")
    file.write ("123"+soru1+"1234567\n")
    file.write ("123"+soru1+"123456\n")
    file.write ("123"+soru1+"12345\n")
    file.write ("123"+soru1+"1234\n")
    file.write ("123456789"+soru1+"123\n")
    file.write ("12345678"+soru1+"123\n")
    file.write ("1234567"+soru1+"123\n")
    file.write ("123456"+soru1+"123\n")
    file.write ("12345"+soru1+"123\n")
    file.write("1234"+soru1+"123\n")
    file.write("123"+soru1+"123\n")
    file.write(soru1+soru11+"\n")
    file.write(soru1+soru2+"1\n")
    file.write(soru1+soru2+"12\n")
    file.write(soru1+soru2+"123\n")
    file.write(soru1+soru2+"1234\n")
    file.write(soru1+soru2+"12345\n")
    file.write(soru1+soru2+"123456\n")
    file.write(soru1+soru2+"1234567\n")
    file.write(soru1+soru2+"12345678\n")
    file.write(soru1+soru2+"123456789\n")
    file.write(soru1+soru2+"1234567890\n")
    file.write(soru2+soru10+"\n")
    file.write(soru1+soru7+"\n")
    file.write(soru2+soru9+"\n")
    file.write(soru6+soru8+"\n")
    file.write(soru4+soru9+"\n")
    file.write(soru4+soru10+"\n")
    file.write(soru1+soru1+"\n")
    file.write(soru2+soru2+"\n")
    file.write(soru11+soru1+soru11+"\n")
    file.write(soru11+soru1+"\n")
    file.write(soru8+soru4+"\n")
    file.write(soru9+soru10+"\n")
    file.write(soru4+soru8+"\n")
    file.write(soru6+soru7+"\n")
    file.write(soru7+soru6+"\n")
    file.write(soru1+soru11+"\n")
    file.write(soru1+soru10+"\n")
    file.write(soru1+soru11+soru10+"\n")
    file.write(soru1+soru11+soru9+"\n")
    file.write(soru1+"123\n")
    file.write(soru1+"1234\n")
    file.write(soru1+"12345\n")
    file.write(soru1+"123456\n")
    file.write(soru1+"1234567\n")
    file.write(soru1+"12345678\n")
    file.write(soru1+"123456789\n")
    file.write(soru1+"1234567890\n")
    file.write(soru1+soru10+"\n")
    file.write(soru1+"111\n")
    file.write(soru1+"222\n")
    file.write(soru1+"333\n")
    file.write(soru1+"444\n")
    file.write(soru1+"555\n")
    file.write(soru1+"666\n")
    file.write(soru1+"777\n")
    file.write(soru1+"888\n")
    file.write(soru1+"999\n")
    file.write(soru1+"000\n")
    file.write(soru1+soru7+"\n")
    file.write(soru1+soru7+soru10+"\n")
    file.write(soru1+soru2+soru7+"\n")
    file.write(soru1+soru4+"\n")
    file.write(soru1+soru4+soru7+"\n")
    file.write(soru1+soru9+"\n")
    file.write("123"+soru1+"\n")
    file.write("1234"+soru1+"\n")
    file.write("12345"+soru1+"\n")
    file.write("123456"+soru1+"\n")
    file.write("1234567"+soru1+"\n")
    file.write("12345678"+soru1+"\n")
    file.write("123456789"+soru1+"\n")
    file.write("1234567890"+soru1+"\n")
    file.write(soru1+soru2+"\n")
    file.write(soru1+soru2+soru9+"\n")
    file.write(soru1+soru2+"123\n")
    file.write(soru1+soru2+"1234\n")
    file.write(soru1+soru2+"12345\n")
    file.write(soru1+soru2+"12345\n")
    file.write(soru1+soru2+"123456\n")
    file.write(soru1+soru2+"1234567\n")
    file.write(soru1+soru2+"12345678\n")
    file.write(soru1+soru2+"123456789\n")
    file.write(soru1+soru2+"1234567890\n")
    file.write("123"+soru1+soru2+"\n")
    file.write("1234"+soru1+soru2+"\n")
    file.write("12345"+soru1+soru2+"\n")
    file.write("123456"+soru1+soru2+"\n")
    file.write("1234567"+soru1+soru2+"\n")
    file.write("12345678"+soru1+soru2+"\n")
    file.write("123456789"+soru1+soru2+"\n")
    file.write("1234567890"+soru1+soru2+"\n")
    file.write(soru1+soru11+"\n")
    file.write(soru11+soru1+soru11+"\n")
    file.write(soru1+soru11+soru10+"\n")
    file.write(soru1+soru3+"\n")
    file.write(soru3+soru1+"\n")
    file.write(soru3+soru1+"\n")
    file.write(soru1+soru9+soru3+"\n")
    file.write(soru1+soru10+soru3+"\n")
    file.write(soru1+soru4+soru3+"\n")
    file.write(soru3+soru4+soru1+"\n")
    file.write(soru1+soru3+soru4+"\n")
    file.write(soru4+soru3+soru1+"\n")
    file.write(soru3+soru4+"\n")
    file.write(soru4+soru3+"\n")
    file.write(soru1+soru4+"\n")
    file.write(soru4+soru1+"\n")
    file.write(soru2+soru4+"\n")
    file.write(soru4+soru2+"\n")
    file.write(soru9+soru1+"\n")
    file.write(soru1+soru4+"\n")
    file.write(soru4+soru3+"\n")
    file.write(soru3+soru2+"\n")
    file.write(soru1+"123"+soru4+"\n")
    file.write(soru4+"123"+soru1+"\n")
    file.write(soru1+soru1+"123\n")
    file.write("123"+soru1+soru1+"\n")
    file.write(soru1+"+"+soru2+"\n")
    file.write(soru2+"+"+soru1+"\n")
    file.write(soru2+soru3+"\n")
    file.write(soru3+"123"+soru2+"\n")
    file.write(soru2+"123"+soru3+"\n")
    file.write(soru1+"321\n")
    file.write("321"+soru1+"\n")
    file.write("321"+soru1+soru2+"\n")
    file.write(soru3+"321"+soru1+"\n")
    file.write(soru1+"321"+soru3+"\n")
    file.write(soru1+"321"+soru4+"\n")
    file.write(soru4+"321"+soru1+"\n")
    file.write(soru1+soru6+"\n")
    file.write(soru6+soru1+"\n")
    file.write(soru1+"123"+soru6+"\n")
    file.write(soru6+"123"+soru1+"\n")
    file.write(soru2+soru6+"\n")
    file.write(soru6+soru2+"\n")
    file.write(soru1+soru6+"\n")
    file.write(soru6+soru1+"\n")
    file.write(soru2+"123"+soru6+"\n")
    file.write(soru6+"123"+soru2+"\n")
    file.write(soru2+"+"+soru6+"\n")
    file.write(soru6+"-"+soru2+"\n")
    file.write(soru2+"-"+soru6+"\n")
    file.write(soru6+soru1+soru3+"\n")
    file.write(soru3+soru1+soru6+"\n")
    file.write(soru3+soru6+"\n")
    file.write(soru6+soru3+"\n")
    

os1=tk.Label(text="Ad: ",bg="black",fg="red",font="Verdana 11")
os1.pack()
s1=tk.Entry(bg="white",fg="black",font="Verdana 10")
s1.pack()

os2=tk.Label(text="Soyad: ",bg="black",fg="red",font="Verdana 11")
os2.pack()
s2=tk.Entry(bg="white",fg="black",font="Verdana 10")
s2.pack()

os11=tk.Label(text="Doğum Tarihinin Son İki Hanesi: ",bg="black",fg="red",font="Verdana 11")
os11.pack()
s11=tk.Entry(bg="white",fg="black",font="Verdana 10")
s11.pack()

os3=tk.Label(text="Doğum Yılı: ",bg="black",fg="red",font="Verdana 11")
os3.pack()
s3=tk.Entry(bg="white",fg="black",font="Verdana 10")
s3.pack()

os4=tk.Label(text="Yakın İsmi:  ",bg="black",fg="red",font="Verdana 11")
os4.pack()
s4=tk.Entry(bg="white",fg="black",font="Verdana 10")
s4.pack()

os6=tk.Label(text="Özel Sayı:  ",bg="black",fg="red",font="Verdana 11")
os6.pack()
s6=tk.Entry(bg="white",fg="black",font="Verdana 10")
s6.pack()

os7=tk.Label(text="Memleket Plaka Kodu: ",bg="black",fg="red",font="Verdana 11")
os7.pack()
s7=tk.Entry(bg="white",fg="black",font="Verdana 10")
s7.pack()

os8=tk.Label(text="Doğum Tarihi(ör:'01012000'): ",bg="black",fg="red",font="Verdana 11")
os8.pack()
s8=tk.Entry(bg="white",fg="black",font="Verdana 10")
s8.pack()

os9=tk.Label(text="Eklemek İstediğiniz Kelime grubu:  ",bg="black",fg="red",font="Verdana 11")
os9.pack()
s9=tk.Entry(bg="white",fg="black",font="Verdana 10")
s9.pack()

os10=tk.Label(text="Sonuna Eklemek İstediğiniz Özel Karakter: ",bg="black",fg="red",font="Verdana 11")
os10.pack()
s10=tk.Entry(bg="white",fg="black",font="Verdana 10")
s10.pack()

submit=tk.Button(text="Gönder",command=fonk1,bg="red",font="Verdana 11")
submit.pack()




root.mainloop()
