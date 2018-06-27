
""" 
ROHIT MALYALA JUNE 2018

Brief description of this tool: Outputs a DNA sequence, visual, and relevant parameters 
for the desired ssDNA-TAL origami nanostructure.
   
Future tasks:    
Later on, we will need to add the option to perform these operations in reverse. What this means is that we will need to allow a user to input proteinDistance, dihedralAngle, and arcDepth. Then the program will output two appropriate TAL distances. The dihedral must also be associated somehow with a "likelihood of monomerization problems." And of course, it must also output a DNA sequence!

After this basic functionality is added, our next steps are to do a few different things.
1) It is absolutely vital that this functionality be extended to three or four tal monomers, AT THE VERY LEAST.
   It is a joke of a program if we leave it at this.
2) More complex shapes are less important but still would be absolutely excellent!!
3) An output to a .blend file is pretty much vital
4) Finally, ALL OF THE WORK DONE HERE WITH THIS PROGRAM MUST BE VALIDATED EMPIRICALLY.
    
Have fun!    
"""


"""
Background from the Praetorius thing,
why its needed,
how you did it,
what was done

FUTURE DIRECTIONS
"""

"""
INITIALIZATION
--------------

In the future, initialization must provide the following options
First option:  "What TAL structure primitive would you like to make? Two-TAL monomer, Three-TAL monomer
                square, triangle, etc." At least four or five options would be nice.
Second option: "What style of inputs would you like to provide? Do you want to manually input base pair distances
                to get an output? Or do you want to dictate a enzyme-distance, structure angle, dihedral angle etc, 
                and then get your sequence from there? --- the two options are "a priori" and "a posteriori".
                
For now, however, initialization is just the title sequence.                
"""

import random

while True:

print("DNA ORIGAMI TWO-TAL SEQUENCE STRUCTURE")

"""
Below is the option to include two distances. The upper distance1 refers to the base pair gap between the two double
TALs' n-terminal single-TAL. The lower distance2 refers to the base pair gap between the two c-terminal single TALs.
"""

distanceNtal_1 = int(input("Input base pair distance between N-terminal TAL 1 and N-terminal TAL 2:"))
distanceNtal_2 = int(input("Input base pair distance between N-terminal TAL 2 and N-terminal TAL 3:"))
distanceCtal_1 = int(input("Input base pair distance between C-terminal TAL 1 and C-terminal TAL 2:"))
distanceCtal_2 = int(input("Input base pair distance between C-terminal TAL 2 and C-terminal TAL 3:"))

"""
Below is the number crunching to get the estimated distance between your two enzymes mounted on the N-terminus
of each of the N-terminal single-TALs. The distance is provided with respect to base pairs, and with respect to an actual nanometre distance. Protein angle distance takes into account the chord created by the line bisecting the protein mounting sites on arched nanostructures. Arched nanostructures are created when there is a difference between distance1 and distance2.

According to the Dietz lab, 10bp = 3.4nm = 1 turn of the helix. 
According to wikipedia, 1.0bp is 3.4 angstroms, or 340pm of length along the strand.
These are equivalent statements.
"""

proteinDistance_1_2 = 21+distanceNtal_1
proteinDistance_2_3 = 21+distanceNtal_2
proteinLinearDistance_1_2 = proteinDistance_1_2*0.34
proteinLinearDistance_2_3 = proteinDistance_2_3*0.34

proteinAngleDOC = (proteinLinearDistance_1_2 + proteinLinearDistance_1_2)/distanceNtal_1

print("\n")
print("The distance between your mounted proteins, assuming both are chimerized to the n-terminal of each double-TAL:") 
print("linear protein distance, bp")
print(proteinDistance_1_2)
print("linear protein distance, nm")
print(proteinLinearDistance_1_2)
print("angled protein distance, nm")
print(proteinAngleDOC)
print("\n")

"""
The following is the dihedral angle. It is a description of how far-away the enzymes are in an angular sense. 
The monomeric TAL structure is fundamentally a line.
"""

dihedralAngle_1_2 = ((proteinLinearDistance_1_2)%10*180)%360
dihedralAngle_2_3 = ((proteinLinearDistance_2_3)%10*180)%360

print("The estimated dihedral angle between your mounted enzymes along the axis of the DNA sequence where the TALs are mounted is provided below. This estimate becomes less meaningful the greater inter-enzyme distance is.")
print("\n")
print("Dihedral between TAL 1 and TAL 2 in degrees")
print(dihedralAngle_1_2)
print("Dihedral between TAL 2 and TAL 3 in degrees")
print(dihedralAngle_2_3)
print("\n")


gapSequence_N_1_2 = (''.join(random.choice("ATCG") for i in range(distanceNtal_1))) 
gapSequence_N_2_3 = (''.join(random.choice("ATCG") for i in range(distanceNtal_2))) 
gapSequence_C_3_2 = (''.join(random.choice("ATCG") for i in range(distanceCtal_2))) 
gapSequence_C_2_1 = (''.join(random.choice("ATCG") for i in range(distanceCtal_1))) 

"""
The following is the calculation to get the degree of curvature.
>>The degree of curvature in the arc is calculated from the differential in bp length
>>If there is no differential, there is no arc. The monomer is linear
>>The degree of curvature is provided here actually as a radius.
>>If the radius is small, the degree of curve is high.
>>If the radius is very large or infinite, the structure is probably linear.
>>You can see here why a visual is so important!!

>>It is calculated by taking the difference between the bp gap lengths and then doing some mild trigonometry to calculate the degree of the curvature
>>A 21bp differential assuming a 6nm gap between DNA lines is a 67 degree curve.
"""



"""
The last output is the DNA sequence.
tCTGCTCGACGTAACTGACGTATACTGTGACCCGTCCGTTATAACATGAaGTTGCGCAGTTACtCCGGTGAATCCACATTTACCATTCCTATACTAGAATGCTCGCGTATTGaTGGACATAGATAGtCCGGTCCGTGTTAGCGATGCGGAAAAAGTCGCCAATGAGCCACTTGTAaCACAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCTTACCAGTACATGTATAACTaCTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATTTCGAGATCAATCGATAGTAaGACCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACTTCGAGATCTATGAATTATGaACAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGGCTGGACCGCGGCGCTTAATaCCCAGTGGCTCATtCAATATCGATTCATCTGAATCACCCGATAGGTATTAGAGGTGCGCTGTaGGCTTGATAGTTAtCATCAGCGGATCATCTCGATCGAGACAAAGATCGCACAAATTATCACGaAACTCCACAAGAAtAGCTAGTATTTCATCCAATAGGTCGTTGGATACTATCGGTACTACTGAaGCCTAAGCCGACAtTGTCACTCACTAATGCAGGCGCCAGCACACTCTATCCAGGATGGAAGAaACTTTTTGAAGTCtTTACAGTGATAAAATCTTACAGTGGGGCAATGTAATCAGCGCTCTTGGaCCAAATAACGAAAtCGTGAACCGACAACTCTTGA
"""





print("TAL(#8) tCTGCTCGACGTAACTGACGT" + " | " + gapSequence_N_1_2 + " | " + "tCCGGTGAATCCACATTTACC" + " | " + gapSequence_N_2_3 + " | " + "tCCGGTCCGTGTTAGCGATGC" + " | " + "GGAAAAAGTCGCCAATGAGCCACTTGTAaCACAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCTTACCAGTACATGTATAACTaCTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATTTCGAGATCAATCGATAGTAaGACCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACTTCGAGATCTATGAATTATGaACAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTGTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGGCTGGACCGCGGCGCTTAATaCCCAGTGGCTCATtCAATATCGATTCATCTGAATCACCCGATAGGTATTAGAGGTGCGCTGTaGGCTTGATAGTTAtCATCAGCGGATCATCTCGATCGAGACAAAGATCGCACAAATTATCACGaAACTCCACAAGAAtAGCTAGTATTTCATCCAATAGGTCGTTGGATACTATCGGTACTACTGAaGCCTAAGCCGACAtTGTCACTCACTAATGCAGGCGCCAGCACACTCTATCCAGGATGGAAGAaACTTTTTGAAGTCtTTACAGTGATAAAATCTTAC"  + " | " + gapSequence_C_3_2 + " | "  "AGTGGGGCAATGTAATCAGCGCTCTTGGaCCAAATAACGAAA" + " | " + gapSequence_C_2_1 + " | " + "TAL(#8) tCGTGAACCGACAACTCTTGA")
        
 try_again = int(input("Press 1 to try again, 0 to exit"))
 if try_again == 0:
     break
