DOT = "."
NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
DIRECTIONS = {"NW":(-1,-1), "N":(-1,0), "NE":(-1,1), "E":(0,1), "SE":(1,1), "S":(1,0), "SW":(1,-1), "W":(0,-1)}

input_list = []

# Purpose: finds the engine schematic; main driver
# Parameters: None
# Returns: None
def findEngineSchematic() -> None:
    # open input file
    with open("day3_input.txt") as input_file:
        # create input lise
        for row in input_file:
            input_list.append(row)
        
        # iterate over input_list
        for row in range(0, len(input_list)):
            for col in range(0, len(input_list[0]) - 1): 
                # if a symbol is present add the number to list
                if searchSymbolSpace(row=row, col=col, input_list=input_list):
                    pass
                    # add number to list

def isInBounds(row:int ,col:int, r_max:int, c_max:int) -> bool:
    if row >= 0 and row < r_max and col >= 0 and col < c_max:
        return True
    return False

# 
def searchSymbolSpace(row:int, col: int, input_list:list[str]) -> bool:
    row_max = len(input_list)
    col_max = len(input_list[0]) - 1
    for direction in DIRECTIONS.keys():
        new_r = row + DIRECTIONS[direction][0]
        new_c = col + DIRECTIONS[direction][1]
        if isInBounds(row=new_r, col=new_c, r_max=row_max, c_max=col_max):    
            if input_list[new_r][new_c] == DOT or input_list[new_r][new_c] in NUMBERS:
                return False
            else:
                print("found symbol at: ",new_r,",",new_c)
                return True

# run driver here
findEngineSchematic()