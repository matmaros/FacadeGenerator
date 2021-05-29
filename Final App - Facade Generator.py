import openpyxl
import copy

def make_body_rows_types(edge_types, center_types):
    '''generate 12 different body row types using defined edge and center window blocks'''
    
    body_row_types = []
    for edge in edge_types:
        for center in center_types:
            body_row_types.append([edge[0],center,edge[1]])

    return body_row_types

def body_block_generator(body_row_types, num_floors):
    '''copy each body_row_type by n number of floors to creat body blocks of n floors'''
    
    body_types = []
    for item in body_row_types:
        body_type = []
        for i in range(num_floors):
            body_type.append(item)
        body_types.append(body_type)

    return body_types    

def make_body_types(body_row_types, body_floors):
    '''using a list of floor numbers generate groups of building bodies with corresponding level of floors i.e.:
    a number '5' in the list will call the body_block_generator funcion to create a buiding of 5 floors for each
    body_row_type'''
    
    body_types = []
    for item in body_floors:
        #call block generator based on #floors in each body_floor
        body_types.append(body_block_generator(body_row_types, item))

    return body_types

def make_body_with_base(body_types, base_types):
    '''create copies of bodies and add a new group based on each base type'''

    body_with_base =[]
    for base in base_types:
        body_with_base.append(copy.deepcopy(body_types))

    #alter new list to include base types
    for i, body_types in enumerate(body_with_base):
        for group in body_types:
            for body in group:
                multi = len(''.join(body[0]))-2 #set multiplier for length of base, -1 to include | | edges
                body+=['|'+base_types[i]*multi+'|'] #OR USE BODY.APPEND()

    return body_with_base

def make_body_with_attic(body_with_base, attic_types):
    '''copy all bodies with bases and create new group for each attic type'''

    body_with_attic =[]
    for attic in attic_types:
        body_with_attic.append(copy.deepcopy(body_with_base))

    #alter new list to include base types
    for i, body_with_base in enumerate(body_with_attic):
        for body_types in body_with_base:
            for group in body_types:
                for body in group:
                    multi = len(''.join(body[0]))-2 #set multiplier for lenght of attic, -2 for | | edges 
                    body.insert(0,'|'+attic_types[i]*multi+'|')

    return body_with_attic

def make_excel(set):
    '''print all groups of the final attic set to check that set was formed correctly'''

    wb = openpyxl.Workbook()
    sheet = wb['Sheet']
    COL = 0

    for body_with_base in set:
        for body_types in body_with_base:
            for group in body_types:
                COL+=1     
                ROW = 0        
                for body in group:
                    body.extend(' ') # add blank row for spacing on excel sheet
                    for row in body:
                        ROW+=1
                        sheet.cell(row=ROW, column=COL).value = ''.join(row)
 
    wb.save('test.xlsx')

#region - INPUTS
# for types s = single window, d = double window, m = mirrored window, | = no window
window_edge_types = [['|=','=|'],['|= =','= =|'], ['|==','==|']]           
window_center_types = ['=', '= =', '==', ' ']
body_floors = [2,3,4]
base_types = ['|','_']
attic_types =[':','~']
#endregion

body_row_types = make_body_rows_types(window_edge_types, window_center_types)
body_types =make_body_types(body_row_types,body_floors)
body_with_base = make_body_with_base(body_types,base_types)
body_with_attic = make_body_with_attic(body_with_base,attic_types)

make_excel(body_with_attic)

