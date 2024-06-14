class Matrix:
    def __init__(self, m_list: list[list[int]]) -> None:
        self.matrix = m_list
        self.n = len(m_list)
    
    def is_valid(self) -> bool:
        #no input = not valid matrix
        if self.n == 0:
            return False
        # if matrix is either [x] or [[x,y,z]] need to check
        if self.n == 1:
            if isinstance(self.matrix[0], int):
                return True
        
        for row in self.matrix:
            if len(row) != self.n:
                return False
    
        return True
    
    def find_2x2(self, i: int, j: int) -> list:
        tbyt = []
        for x in range(self.n):
            temp = []
            for y in range(self.n):
                if x != i and y != j:
                    temp.append(self.matrix[x][y])
            if temp:
                tbyt.append(temp)
        
        return tbyt

    def find_cofactors(self) -> list:
        cof = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                curr_2x2 = self.find_2x2(i,j)
    
                val = (curr_2x2[0][0]*curr_2x2[1][1]) - (curr_2x2[0][1] * curr_2x2[1][0])
                if (i+j)%2 != 0:
                    val = 0 - val
                row.append(val)

            cof.append(row)
        return cof
    
    def find_transpose(self, cof: list) -> list:
        trans = []
        for _ in range(self.n):
            trans.append([])

        for row in cof:
            for i in range(self.n):
                trans[i].append(row[i])
        return trans
        
    
    def adjoint(self) -> list:
        m = self.find_transpose(self.find_cofactors())
        return m



m = Matrix([[2,4,55],[3,-54,54],[53,97,6]])

n = m.adjoint()

print(n[0])
print(n[1])
print(n[2])