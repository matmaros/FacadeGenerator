# Facade Generator

A recursive algorithm to arrange various facade elements into a series of building elevations.  

![image](https://user-images.githubusercontent.com/67350711/120078372-42da9b80-c07d-11eb-9bf0-3bb63c9516b2.png)

---
### Requirements:
Python Modules:
*  openpyxl
*  copy
Optional:
* CAD program (Rhino3d, Autocad) for 'rendered' elevations

---
### Background:
The Facade Generator combines a series of hypothetical building facade elements and uses a recursive algorithm to combine all combinations into distinct building facades.  The three major facade blocks are the base, the body, and the attic.  

1.  For the base there are two options represented in the algorithm.
  * Type 1 is verticals lines:  |||||
  * Type 2 is a continuous base: _______ 
2.  The main body is based on the number of floors (2-4) and an arrangement of window types.  Three window types are used.
  * Single window type: =
  * Double window type: = = 
  * Mirrored window type: ==

  These window types are joined as edge/center/edge combinations to form 12 possible arrangements, each representing the window expression for a single floor.  These are shown below represented as 'rendered' building rows.
  
  ![image](https://user-images.githubusercontent.com/67350711/120078645-6eaa5100-c07e-11eb-92b5-e0e132096e0a.png)
  
3.  Lastly there are two attic types.
  * Type 1 as a 'double cornice"- : : : : :
  * Type 2 as a squigle cornice: ~ ~ ~ ~ 

The python file attached combines these different blocks and produces all possible outcomes.  A simple L systems combines all blocks and produces an excel sheet as a graphical representation of the result.  The logic can be used with CAD blocks substituted in place of the simple text representationsn of the building components.  This will produce a higher quality graphic more like a typical building elevation as shown in the project description above.

The python file attached combines these different blocks and produces all possible outcomes.  A simple L systems combines all blocks and produces an excel sheet as a graphical representation of the result as shown in the 'Example Output' file and the image below.  

![image](https://user-images.githubusercontent.com/67350711/120079150-9d292b80-c080-11eb-85fb-b7de91ac1f30.png)

Zoomed region:

![image](https://user-images.githubusercontent.com/67350711/120079183-c2b63500-c080-11eb-81ba-75280fa4b680.png)

The logic can be used with CAD blocks substituted in place of the simple text representationsn of the building components.  This will produce a higher quality graphic more like a typical building elevation as shown in the example output image above.




