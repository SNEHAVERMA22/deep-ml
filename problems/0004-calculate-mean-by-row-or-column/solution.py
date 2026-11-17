def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    result=[]

    if mode=="column":
        for j in range(len(matrix[0])):
            column=[]

            for i in range(len(matrix)):
                column.append(matrix[i][j])

            avg=sum(column)/len(column)
            result.append(avg)
           

    else:
        for row in matrix:
            avg=sum(row)/len(row)
            result.append(avg)



    return result