import os

account_no=None

def login():
    global account_no
    account_number = input("Hesap numaranızı girin: ")
    password = input("Şifrenizi girin: ")
    sifre=""
    if os.path.exists(account_number + ".txt"):
        with open(account_number + ".txt", "r") as file:
            correct_password = file.readline().split()
            for i in correct_password:
                sifre+=i
            print(sifre)
            if password == sifre:
                account_no = account_number
                print("Giriş başarılı!")
                print()
                
                Operating_ChapterOperatings()
            else:
                print("Hatalı şifre!")
    else:
        print("Hesap bulunamadı!")
   
def SingUp():
    global account_no
    password = input("Şifrenizi girin: ")
    bakiye=0
    if os.path.exists(account_no + ".txt"):
        print("Bu hesap numarası zaten var!")
    else:
        with open(account_no + ".txt", "w") as file:
            file.write(password + "\n"+"{} ".format(bakiye))
            file.close()
        print("Kayıt başarılı!")
        
def Draw_Money():
    global account_no
    bakiye = 0  
    if os.path.exists(account_no + ".txt"):
        miktar = int(input("Hesabınızdan ne kadar para çekeceksiniz: "))
        
        with open(account_no+ ".txt", "r+") as file:
            lines = file.readlines()
            sifre = lines[0].strip()  
            bakiye = int(lines[1])  
            if bakiye < miktar:
                print("Hesap bakiyesi yetersiz")
                input("İşlemler sayfasına dönmek için Enter'a basınız")
                Operating_ChapterOperatings()
            else:
                bakiye -= miktar
                file.seek(0)  
                file.write(sifre + "\n" + str(bakiye)) 
                print("Para çekme işlemi başarılı. Yeni bakiye:", bakiye)
    else:
        print("Hesap bulunamadı!")
        
def Send_Money_SelfAccount():
    global account_no
    bakiye = 0    
    if os.path.exists(account_no + ".txt"):
        with open(account_no + ".txt", "r+") as file:
            lines = file.readlines()
            bakiye = int(lines[1])  # Dosyanın ikinci satırı bakiyeyi içeriyor
            
            miktar = int(input("Hesabınıza ne kadar para yatıracaksınız: "))
            if miktar < 0:
                print("Geçersiz miktar. Pozitif bir değer girin.")
                Send_Money_SelfAccount()
                return
            
            yeni_bakiye = bakiye + miktar
            lines[1] = str(yeni_bakiye) + "\n"  # Yeni bakiyeyi ikinci satıra yaz
            
            file.seek(0)  # Dosya imlecini başa al
            file.writelines(lines)  # Yenilenmiş satırları dosyaya yaz
            print(f"Yeni bakiye: {yeni_bakiye}")
            input("Anamenüye dönmek için Enter'a basın")
            Operating_ChapterOperatings()
    else:
        print("Hesap bulunamadı!")


def Send_Money_ToAnotherAccount():
    global account_no
    kaynak_hesap=account_no
    hedef_hesap=input("Para göndermek istediğiniz hesabın 'hesap numarasını' giriniz: ")  
    if os.path.exists(hedef_hesap + ".txt"):    
        miktar = int(input("Hesaba ne kadar para aktarılacak: ")) 
        with open(kaynak_hesap+ ".txt", "r+") as file:
            lines = file.readlines()
            sifre = lines[0].strip()  
            bakiye = int(lines[1])  
            if bakiye < miktar:
                print("Hesap bakiyesi yetersiz")
                input("İşlemler sayfasına dönmek için Enter'a basınız")
                Operating_ChapterOperatings()
            else:
                bakiye -= miktar
                file.seek(0)  
                file.writelines(sifre + "\n" + str(bakiye)) 
    else:
        print("Yanlış veya hatalı hesap numarası girişi yaptınız")             
                
    if os.path.exists(kaynak_hesap + ".txt"):
             
        with open(hedef_hesap + ".txt", "r+") as file:
                lines = file.readlines()
                sifre=lines[0]
                bakiye = int(lines[1])  
                                
                if miktar < 0:
                    print("Geçersiz miktar. Pozitif bir değer girin.")
                    Send_Money_ToAnotherAccount()
                    return
                
                yeni_bakiye = bakiye + miktar
                lines[0]=sifre
                lines[1] = str(yeni_bakiye) + "\n" 
                
                file.seek(0) 
                file.writelines(lines)  
                print(f"Yeni bakiye: {yeni_bakiye}")
                input("Anamenüye dönmek için Enter'a basın")
                Operating_ChapterOperatings() 
    else:
        print("Yanlış veya hatalı hesap numarası girişi yaptınız")            

def Show_Balance():
    global account_no
     
    if os.path.exists(account_no + ".txt"):  
        with open(account_no+ ".txt", "r+") as file:
            lines = file.readlines()              
            bakiye = int(lines[1])
            print("{} numaralı hesabınızda {} miktar para bulunmakta".format(account_no,bakiye))
            input("Başka bir işlem yapmak için enter'a basınız") 
            Operating_ChapterOperatings()
                                              
def Operating_ChapterOperatings():
            
    TransactionsText="""
        Transactions İnterface of X Bank
    
    1) Hesaptan Para Çekme   
    2) Kendi Hesabına Para Yatırma
    3) Başka Hesaba Para Yatırma
    4) Hesap bakiyesi Görüntüleme
    Q) Sistemden Çıkış
    """ 
    print(TransactionsText)
    
    secim=input("Yapmak istediğiniz işlem numarasını giriniz: ")
    
    if secim == '1':
        Draw_Money()
    elif secim == '2':
        Send_Money_SelfAccount()
    elif secim=="3":
        Send_Money_ToAnotherAccount()
    elif secim=="4":
        Show_Balance()        
    elif secim == 'Q':
        quit()
    else:
        input("Hatalı işlem numarası girişi oldu enter ile login ekranına dönebilirsiniz.") 

def Operating_ChapterLogin():
    LoginText="""
        Login İnterface of X Bank

    1) Giriş Yapmak
    2) Kaydolmak
    Q) Çıkış Yapmak
    """ 
    print(LoginText)
    secim=input("Yapmak istediğiniz işlem numarasını giriniz: ")
    
    
    if secim == '1':
        login()
    elif secim == '2':
        SingUp()
    elif secim == 'Q':
        quit()
    else:
        input("Hatalı işlem numarası girişi oldu enter ile login ekranına dönebilirsiniz.")
        Operating_ChapterLogin()  

       
Operating_ChapterLogin()              

