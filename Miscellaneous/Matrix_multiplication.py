from datetime import datetime, date
import numpy as np

if __name__ == "__main__":
    matrix1 = np.random.randint(50, size=(100, 100))
    matrix2 = np.random.randint(50, size=(100, 100))

    print("MATRIX 1 : ")
    print(matrix1)
    print("MATRIX 2 : ")
    print(matrix2)

    result = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))] 

    inital = datetime.utcnow()
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    final = datetime.utcnow()

    inital1 = datetime.utcnow()
    result = np.dot(matrix1,matrix2)
    final1 = datetime.utcnow()
    print("RESULT AFTER MULTIPLICATION:")
    print(result)
    total_time = ((final - inital).total_seconds())
    print("Total time taken when using FOR LOOPS:", total_time, "seconds")
    total_time1 = ((final1 - inital1).total_seconds())
    print("Total time taken when using np.dot:", total_time1, "seconds")