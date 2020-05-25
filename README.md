# modify_lammps_data
## Delete bonds, angles and dihedrals type  and arrange it to a new lammps data file, For example: At most you can delete 1 bond, 1 angle and 1 dihedral at a time. 

### Note1.   
You can delete only one combination of bond, angle or dihedral type at a time 

### Note2. 
Your input LAMMPS data should start from "Atom" Section, shown below

Example Input file shown below as well as provided in the main directory of this tool

1 1 3 0.000000 8.051000 -4.466000 -3.810000 #CS     
2 1 9 0.000000 7.372000 -4.735000 -3.027000 #HS          
3 1 9 0.000000 7.548000 -4.524000 -4.753000 #HS    


 Bonds

1 7 1 2       
2 7 1 3      
3 8 1 4        

 Angles     

1 15 2 1 3      
2 16 2 1 4    
3 8 2 1 5    
4 16 3 1 4     
   
 Dihedrals     
       
1 11 2 1 4 14    
2 11 2 1 4 18    
3 11 2 1 4 10     


### Note3. 
After building modified LAMMPS data, you need to see the total number of remaining bonds, angles and dihedrals, 
also if you deleted 2 types of bonds out of 8 types then remaining 6 bond types should be updated in the header section of LAMMPS 
Data file. 



