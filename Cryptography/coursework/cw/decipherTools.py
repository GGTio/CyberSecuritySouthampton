import operator

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
FREQ = {"a":0.0815,"b":0.0144,"c":0.0276,"d":0.0379, "e":0.1311, "f":0.0292, "g":0.0199, "h":0.0526, "i":0.0635, "j":0.0013, "k":0.0042, "l":0.0339, "m":0.0254, "n":0.0710, "o":0.08, "p":0.0198, "q":0.0012, "r":0.0683, "s":0.0610, "t":0.1047, "u":0.0246, "v":0.0092, "w":0.0154, "x":0.0017, "y":0.0198, "z":0.0008}
sorted_list_frequencies = []
all_letters = {}

# General analysis of cipher under different shifts
def complete_frequency_analysis(text):
    # FInd the frequency for each letter
    frequency_analysis(text)
    # Correlation of frequencies
    correlations=[]
    for shift in range(26):
        print(str(shift) +" : ",end='')
        correlations.append(correlation(shift,text))



# This is trying to find the right shift by comparing
def correlation(shift,text):
    somme = 0.0
    index_of_all_letters = []
    for letter in all_letters:
        index_of_all_letters.append(alphabet.index(letter.lower()))
    for c in index_of_all_letters:
        # f(c) -> frequency of c in cyphertext
        # p(c-letter) -> regular frequency of character  c if it was shifted to the left
        somme += frequency(c,text)*p((c-shift)%26)
    print(somme)
    return somme

# frequency of a letter in the english dictionary
def p(letter):
    return FREQ[alphabet[letter]]

# frequency of character given in the cyphertext
def frequency(index_char,text):
    result = 0
    for freq in sorted_list_frequencies:
        if freq[0] == alphabet[index_char]:
            result=float(freq[1])
    return result

# Simply applies a given shift to a given text
def shift(text,rotation):
    chars = ''.join([i for i in text if i.isalpha()])
    result=""
    for i in chars:
        result+=alphabet[(alphabet.index(i.lower())-rotation)%26]
    print(result)
    return result

# Index of coincidence
def basic_IC(text):
    chars = ''.join([i for i in text if i.isalpha()])
    find_all_letters(text)
    IC = 0.0
    for letter in all_letters:
        #print(all_letters[letter])
        #print(all_letters[letter]*(all_letters[letter] - 1))
        IC += all_letters[letter]*(all_letters[letter] - 1)
    #print(IC)
    #print((len(chars)*(len(chars)-1)))
    IC/=(len(chars)*(len(chars)-1))
    print(IC)
    return IC

# 2nd Method
def advanced_IC(text):
    result = basic_IC(text)*26
    return result

def find_key_length(text):
    chars = ''.join([i for i in text.lower() if i.isalpha()])
    # test key lengths from 1 to 10
    for length in range(1,11):
        column_strings = ["" for x in range(length)]
        text_divided = []
        division = ""
        for index in range(1,len(chars)+1):
            division+= chars[index-1]
            if index%length==0:
                text_divided.append(division)
                division=""
        for row in text_divided:
            for char in range(len(row)):
                column_strings[char] += row[char]
        print("=================")
        print("key length: "+str(length))
        delta_bar_IC = 0.0
        for i in column_strings:
            delta_bar_IC+= advanced_IC(i)
            # After finding the most likely key lengths let's look for the possible shifts for each column
            complete_frequency_analysis(i)
        print(delta_bar_IC/length)



# All letters used
def find_all_letters(text):
    all_letters.clear()
    clean_text = ''.join([i for i in text.lower() if i.isalpha()])
    for letter in clean_text:
        if letter not in all_letters:
            all_letters[letter] = 1
        elif letter in all_letters:
            all_letters[letter] += 1

def frequency_analysis(text):
    frequencies={}
    find_all_letters(text)
    for letter in all_letters:
        frequencies[letter]= "%.3f" % (all_letters[letter]/len(text))
    sorted_list_frequencies.extend(sorted(frequencies.items(), key=operator.itemgetter(1)))


# letters not used
def letters_not_used(text):
    all_letters = find_all_letters(text).keys()
    print("all letters: "+str(all_letters))
    print("alphabet length:"+str(len(all_letters)))
    alphabet_used = [chr(i) for i in range(127)]
    list_of_letters_not_used = [x for x in alphabet_used if x not in all_letters]
    print(list_of_letters_not_used)
    print("nb letters not used: "+str(len(list_of_letters_not_used)))
    print()

# repeating words
def repeating_patterns(text):
    dict_of_patterns = {}
    for block_size in range(12,13):
        for index in range(len(text)-block_size):
            pattern = text[index:index+block_size+1]
            dict_of_patterns = dict_check(pattern,dict_of_patterns)
            dict_of_patterns[pattern]+=finding_patterns(text,pattern)
    dict_of_patterns = dict_cleaning(dict_of_patterns)
    print(dict_of_patterns)


def dict_check(pattern,dict):
    if pattern not in dict:
        dict[pattern] = 1
    elif pattern in dict:
        dict[pattern] += 1
    return dict

def finding_patterns(text,pattern):
    list_of_indexes = [n for n in range(len(text)) if text.find(pattern, n) == n]
    if pattern == '\x17<E?RzZ;E1R.\x17':
        print(list_of_indexes)
    return len(list_of_indexes)

def dict_cleaning(dict):
    list_to_del = []
    for key in dict:
        if dict[key] == 1 or dict[key] == 2 or dict[key] == 5 or dict[key] == 6 or dict[key] == 7 or dict[key] == 8 or dict[key] == 9:
            list_to_del.append(key)
    for pattern in list_to_del:
        del dict[pattern]
    return dict

def findKey(text):
    key1=""
    key2=""
    for i in range(len(text)):
        if i ==0:
            key1 = ord(text[i]) ^ ord('A')
        elif i == 1:
            key2 = ord(text[i]) ^ ord(' ')
    print("key1: "+str(chr(key1)))
    print("key2: "+str(chr(key2)))

def decrypt(key,text):
    plain=""
    for i in range(len(text)):
        if i%2==0:
            plain+=chr(ord(text[i]) ^ ord(key[0]))
        elif i%2==1:
            plain+=chr(ord(text[i]) ^ ord(key[1]))
    print(plain)

def sum_binary(filename):
    file = open(filename, "rb")
    try:
        byte = file.readlines()
        print(byte)
        work = str(byte[0])
        work = work.replace("b","")
        work = work.replace("'", "")
        print("work: "+str(work))
        list_work=work.split(" ")
        print(list_work)
        list_work.pop()
        result = "00000000"
        for i in list_work:
            result = str(bin(int(result,2) ^ int(i,2)))
        print(result)
    finally:
        file.close()

def find_key(text):
    #ascii chr
    ll = [chr(i) for i in range(128)]
    list_=[]
    for key1 in ll:
        for key2 in ll:
            possible_answer = ""
            for index in range(len(text)):
                if index%2 == 0:
                    possible_answer+= chr(ord(text[index]) ^ ord(key1))
                elif index%2 == 1:
                    possible_answer+= chr(ord(text[index]) ^ ord(key2))
            list_.append(possible_answer)
    list_ = test_list(list_)
    cap = []
    low = []
    for i in list_:
        if i.isupper():
            cap.append(i)
        elif i.islower():
            low.append(i)
    print(cap)


def test_list(liste):
    final=[]
    for i in range(len(liste)):
        if liste[i].isalpha():
            final.append(liste[i])
    return final

def decode_beaufort(text):
    dict={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}
    decoded=""
    for i in text:
        decoded+=dict[i]
    print(decoded)


# First rapid analysis to see if it is a shifted or a vigenere like encryption
#print(basic_IC("Iak rhsexzxmodg oh yug igexxh mnpm ctkk enhabywxj qxzlxkc Wkrxsqxx pgj Dvzdukg , tts mnpm ywhc pg ujmyittsbtv vucmxxuaibuc mu rrhtkytvagbzn lixxtrx. Zwx idfvtmoibuc pgh vxttztw zd lzxfaatzt kkhxggvn ihcpkj iak sxbteuefkcm uu lehmkbl zwtz pkk gxyxeotgz ih inukg tzitizl. Kcmxxxy pkk ynjvxj dg yrbkcmoubi bxxxm, zwx yikkczzw tts lovgoubipgit hl iak lhxz kkehxixj."))

#frequency_analysis("Iak rhsexzxmodg oh yug igexxh mnpm ctkk enhabywxj qxzlxkc Wkrxsqxx pgj Dvzdukg , tts mnpm ywhc pg ujmyittsbtv vucmxxuaibuc mu rrhtkytvagbzn lixxtrx. Zwx idfvtmoibuc pgh vxttztw zd lzxfaatzt kkhxggvn ihcpkj iak sxbteuefkcm uu lehmkbl zwtz pkk gxyxeotgz ih inukg tzitizl. Kcmxxxy pkk ynjvxj dg yrbkcmoubi bxxxm, zwx yikkczzw tts lovgoubipgit hl iak lhxz kkehxixj.")

#print(sorted_list_frequencies)

#find_key_length("Iak rhsexzxmodg oh yug igexxh mnpm ctkk enhabywxj qxzlxkc Wkrxsqxx pgj Dvzdukg , tts mnpm ywhc pg ujmyittsbtv vucmxxuaibuc mu rrhtkytvagbzn lixxtrx. Zwx idfvtmoibuc pgh vxttztw zd lzxfaatzt kkhxggvn ihcpkj iak sxbteuefkcm uu lehmkbl zwtz pkk gxyxeotgz ih inukg tzitizl. Kcmxxxy pkk ynjvxj dg yrbkcmoubi bxxxm, zwx yikkczzw tts lovgoubipgit hl iak lhxz kkehxixj.")

find_key("RYJWLRMCRYMSJFMUKSQCK^HEU_JZQQ@QPSQQFWPX@DFFQCD[LRJB@EWBKBU_DDK_J_QAMUHBMAJBV^WBS_VXPXJSJ_")

#find_key('<E?RzZ;E1R.>X?DzY5CzE?F/vç^(RzC2RzR"^)C?Y9RzX<9X7G?C3C3X42X-R,R(3CzS5R)(R+B3E?;<E;Z?@5E1._;CzV6[5@)4R-7V(\?CzR4C(V4C)z?Y9Rz^4._?6V9\zX<9X?E9^,RzU;E(^?E)zV4Sz^47V(\?C)-^._z[5@zR4C(NzT5D.3Cz^)=R4R(V6[#/Y>R(D.X5SzC2V.9X7G?C3C3X4<[5B(^)_?Dz^4;<E?RwZ;E1R.?Y,^(X4Z?Y.zN*^9V6[#zVzZ5S?E4<E?RzZ;E1R.?T5Y5Z#-X/[>3Y9[/S?5C2R(<R;C/E?Dv)B9_zV);)C5T1?O9_;Y=RzV4SzVzQ3Y;Y9^;[zD?E,^9R))R9C5Ev8B.._?NzS54X.>R<^4Rz^.zt(^.^9DzX<._?<E?RzZ;E1R.2V,RzV(P/R>._;Cv3YzE?V6-X([>)^.B;C3X4Dv3Cz_;DzG(X,R4.XzU?)B)T?G.^8[?.XzC2RzS?A?[5G7R4CzX<*E3T?<^"^4PzZ5Y5G5[3R)zd/T2(R;D5Y3Y=2V)6R>3YzC2RzG;D..XzP5A?E4Z?Y.3Y.R(A?Y.^5YtCz^)<V3EzC5)V#._;CzX4[#5Y?1Y5@4?O;Z*[?5QzVzC(B?<E?RzZ;E1R.?O3D.DzV4SzC2V.3DzC2Rzu6V9\zz;E1R.zc2V.3DzC5)V#zV4N5Y?9V4*E5S/T?;Y#C2^4PzV.;Y#.^7Rv;Y>;Y#X4RzT;YzG/E9_;D?;Y#C2^4PzV,V3[;U6RzV.;Y#.^7Rt')

#find_key_length("THERE ARETW OWAYS OFCON STRUC TINGA SOFTW AREDE SIGNO NEWAYISTOM AKEIT SOSIM PLETH ATTHE REARE OBVIO USLYN ODEFI CIENCIESAN DTHEO THERW AYIST OMAKE ITSOC OMPLI CATED THATT HEREARENOO BVIOU SDEFI CIENC IESTH EFIRS TMETH ODISF ARMOR EDIFFICULT")

#shift("THERE ARETW OWAYS OFCON STRUC TINGA SOFTW AREDE SIGNO NEWAYISTOM AKEIT SOSIM PLETH ATTHE REARE OBVIO USLYN ODEFI CIENCIESAN DTHEO THERW AYIST OMAKE ITSOC OMPLI CATED THATT HEREARENOO BVIOU SDEFI CIENC IESTH EFIRS TMETH ODISF ARMOR EDIFFICULT",1)


#basic_IC("THERE ARETW OWAYS OFCON STRUC TINGA SOFTW AREDE SIGNO NEWAYISTOM AKEIT SOSIM PLETH ATTHE REARE OBVIO USLYN ODEFI CIENCIESAN DTHEO THERW AYIST OMAKE ITSOC OMPLI CATED THATT HEREARENOO BVIOU SDEFI CIENC IESTH EFIRS TMETH ODISF ARMOR EDIFFICULT")

#advanced_IC("THERE ARETW OWAYS OFCON STRUC TINGA SOFTW AREDE SIGNO NEWAYISTOM AKEIT SOSIM PLETH ATTHE REARE OBVIO USLYN ODEFI CIENCIESAN DTHEO THERW AYIST OMAKE ITSOC OMPLI CATED THATT HEREARENOO BVIOU SDEFI CIENC IESTH EFIRS TMETH ODISF ARMOR EDIFFICULT")

#basic_IC("Iak rhsexzxmodg oh yug igexxh mnpm ctkk enhabywxj qxzlxkc Wkrxsqxx pgj Dvzdukg , tts mnpm ywhc pg ujmyittsbtv vucmxxuaibuc mu rrhtkytvagbzn lixxtrx. Zwx idfvtmoibuc pgh vxttztw zd lzxfaatzt kkhxggvn ihcpkj iak sxbteuefkcm uu lehmkbl zwtz pkk gxyxeotgz ih inukg tzitizl. Kcmxxxy pkk ynjvxj dg yrbkcmoubi bxxxm, zwx yikkczzw tts lovgoubipgit hl iak lhxz kkehxixj.")

#advanced_IC("Iak rhsexzxmodg oh yug igexxh mnpm ctkk enhabywxj qxzlxkc Wkrxsqxx pgj Dvzdukg , tts mnpm ywhc pg ujmyittsbtv vucmxxuaibuc mu rrhtkytvagbzn lixxtrx. Zwx idfvtmoibuc pgh vxttztw zd lzxfaatzt kkhxggvn ihcpkj iak sxbteuefkcm uu lehmkbl zwtz pkk gxyxeotgz ih inukg tzitizl. Kcmxxxy pkk ynjvxj dg yrbkcmoubi bxxxm, zwx yikkczzw tts lovgoubipgit hl iak lhxz kkehxixj.")

#find_key_length("QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV")

#advanced_IC("QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV")

#complete_frequency_analysis("KHOORZRUOG")

#correlation()

#find_key("UJYMBJE@S@BBXVDQWH_@WRD@USEHUQSITJ_WXSZPX@SWFLSK")

#asterios("|DmEpP|ToXuX{PpXuRkTxA`B]u_|\cB}TkRwX|HkEpPmXmV|E")

#frequency_analysis("RYJWLRMCRYMSJFMUKSQCK^HEU_JZQQ@QPSQQFWPX@DFFQCD[LRJB@EWBKBU_DDK_J_QAMUHBMAJBV^WBS_VXPXJSJ")

#find_key("RYJWLRMCRYMSJFMUKSQCK^HEU_JZQQ@QPSQQFWPX@DFFQCD[LRJB@EWBKBU_DDK_J_QAMUHBMAJBV^WBS_VXPXJSJ_")

#find_key("OVZ]KMZLLKFWFY]_GLGM[VMKZUFW]LLQ]YEJLYF\YQ]VDPGVL_GP\TYPMUBAHMEQHYLUKK@VESZWE]OV@Q@JL^LW")

#resuuult=['fnsebustesoooatgntnurndssmootteitalreaodpitnmhnnegnhulphdmkyauliaaembsinlksolefniiirefeo', 'fmsfbvswepolobtdnwnvrmdpsnoltwejtblqebogpjtmmknmednkuopkdnkzavljabenbpimlhsllffmijiqeeel', 'enpeauptfslolawgmtmuqngspmlowtfiwaorfaldsiwnnhmnfgmhvlshgmhybuoibafmasjnokpooeenjijrfffo', 'empfavpwfplllbwdmwmvqmgppnllwwfjwboqfblgsjwmnkmmfdmkvoskgnhzbvojbbfnapjmohplofemjjjqfefl', 'anteeuttbshohasgitiuuncstmhostbisakrbahdwisnjhinbgihrlwhcmlyfukifabmesnnkktokeanninrbfbo', 'amtfevtwbphlhbsdiwivumcptnhlswbjsbkqbbhgwjsmjkimbdikrowkcnlzfvkjfbbnepnmkhtlkfamnjnqbebl']

#after_xor("RYJWLRMCRYMSJFMUKSQCK^HEU_JZQQ@QPSQQFWPX@DFFQCD[LRJB@EWBKBU_DDK_J_QAMUHBMAJBV^WBS_VXPXJSJ_")

#sum_binary("binary.txt")

#decrypt("Z7",'<E?RzZ;E1R.>X?DzY5CzE?F/^(RzC2RzR"^)C?Y9RzX<9X7G?C3C3X42X-R,R(3CzS5R)(R+B3E?;<E;Z?@5E1._;CzV6[5@)4R-7V(\?CzR4C(V4C)z?Y9Rz^4._?6V9\zX<9X?E9^,RzU;E(^?E)zV4Sz^47V(\?C)-^._z[5@zR4C(NzT5D.3Cz^)=R4R(V6[#/Y>R(D.X5SzC2V.9X7G?C3C3X4<[5B(^)_?Dz^4;<E?RwZ;E1R.?Y,^(X4Z?Y.zN*^9V6[#zVzZ5S?E4<E?RzZ;E1R.?T5Y5Z#-X/[>3Y9[/S?5C2R(<R;C/E?Dv)B9_zV);)C5T1?O9_;Y=RzV4SzVzQ3Y;Y9^;[zD?E,^9R))R9C5Ev8B.._?NzS54X.>R<^4Rz^.zt(^.^9DzX<._?<E?RzZ;E1R.2V,RzV(P/R>._;Cv3YzE?V6-X([>)^.B;C3X4Dv3Cz_;DzG(X,R4.XzU?)B)T?G.^8[?.XzC2RzS?A?[5G7R4CzX<*E3T?<^"^4PzZ5Y5G5[3R)zd/T2(R;D5Y3Y=2V)6R>3YzC2RzG;D..XzP5A?E4Z?Y.3Y.R(A?Y.^5YtCz^)<V3EzC5)V#._;CzX4[#5Y?1Y5@4?O;Z*[?5QzVzC(B?<E?RzZ;E1R.?O3D.DzV4SzC2V.3DzC2Rzu6V9\zz;E1R.zc2V.3DzC5)V#zV4N5Y?9V4*E5S/T?;Y#C2^4PzV.;Y#.^7Rv;Y>;Y#X4RzT;YzG/E9_;D?;Y#C2^4PzV,V3[;U6RzV.;Y#.^7Rt')

#find_all_letters('<E?RzZ;E1R.>X?DzY5CzE?F/^(RzC2RzR"^)C?Y9RzX<9X7G?C3C3X42X-R,R(3CzS5R)(R+B3E?;<E;Z?@5E1._;CzV6[5@)4R-7V(\?CzR4C(V4C)z?Y9Rz^4._?6V9\zX<9X?E9^,RzU;E(^?E)zV4Sz^47V(\?C)-^._z[5@zR4C(NzT5D.3Cz^)=R4R(V6[#/Y>R(D.X5SzC2V.9X7G?C3C3X4<[5B(^)_?Dz^4;<E?RwZ;E1R.?Y,^(X4Z?Y.zN*^9V6[#zVzZ5S?E4<E?RzZ;E1R.?T5Y5Z#-X/[>3Y9[/S?5C2R(<R;C/E?Dv)B9_zV);)C5T1?O9_;Y=RzV4SzVzQ3Y;Y9^;[zD?E,^9R))R9C5Ev8B.._?NzS54X.>R<^4Rz^.zt(^.^9DzX<._?<E?RzZ;E1R.2V,RzV(P/R>._;Cv3YzE?V6-X([>)^.B;C3X4Dv3Cz_;DzG(X,R4.XzU?)B)T?G.^8[?.XzC2RzS?A?[5G7R4CzX<*E3T?<^"^4PzZ5Y5G5[3R)zd/T2(R;D5Y3Y=2V)6R>3YzC2RzG;D..XzP5A?E4Z?Y.3Y.R(A?Y.^5YtCz^)<V3EzC5)V#._;CzX4[#5Y?1Y5@4?O;Z*[?5QzVzC(B?<E?RzZ;E1R.?O3D.DzV4SzC2V.3DzC2Rzu6V9\zz;E1R.zc2V.3DzC5)V#zV4N5Y?9V4*E5S/T?;Y#C2^4PzV.;Y#.^7Rv;Y>;Y#X4RzT;YzG/E9_;D?;Y#C2^4PzV,V3[;U6RzV.;Y#.^7Rt')