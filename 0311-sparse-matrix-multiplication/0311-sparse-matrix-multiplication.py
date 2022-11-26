class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        print(k,n)
        result = [[0 for i in range(n)] for j in range(m)] 
        hash_mat1 = {}
        hash_mat2 = {}
        for i in range(m):
            for j in range(k):
                if mat1[i][j]!=0:
                    hash_mat1[(i,j)]=mat1[i][j]
        for i in range(k):
            for j in range(n):
                print(i,j)
                if mat2[i][j]!=0:
                    print(mat2[i][j])
                    hash_mat2[(i,j)]=mat2[i][j]       
        for i in range(m):
            for j in range(n):
                dot_product = []
                for x in range(k):
                    if (i,x) in hash_mat1 and (x,j) in hash_mat2:
                        dot_product.append(hash_mat1[(i,x)] * hash_mat2[(x,j)])
                    else:
                        dot_product.append(0)
                result[i][j] = sum(dot_product)
        return result
                
                
                