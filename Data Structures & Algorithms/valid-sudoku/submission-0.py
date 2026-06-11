class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(10)]
        cols = [set() for _ in range(10)]
        subBox = [set() for _ in range(10)]

        for rowIndex, row in enumerate(board):
            for colIndex, value in enumerate(row):
                if value == ".":
                    continue
                
                #Checking rows
                if value in rows[rowIndex]:
                    return False
                else:
                    rows[rowIndex].add(value)


                #checking cols
                if value in cols[colIndex]:
                    return False
                else:
                    cols[colIndex].add(value)


                #checking Subbox
                a = (rowIndex // 3) * 3               
                b = colIndex // 3 
                subBoxIndex = a + b

                if value in subBox[subBoxIndex]:
                    return False
                else:
                    subBox[subBoxIndex].add(value)


        return True
