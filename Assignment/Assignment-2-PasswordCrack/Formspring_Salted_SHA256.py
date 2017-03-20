import hashlib,sys
def main():
    print " Formspring Password Hashing Crack"
    print """ Formspring Hashes - SHA256 with 2 Digit Salt - SHA256(salt+Password)"""

    # PASSWORD HASH FILE READ
    fd = open("/home/srinivas/Desktop/PasswordCrack/formspring.txt", "r")
    hashes = fd.readlines()
    fd.close()

    # DICTIONARY FILE READ
    fd = open("/home/srinivas/Desktop/PasswordCrack/rockyou.txt", "r")
    data = fd.readlines()
    fd.close()

    # SALT FILE CREATION AND UPDATE OF 2 DIGIT SALT
    fd = open("/home/srinivas/Desktop/PasswordCrack/salt.txt", "a")
    fd.write('00\n')
    fd.write('01\n')
    fd.write('02\n')
    fd.write('03\n')
    fd.write('04\n')
    fd.write('05\n')
    fd.write('06\n')
    fd.write('07\n')
    fd.write('08\n')
    fd.write('09\n')
    for i in range(10,100):
        i = str(i) + "\n"
        fd.write(i)
    fd.close()

    # SALT FILE READ
    fd = open("/home/srinivas/Desktop/PasswordCrack/salt.txt", "r")
    salt = fd.readlines()
    fd.close()
    count = 0

    # ANSWER FILE OPEN TO SAVE THE ANSWERS IN THE FORMAT - HASH PASSWORD
    ans = open("/home/srinivas/Desktop/PasswordCrack/answers.txt", "a")

    #ITERATING THROUGH THE HASH, WORDLIST AND THE SALTS - CONCATENATED
    try:
     for hash in hashes:
        for dic in data:
            #SALT CODE
            for s in salt:
              #print s.strip('\r\n') + dic.strip('\r\n')
              sh = s.strip() + dic.strip()
              h = hashlib.sha256(sh).hexdigest()
              if h == hash.strip('\r\n'):
                print "Password Hit for %s\n" % (sh)
                ans.write(dic)
                count = count + 1

    except:
       print "Test Done !!! Count = %d" % (count)
    print "Test Done !!! Count = %d" % (count)

main()