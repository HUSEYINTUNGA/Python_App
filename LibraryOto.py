Aktif_Kitaplar=list()
Pasif_Kitaplar=list()

Islem="""
0-Kitap Ekle
1-Kitap Sil
2-Kitap Guncelle
3-Aktif Kitaplari Listele
4-Emanetteki Kitapları Listele
5-Kitap Emanet Al
6-Cikis Yap
"""

def Add():
    name=str(input("Lütfen kitap ismini giriniz "))  
    Aktif_Kitaplar.append(name)

def Delete():
    if len(Aktif_Kitaplar)==0:
        print("Listede Kayıtlı Hiç Bir Kitap Bulunamadı.")
    else:    
        name=str(input("Lütfen silmek istediğiniz kitap ismini giriniz "))
        Aktif_Kitaplar.remove(name)            

def Update():
    if len(Aktif_Kitaplar)==0:
        print("Listeye Kayıtlı Hiç Bir Kitap Bulunamadı")
    else:
        bfrname=str(input("Güncellemek istediğiniz kitabın listedeki ismini giriniz "))
        aftname=str(input("Güncellemek istediğiniz kitabın yeni ismini giriniz "))
        Aktif_Kitaplar.remove(bfrname)
        Aktif_Kitaplar.append(aftname)
    
def Show(liste):
    if len(liste)==0:
        print("Listelenecek kitap yok!")
    else:    
        for i in liste:
            print(i)    
        
def ToReserve():
    if len(Aktif_Kitaplar)==0:
        print("Emanet alabileceğiniz bir kitap yok")
    else:    
        name=str(input("Emanet almak istediğiniz kitap ismini giriniz "))
        Aktif_Kitaplar.remove(name)
        Pasif_Kitaplar.append(name)
    
while True:
    print(Islem)   
    islem=int(input("Lütfen yapmak istediğiniz işlem numarasını giriniz "))
    print()
    if islem==0:
        Add()
    elif islem==1:
        Delete()
    elif islem==2:
        Update()
    elif islem==3:
        Show(Aktif_Kitaplar)
    elif islem==4:
        Show(Pasif_Kitaplar)
    elif islem==5:
        ToReserve()
    elif islem==6:
        break


