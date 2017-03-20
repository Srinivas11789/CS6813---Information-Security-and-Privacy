import re

def main():
    print "This Program Extracts the Plain Text Passwords from the Yahoo DB\n"
    print "Pattern : Yahoo: Plaintext , extract the plain text password from the file ! \n"
    print "Input Format --> user_id   :  user_name  : clear_passwd : passwd\n\n"
    print "Output Format --> Username Password"

    fd = open("/Users/darkknight/Desktop/Password Cracking/PasswordDumps/Password List/Yahoo.txt","r")
    data  = fd.readlines()
    fd.close()

    fd = open("/Users/darkknight/Desktop/Password Cracking/PasswordDumps/Yahoo_Extract.txt","w")
    for line in data:
          extract = re.search('^[0-9]+:(.*):(.*)$', line)
          if extract:
            if extract.group(1):
                if extract.group(2):
                    fd.write("%s %s\n" % (extract.group(1),extract.group(2)))
            else:
                print ("\tFAIL: No Pattern Match for Username:Password")
    fd.close()

main()
