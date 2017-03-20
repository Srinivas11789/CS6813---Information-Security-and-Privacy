import re

def main():
    print "This Program Extracts the Hashes from the DB\n - XSplit"

    fd = open("/Users/darkknight/Desktop/Password Cracking/PasswordDumps/xsplit_leak.txt","r")
    data  = fd.readlines()
    fd.close()
    fd = open("/Users/darkknight/Desktop/Password Cracking/PasswordDumps/XSplit_Extract.txt","w")

    for line in data:
          #print line.strip()
          #extract = re.search('^.*(\.).*\s([a-zA-Z0-9]*)', line)
          #extract = re.search('^.*\s.*\s.*\s([a-zA-Z0-9]*)', line)
          extract = re.search('.*\s+(.*)$', line.strip())
          try:
              print extract.group(1)
         #  if extract.group(1):
              if extract.group(1):
                  print "Hi"
                  print extract.group(1)
                  #fd.write("%s - %s\n" % (extract.group(1),extract.group(2)))
                  fd.write("%s\n" % (extract.group(1)))

          except:
                print ("\tFAIL: Hash Not Found")
                print line
    fd.close()

main()