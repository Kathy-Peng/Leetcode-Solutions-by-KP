class Solution(object):
               
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(board)
        col = len(board[0])
        flag = True
        #tag horizontal candies
        for i in range(row):
            for j in range(col-2):
                nums1 = abs(board[i][j])
                nums2 = abs(board[i][j+1])
                nums3 = abs(board[i][j+2])
                if nums1 == nums2 and nums2==nums3 and nums1 !=0:
                    board[i][j]= -nums1
                    board[i][j+1]= -nums2
                    board[i][j+2]= -nums3
                    flag = False
        #tag vertical candies
        for j in range(col):
            for i in range(row-2):
                nums1 = abs(board[i][j])
                nums2 = abs(board[i+1][j])
                nums3 = abs(board[i+2][j])
                if nums1 == nums2 and nums2 ==nums3 and nums1 !=0:
                    board[i][j]=-nums1
                    board[i+1][j]=-nums2
                    board[i+2][j]=-nums3
                    flag = False
        if not flag: 
        #make crash candies disappear and let the above candies fall down
            for j in range(col):
                ptr = row - 1
                for i in range(row-1, -1, -1):
                    if board[i][j]>0:
                        board[ptr][j]=board[i][j]
                        ptr -= 1
                #fill the top rows with 0s
                for k in range(ptr, -1, -1):
                    board[k][j]=0
        return board if flag else self.candyCrush(board)  