DOT = "."
NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
DIRECTIONS = {"NW":(-1,-1), "N":(-1,0), "NE":(-1,1), "E":(0,1), "SE":(1,1), "S":(1,0), "SW":(1,-1), "W":(0,-1)}

input_list:[str] = []
number_list:[str] = []

# Purpose: finds the engine schematic; main driver
# Parameters: None
# Returns: None
def findEngineSchematic() -> None:
    # open input file
    with open("sample_input.txt") as input_file:
        # create input lise
        for row in input_file:
            input_list.append(row)
        
        # iterate over input_list
        for row in range(0, len(input_list)):
            for col in range(0, len(input_list[1])): 
                # if a symbol is present add the number to list
                sym_cord = searchSymbolSpace(row=row, col=col, input_list=input_list)
                if sym_cord != (-1,-1):
                    # pre-append number to be added to list
                    findNumber(sym_r=sym_cord[0], sym_c=sym_cord[1], input_list=input_list)
    total:int = 0
    print(number_list)
    for num in number_list:
        total += int(num)
    print(total)

                    

def isInBounds(row:int ,col:int, r_max:int, c_max:int) -> bool:
    if row >= 0 and row < r_max and col >= 0 and col < c_max:
        return True
    return False

def searchSymbolSpace(row:int, col: int, input_list:list[str]) -> (int, int):
    row_max = len(input_list)
    col_max = len(input_list[1]) - 1
    for direction in DIRECTIONS.keys():
        new_r = row + DIRECTIONS[direction][0]
        new_c = col + DIRECTIONS[direction][1]
        if isInBounds(row=new_r, col=new_c, r_max=row_max, c_max=col_max):    
            if input_list[new_r][new_c] == DOT or input_list[new_r][new_c] in NUMBERS:
                return (-1,-1)
            else:
                return (new_r, new_c)

def findNumber(sym_r:int, sym_c:int, input_list:list[str]) -> None:
    row_max = len(input_list)
    col_max = len(input_list[0]) - 1
    num_str: str = ""
    for direction in DIRECTIONS.keys():
        num_r = sym_r + DIRECTIONS[direction][0]
        num_c = sym_c + DIRECTIONS[direction][1]
        if isInBounds(row=num_r, col=num_c, r_max=row_max, c_max=col_max):
            if input_list[num_r][num_c] in NUMBERS:
                for i in range(-2,3):
                    if isInBounds(row=num_r, col=num_c+i, r_max=row_max, c_max=col_max): 
                        if input_list[num_r][num_c+i] in NUMBERS:
                            num_str += input_list[num_r][num_c+i]
                        else:
                            if num_str != "":
                                print(num_str)                            
            if num_str != "":
                number_list.append(num_str)
            num_str = ""
            continue        
                    

# run driver here
findEngineSchematic()