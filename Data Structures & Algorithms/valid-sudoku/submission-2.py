class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                curr = board[i][j]

                if curr in rows[i] or curr in cols[j]:
                    return False

                if curr != ".":
                    rows[i].add(curr)
                    cols[j].add(curr)

            for i in range(0, len(board), 3):
                for j in range(0, len(board), 3):
                    visited_set = set()
                    for k in range(i, i + 3, 1):
                        for l in range(j, j + 3, 1):
                            if board[k][l] in visited_set:
                                print(visited_set)
                                print("i " + str(i))
                                print("j " + str(j))
                                print("k " + str(k))
                                print("l " + str(l))
                                return False
                            if board[k][l] != ".":
                                visited_set.add(board[k][l])

        return True



    
        