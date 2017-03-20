import hashlib,sys
def main():
    print " SHA1 Password Hashing Crack"
    print " Linkedin: Hash Type - SHA1 - SHA1(Password)"

    # READ THE PASSWORD HASH FILE
    fd = open("/home/srinivas/Desktop/PasswordCrack/Password List/Linkedin.txt", "r")
    hashes = fd.readlines()
    fd.close()

    # READ THE DICTIONARY FILE
    fd = open("/home/srinivas/Desktop/PasswordCrack/rockyou.txt", "r")
    data = fd.readlines()
    fd.close()
    count = 0

    # HANDLE FOR RECORDING THE ANSWERS IN THE FORMAT - HASH PASSWORD
    ans = open("/home/srinivas/Desktop/PasswordCrack/answers.txt", "a")

    # ITERATING THROUGH THE HASHES , WORDLIST WITH SHA1 DIGEST
    try:
     for hash in hashes:
        for dic in data:
            h = hashlib.sha1(dic.strip('\r\n')).hexdigest()
            if h == hash.strip('\r\n'):
                print "Password Hit for %s\n" % (dic)
                ans.write("%s %s\n" % (hash.strip(),dic.strip()))
                count = count + 1

    except:
       print "Test Done !!! Count = %d" % (count)
    print "Test Done !!! Count = %d" % (count)

main()