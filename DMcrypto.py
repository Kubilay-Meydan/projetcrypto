'''
Texte 1:

kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd.

clef 1:
Z, ou ZZ, ou ZZZ.....

Texte dechiffre 1: 

le prochain fichier aura un code par substitution alphabetique: chaque lettre est remplacee par une autre. utiliser la frequence des lettres pour decoder le message.

Texte 2:

gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi.\

Clef 2: y'en a pas

Texte dechiffre 2:

LE PROCHAIN FICHIER EST CODE PAR UN MOT DE PASSE DE TAILLE INCONNUE ET CONTIENT L'INDICE. LES LETTRES DU MOT DE PASSE PERMETTENT DE DECALER LES LETTRES DU MESSAGE ORIGINAL MODULO 26. SEULES LES LETTRES DE A A Z SONT CHIFFREES. 

Texte 3:

dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?

Clef 3:

lettre 1 = c
lettre 2 = l
lettre 3 = e
lettre 4 = z

Texte dechiffre 3: 

BRAVO A L AIDE DE L INDICE VOUS AVEZ REUSSI A CASSER CE CODE ET A FINIR CE DEVOIR  LE DERNIER TEXTE EST POUR LES BRAVES  REGARDEZ VOUS DANS UN MIROIR  EN ETES VOUS UN ?

Texte 4:

kv qsteiadw qrs gqfmem zwrno c'rvjmq toirt cen bizeiw ofimw el Miwjhuz pvz ysqnvno rbes vdwvr pdt sdrffj à bvc iy evvjvdvis hd krjthrlen kfj vvzjxnzir u'vvffet et eiy sslfai ev wykmvs  if vjycsrin obj xvdwvr wzoj neupzr wh ca ptov nstt sjr grus zji yi uyuii b ui bpke tnjetp rj lz rpcedp fjt jqpzd wh cen pvrtmi trinsmt nz rpet zqbzmzrs huz pvrtmi trnn zwfim dtjati ev ksquvr ymf rjfd jum kfj bvzous fnvceqeqej


clef 4: bravez

JE VOUDRAIS PAS CREVER AVANT D AVOIR CONNU LES CHIENS NOIRS DU LEXIQUE QUI DORMENT SANS REVER LES SINGES C CUL NU DEVOREURS DE TROPIQUES LES ARAIGNEES D ARGENT AU NID TRUFFE DE 
BULLES  JE VOUDRAIS PAS CREVER SANS SAVOIR SI LA LUNE SOUS SON FAUX AIR DE THUNE A UN COTE POINTU SI LE SOLEIL EST FROID SI LES QUATRE SAISONS NE SONT VRAIMENT QUE QUATRE SANS AVOIR ESSAYE DE PORTER UNE ROBE SUR LES GRANDS BOULEVARDS
'''


#permet de tester des clefs plus facilement 

code_chiffre = str(input("entrez le code a modifier:"))
clef = str(input("entrez une clef de dechiffrage:"))



#code qui deplace la valeur ascii d'un message et retourne le message associe aux nouvelles valeurs ascii.
def code_vigenere1 ( message, clef) :
    
    #le message code sera en forme de liste
    message_code = []


    for i,c in enumerate(message) :


        #decalage ascii
        d = clef[ i % len(clef) ]
        d = ord(d) - 65
        d = 26 - d

        #pour eviter que les ".", les espaces et les ":" soient traduits, je ne prends que les caracteres avec une valeur ascii superieur a 65,
        #  ce qui comprends les lettres de A a Z + d'autres caracteres bizares qui ne sont pas dans les messages. 
        if ord(c) <= 65:
            
            correspondant = " " 
            
        else:
           correspondant = chr((ord(c)-65+d)%26 + 65) 
       
        #append les lettres dechiffres dans la liste
        message_code += correspondant

        #permet d'avoir un message lisible et non une liste
        message_code = "".join(message_code)
    return message_code


#foction qui permet de decouper le texte en un nomnre de segments donne
def decouper(texte,Nombre_De_Segments):
    #les segments seronts stoques sous forme de listes
    global segments
    segments = []
    #la taille est definie par la division de la taille du texte par le nb de segments
    tailleSegment = int(len(texte)/Nombre_De_Segments)
    #prints de verifications
    print(len(texte))
    print(tailleSegment)
    #decoupage et stockage des segents
    for i in range(0,Nombre_De_Segments):
        segments.append(texte[i * tailleSegment  :i * tailleSegment + tailleSegment])
    #permet de se rajouter le dernier caractere a la derniere liste si la phrase n'est pas divisible sans reste
    if len(texte) % Nombre_De_Segments :
        segments[-1] = segments[-1] + texte[-1]
    #prints de verifications
    for i in range(len(segments)):
        print(len(segments[i]))
    print(segments)
    
#fonction permetant de calculer la frequence de chaque caractere dans un texte donne
def frequence(code_chiffre):
    #on echappe pas a la regle, tout est stocke en listes
    resultat = []
    resultatTrie = []
    listeFreq = []
    nbLettres = 0
    #calcul du nombre de lettres dans le texte
    for c in code_chiffre:
        if 97 <= ord(c) < 123:
            nbLettres += 1
    #cherche les caracteres du texte et stock leurs valeurs dans resultat
    for i in range(97, 123):
        if chr(i) in code_chiffre:
            resultat.append((chr(i), round(code_chiffre.count(chr(i))/nbLettres*100,2)))
    #prend les frequences d'apparition et les stockent dans listeFreq
    for i in resultat:
        listeFreq.append(i[1])
    #trie les resultats du plus frequent au moins frequent
    while(len(listeFreq)):
        indexMax = listeFreq.index(max(listeFreq))
        resultatTrie.append(resultat[indexMax])
        resultat.remove(resultat[indexMax])
        listeFreq.remove(listeFreq[indexMax])
    return resultatTrie




def sub(code_chiffre, alphabet_de_sub):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    result = ""
    liste = []
    for i in range(len(code_chiffre)):
        liste.append(code_chiffre[i])



    for i in range(len(liste)):
        if liste[i] in alphabet:
            #underscore n'est pas une lettre
            #et va permettre de remplaccer les lettres non utilises
            if liste[i] in alphabet_de_sub:
                x = alphabet_de_sub.index(liste[i])
                result += str(alphabet[x])
        else:
            result += str(liste[i])

    return result



def inverse(texte):
    texte_inverse = []
    long = len(texte)
    for i in texte:
        texte_inverse.append(texte[0 + long-1])
        long -= 1

    texte_inverse = "".join(texte_inverse)
    return texte_inverse


#prints
print(sub(code_chiffre, "n_vcxwmlk__gfdsq_oiuy_____"))
#print(decouper(code_chiffre, 38))
print(frequence(code_chiffre))
#print(code_vigenere1(code_chiffre, clef))
#print(frequence(segments[0]))
#print(frequence(segments[1]))
#print(frequence(segments[2]))
#print(frequence(segments[3]))
