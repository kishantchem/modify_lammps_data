
###import numpy as np
import re

##f = open("lmp-data-8-etgly-mcm.txt", "r")
##for files in filepath:

bondtype = input("Please enter a bondtype to delete: if nothing to do then enter 0\n")
bondtype = int(bondtype)

angletype = input("Please enter a angletype to delete:if nothing to do then enter 0\n")
angletype = int(angletype)

dihedraltype = input("Please enter a dihedraltype to delete:if nothing to do then enter 0\n")
dihedraltype = int(dihedraltype)

ifn = input("Please enter input file name of LAMMPS data, for example input.dat 0\n")
ifn = string(ifn)

ofn = input("Please enter output file name of modified LAMMPS data, for example output.dat 0\n")
ofn = string(ofn)
  
#ifn='deleted-cl-cl-dihedral-6-7.dat'
#ofn='deleted-cl-cl-dihedral-6-7-8.dat'
############################ Reading bond section ##############################
string = ' Bonds'
with open('%s' % ofn, 'w') as outlmp:
    with open('%s' % ifn) as inputheader:
        for line in inputheader:
            outlmp.write(line)
            if string in line:
               break

with open('%s' % ofn, 'a') as outlmp:
 count= 0
 with open('%s' % ifn) as inputbond:
    outlmp.write('\n')
#    outlmp.write(" Bonds")
#    outlmp.write('\n\n')
    for line in inputbond:
          x= re.findall("\s",line)
          if len(x) == 4:
              b=line.split(" ")
      ###  print(b[1])
              if int(b[1]) != bondtype and int(b[1]) > bondtype and bondtype > 0:
       ## print(b)
                count = count + 1
                b[0]= count
                b[1] = int(b[1]) - 1
       ## print(b[1])
                listtostr = ' '.join([str(nitw) for nitw in b])
       ## print(listtostr)
                outlmp.write(listtostr)
              if int(b[1]) < bondtype:
       ### print(b)
                 count = count + 1
                 b[0] = count
                 listtostr = ' '.join([str(nitw) for nitw in b])
                 outlmp.write(listtostr)
              if bondtype == 0:
                 listtostr = ' '.join([str(nitw) for nitw in b])
                 outlmp.write(listtostr)

    

#    print(b)
                  
#    print(x)
###print(b[1])
##print(line[0])
with open('%s' % ofn, 'a') as outlmp:
####################### Reading angle section ########################
 with open('%s' % ifn) as inputangle:
        outlmp.write('\n')
        outlmp.write(" Angles")
        outlmp.write('\n\n')
        count= 0
        for line in inputangle:
            x= re.findall("\s",line)
            if len(x) == 5:
                b=line.split(" ")
      ##       print(b[1])
                if int(b[1]) != angletype and int(b[1]) > angletype and angletype > 0:
               ## print(b)
                    count = count + 1
                    b[0]= count
                    b[1] = int(b[1]) - 1
               ## print(b[1])
                    listtostr = ' '.join([str(nitw) for nitw in b])
               ## print(listtostr)
                    outlmp.write(listtostr)
                if int(b[1]) < angletype:
               ### print(b)
                    count = count + 1
                    b[0] = count
                    listtostr = ' '.join([str(nitw) for nitw in b])
                    outlmp.write(listtostr)
                if angletype == 0:
                    listtostr = ' '.join([str(nitw) for nitw in b])
                    outlmp.write(listtostr)

           ##  else:
             ##    listtostr = ' '.join([str(elem) for elem in b])
               ##  outbond.write(listtostr)
with open('%s' % ofn, 'a') as outlmp:
##################### Reading dihedral section #####################
 with open('%s' % ifn) as inputdihedral:
        outlmp.write('\n')
        outlmp.write(" Dihedrals")
        outlmp.write('\n\n')
        count= 0
        for line in inputdihedral:
            x= re.findall("\s",line)
            if len(x) == 6:
               b=line.split(" ")
      ##       print(b[1])
               if int(b[1]) != dihedraltype and int(b[1]) > dihedraltype and dihedraltype > 0:
               ## print(b)
                count = count + 1
                b[0]= count
                b[1] = int(b[1]) - 1
               ## print(b[1])
                listtostr = ' '.join([str(nitw) for nitw in b])
               ## print(listtostr)
                outlmp.write(listtostr)
               if int(b[1]) < dihedraltype:
               ### print(b)
                count = count + 1
                b[0] = count
                listtostr = ' '.join([str(nitw) for nitw in b])
                outlmp.write(listtostr)
               if dihedraltype == 0:
                 listtostr = ' '.join([str(nitw) for nitw in b])
                 outlmp.write(listtostr)

             ##  else:
             ##    listtostr = ' '.join([str(elem) for elem in b])
             ##    outbond.write(listtostr)


