import os
import subprocess
import shutil

var1 = input ("Numar magazin Magazin: ")
var2 = input ("Tip PC SERVER sau SECUNDAR: ")
var3 = input ("Localitatea: ")
#nume PC si WorkGrup
with open ('NumePC.bat', mode='w') as my_file:
    textul = my_file.write (
        '@echo off \n' + 'wmic computersystem where caption=\"%COMPUTERNAME%\" rename ' + 'Profi' + str (var1) + str (
            var2) + '\nnet config server /srvcomment:\"' + 'Profi' + str (var1) + str (
            var2) + '\"' + '\nwmic computersystem where name=\"%computername%\" call joindomainorworkgroup name=\"' + 'Profi' + var1 + '\"' + '\nexit')

def StartBat1 ():
    subprocess.call ([r'NumePC.bat'])


with open ('Owner.reg', mode='w') as my_file:
    textul = my_file.write (
        'Windows Registry Editor Version 5.00\n' + '\n[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion]' + '\n\"RegisteredOwner\"=\"Magazin ' + str (
            var1) + ' ' + str (var3) + ' ' + str (var2) + '\"')


def StartBat2 ():
    os.system ('cmd /c "regedit.exe /S Owner.reg"')


with open ('D:\Pricing Test\Optiuni.xml', mode='w') as my_file:
    textul = my_file.write (
        '<Optiuni>\n <DirectorLog>D:\\Pricing Test\\Fisiere LOG</DirectorLog>\n <Zile>3</Zile>\n <Magazin>' + str (
            var1) + '</Magazin>\n <DirectorNomenclator>D:\\Pricing Test\\Nomenclatorpricing</DirectorNomenclator>\n <DirectorExport>D:\Pricing Test\Fisiere Exportate</DirectorExport>\n <DirectorRaport>D:\Pricing Test\Fisiere Raport</DirectorRaport>\n <ConnDB>prod</ConnDB>\n <UtilizatorDB>scanner</UtilizatorDB>\n <ParolaDB>sc8n0ner</ParolaDB>\n <TimeDB>7</TimeDB>\n <DirectorAnalizaV>E:\Documente\Etichete RBC</DirectorAnalizaV>\n <Config>1</Config>\n <LogONOFF>0</LogONOFF>\n <ReincercariDescarcare>3</ReincercariDescarcare>\n <GoldG>23.10.2017</GoldG>\n <WinMob>\n </WinMob>\n <ActNom>\n </ActNom>\n <TelServer>\n </TelServer>\n <TelUser>\n </TelUser>\n <TelPass>\n </TelPass>\n <NoCipherLab>0</NoCipherLab>\n <IntervalCS>00:01-12:00</IntervalCS>\n <IntervalPL>00:01-22:00</IntervalPL>\n <DepozitControl>0</DepozitControl>\n</Optiuni>\n')

var4 = int(var1)

# Shorcut Link

class0 = "10.10"
class1 = "10.20."
class2 = "10.21."
class3 = "10.22."
class4 = "10.23."
class5 = "10.24."
clasa6 = "10.25."

if 1000 < var4 <= 1020:
    clasa_mag = class1 + str (var4 - 1000)
elif 2000 <= var4 <= 2250:
    clasa_mag = class1 + str (var4 - 2000)
elif 2251 <= var4 <= 2500:
    clasa_mag = class2 + str (var4 - 2250)
elif 2501 <= var4 <= 2750:
    clasa_mag = class3 + str (var4 - 2500)
elif 2751 <= var4 <= 3000:
    clasa_mag = class4 + str (var4 - 2750)
elif 3001 <= var4 <= 3250:
    clasa_mag = class5 + str (var4 - 3000)
elif 3251 <= var4 <= 3500:
    clasa_mag = class6 + str (var4 - 3250)
else:
    print ("Magazinul nu exista!\nIntrodu numarul corespunzator unui Magazin PROFI!")

with open ('TPLinux.vbs', mode='w') as my_file:
    textul = my_file.write (
        'Set oWS = WScript.CreateObject(\"WScript.Shell\")\nsLinkFile = \"C:\\Users\magazin\\Desktop\\Tp Linux.lnk\"\nSet oLink = oWS.CreateShortcut(sLinkFile)\noLink.TargetPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"\noLink.Arguments = "' + str (
            clasa_mag) + '.20"\noLink.Save')

with open ('Facturare.vbs', mode='w') as my_file:
    textul = my_file.write (
        'Set oWS = WScript.CreateObject(\"WScript.Shell\")\nsLinkFile = \"C:\\Users\magazin\\Desktop\\Facturare.lnk\"\nSet oLink = oWS.CreateShortcut(sLinkFile)\noLink.TargetPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"\noLink.Arguments = "' + str (
            clasa_mag) + '.20:35000"\noLink.Save')

StartBat1()
StartBat2()
subprocess.call ("cmd /c TPLinux.vbs")
subprocess.call ("cmd /c Facturare.vbs")
