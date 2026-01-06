class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_unit(unit):
            nums = [x for x in unit if x != "."]
            return len(nums) == len(set(nums))
        
        for i in board:
            if not valid_unit(i):
                return False
        
        for i in range(9):
            col = [board[r][i] for r in range(9)]
            if not valid_unit(col):
                return False
        
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                square = [
                    board[r][c]
                    for r in range(br, br + 3)
                    for c in range(bc, bc + 3)
                ]
                if not valid_unit(square):
                    return False
        
        return True



