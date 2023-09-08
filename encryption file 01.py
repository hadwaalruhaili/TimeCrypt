import datetime
import random as random

def getPlainText():
    while True:
        InputChoice = input("please enter 1 to encrypt text or 2 to encrypt a file: ")
        if InputChoice == "1":
            plainText = (input("Please enter your text: ")).lower().strip()
            break
        elif InputChoice == "2":
             filename = input("Please enter your file name in full:")
             inputFile = open(filename,"r")
             plainText = inputFile.read()
             inputFile.close()
             break
        else:
            print("please enter a valid input because its not a 1 or 2")
    return plainText

def encrypt():
    global plainText,output
    output += random.choice(encryptionKey[quadrant])
    # output += encryptionKey.[quadrant][0]
    output += random.choice(dividers)
    for letter in plainText:
        encryptionOption = encryptionKey.get(letter, [])
        # print(letter)
        if encryptionOption == []:
            continue
        else:
            output += encryptionOption[quadrant]
            output += random.choice(dividers)
    # print("your encrypted text is",output)
def decrypt():
    global plainText, output
    for divider in dividers:
        plainText = plainText.replace(divider, " ")
    Words = plainText.split()
    quadrant = Words[0]
    quadrant = decryptionKey[quadrant]
    #print(quadrant)

    for word in Words[1:]:
        output += decryptionKey.get(word,"")

plainText = getPlainText()
choice = (input("Enter e to encrypt or d to decrypt: ")).strip()
output = ""
decryptionKey = {}
dividers = ["aksjhds", "w374eye3", "dljfsr", "wekjrfda", "dkjaer", "adslkjarwe"]
encryptionKey = {"a":["kljlkjafd", "akdjhre", "akajrea", "kers873"],"b":["lkjef", "aeoijrd", "dasfse","erkniee"],"c":["lk5erskjasdd", "alkjeraser", "34w8sd", "w3ehjs"],"d":["afsdasdsad","asjsdasdg","kjtuporeer","sdkjfefjpw"],"e":["dkrjtiwu","iterjtkj","roitjeriut","jsemwoskd"],"f":["drgjeirjr","dfkgjeirht","erkjtrjrt","kksefwefto"],"g":["rjoeirijirj","rjgejrtrp","jeijrrtlp","lsndjdfmel"],"h":["asdsasd","ajsdijsdij","asdnaskld","sndlkfnwen"],"i":["nsdaisjdip","skasjdasjd","askdasd","dfneppomes"],"j":["aksdajsd","asdnlasiuj","amdmsdso","sdnnwjefjmw"],"k":["drgjerpqp","iueroitr","iejrweurqi","aknqwdk"],"l":["kreotkbm","poerje","keokrwilk","sdfcwpokfe"],"m":["krngrijerr","djgejgwm","ipoermdfsd","kefwpjefke"],"n":["dfkjirior","dfgjierjeij","foipoklot","dcwejdrgh"],"o":["kepropertjertj","jwjewreekro","oicview","sdfniwpjefpw"],"p":["elroiodi","odofiewk","sdfowewek","sdfwjeldlela"],"q":["dtrmekrtrjt","lkdjfejrr","jndfrije","spkypikjt"],"r":["afasdassf","dfmsdfoke","aefejrmem","dkejpoelms"],"s":["dlreijrijpj","fjjrerer","kdmfjroeokr","dsdknfepw"],"t":["sdfkldke",",siwjerjwe","ndfklnee","djnfwempdd"],"u":["mdmfjroe","fkdjijrtjer","dlkdjigjdf","loejmesp"],"v":["dlmjgojre","djkgierjpjw","xnvnjnf","sndfhoewfd"],"w":["dfkgjeirjij",",dnfewiw","dfsejwe","sdkfnwefp"],"x":["dfngkdrgie","fmdjfpgprog","fmgdjro","fpwjmdmdsk"],"y":["sjfwjejr","mrdfgkd","sjowkwfr","aksdpjwpe"],"z":["jjjbftsk","kjgdtrsr","kjgthnlh","sdnfipekwe"]," ":["ajfiepvf","sdeklmsd","fmdfjees","dnijpwejw"],0:["posoeldodle","dffwiefwew","efjjdlsdfwe","wewkenpwfwer"],1:["ldfskedflsmd","dcniehiwelwke","sdfnwehnfwnef","edkefjwejf"], 2:["lksdfjpoels","afnlehfwie","wefnwlkenwk","wefnlwlkenfwje"], 3:["mdimsmdlr","zdnckenfwipe","sdfnkwenfwpef","sdmwekmwe"],4:["1ndioe39lmkd","sddfwmenfwe","efwkenfwkenfe","c;leflmwe"],5:["dcpe9j23kda","lsenfkwnefwe","efwlkenfwke","dke;mwe"],6:["aksdj03sdwpoek","sdlenfwefwe","werwpejrwe","dlwenrke"],7:["sadkm3pwweik3","wpefwep","ernwekrnwe","wernwklenrew"],8:["knmrneokc94j","qerlwjeowje","dselmfnwke","s;ekfw;el"],9:["erj04urfmpwo","wejwerwlekr","we,mrw;erme","sekrwkerwe"],",":["krfmwofd","wmw;lemfwe","welrnerknwe","werlwkerkwe"],".":["alknijeo0ikr","werjwekrje","sdfjem;s","asdne,rmwer"],"?":["cepmcfpemd","sdnfenfwe","sfnwenfww","elkndfwe"],"!":["slkmamsdoezd","wekrnweknr","wlesotyw","erhnwerwe"],"\n":["skdfeifwioejwe","lsmdkefieklfw","kdnfpwewee","skdfpewks"]}
for key, valuelist in encryptionKey.items():
    for value in valuelist:
        decryptionKey[value] = key
x= datetime.datetime.now()
#print(decryptionKey)
Quarter = {0:"1st quarter",1:"2nd quarter", 2: "3rd quarter", 3:"4th quarter"}
#print(x.hour)
quadrant = x.hour//6
#print(Quarter.get(quadrant,"this was an invalid time"))

if choice == "e":
    encrypt()

elif choice == "d":
    decrypt()
def writeToFile(filename,output):
    outFile = open(filename,"w")
    outFile.write(output)
    outFile.close()
    print("yout output was written to ",filename)

while True:
    outputChoice = input("enter 1 to print result, 2 to write to file, or 3 ot print and write: ")
    if outputChoice == "1":
        print("your output is",output)
        break
    elif outputChoice == "2":
        outputFileName = input("enter output filename or 0 for default:")
        if outputFileName == "0":
            writeToFile((outputFileName,output))
        else:
            writeToFile("edoutput.text",output)
        break
    elif outputChoice == "3":
        print("your output is", output)
        outputFileName = input("enter output filename or 0 for default:")
        if outputFileName == "0":
            writeToFile("edoutput.text",output)
        else:
           writeToFile(outputFileName,output)
        break
    else:
        print("this is not a valid input")




