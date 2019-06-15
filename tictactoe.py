mat=[]
for i in range(3):
    mat.append([])
for i in range(3):
    for j in range(3):
        mat[i].append(j)
        # Initialising all positions of matrix to underscore
        mat[i][j]="_"

for i in range(9):
    if i%2==0:
        print("Player 1:")
        print("Enter the row and column where you want to insert X")
        r=int(input())
        c=int(input())
        mat[r-1][c-1] = "X" 
    
# Printing the matrix after every turn of each player
        for p in range(3):
            for q in range(3):
                print(mat[p][q], end=" ")
            print()
    else:
        print("Player 2:")
        print("Enter the row and column where you want to insert 0")
        r = int(input())
        c = int(input())
        mat[r-1][c-1] = "0"

# Printing the matrix after every turn of each player        
        for p in range(3):
            for q in range(3):
                print(mat[p][q], end=" ")
            print()
            
# Checking row wise elements
    for a in range(3):
        b=0
        if mat[a][b]=="X" and mat[a][b+1]=="X" and mat[a][b+2]=="X":
            print("Player 1 wins!")
            exit()
        elif mat[a][b]=="0" and mat[a][b+1]=="0" and mat[a][b+2]=="0":
            print("Player 2 wins!")
            exit()

# Checking column wise elements            
    for a in range(3):
        b=0
        if mat[b][a]=="X" and mat[b+1][a]=="X" and mat[b+2][a]=="X":
            print("Player 1 wins!")
            exit()
        elif mat[b][a]=="0" and mat[b+1][a]=="0" and mat[b+2][a]=="0":
            print("Player 2 wins!")
            exit()
            
# Checking the diagonal elements
    if mat[0][0]=="X" and mat[1][1]=="X" and mat[2][2]=="X":
        print("Player 1 wins!")
        exit()
    elif mat[0][2]=="X" and mat[1][1]=="X" and mat[2][0]=="X":
        print("Player 1 wins!")
        exit()
    elif mat[0][0]=="0" and mat[1][1]=="0" and mat[2][2]=="0":
        print("Player 2 wins!")
        exit()
    elif mat[0][2]=="0" and mat[1][1]=="0" and mat[2][0]=="0":
        print("Player 2 wins!")
        exit()

print("Its a draw!")

