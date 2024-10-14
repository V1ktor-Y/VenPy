from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn2
from  matplotlib_venn.layout.venn2 import DefaultLayoutAlgorithm as DLA2
from  matplotlib_venn.layout.venn3 import DefaultLayoutAlgorithm as DLA3

def getNumberOfSets() -> int:
    num = int(input("How many sets would you like? (2 or 3): "))
    if num > 3 or num < 2:
        return getNumberOfSets()
    else:
        return num

numberOfSets = getNumberOfSets()

label1 = input("Enter first set name: ")
label2 = input("Enter second set name: ")
if numberOfSets ==3:
    label3 = input("Enter third set name: ")
    
set1 = set(input("Enter first set elements (seperated by a space): ").split())
set2 = set(input("Enter second set elements (seperated by a space): ").split())
if numberOfSets == 3:
    set3 = set(input("Enter third set elements (seperated by a space): ").split())

if numberOfSets == 2:
    venn2((set1 - set2,set2 - set1,set1 & set2), set_labels=(label1,label2),layout_algorithm=DLA2(fixed_subset_sizes=(1,1,1)))
elif numberOfSets == 3:
    venn3(((set1 - set2) - set3, (set2 - set1) - set3, (set1 & set2) - set3, (set3 - set1) - set2, (set3 & set1) - set2, (set3 & set2) - set1, (set1 & set2) & set3),set_labels=(label1,label2,label3) ,layout_algorithm=DLA3(fixed_subset_sizes=(1,1,1,1,1,1,1)))
    
plt.show()