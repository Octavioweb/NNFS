def vectordot(vectA, vectB):
    assert len(vectA)==len(vectB), f"both vectors must be same size. SizeA = {len(vectA)}, sizeB = {len(vectB)}"
    
    result = 0
    for i in range(len(vectA)):
        result += (vectA[i] * vectB[i])
    return result

def transpose(matrix):
    assert isinstance(matrix[0], list), "this is a vector, not a matrix"

    outMatrix = [[] for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            outMatrix[i].append(matrix[j][i])
        
    return outMatrix

def matrixDot(matrixA, matrixB):
    assert len(matrixA)==len(matrixB[0]), "sizes arent compatible, do you need to transpose something?"

    outMatrix = [[] for i in range(len(matrixA))]
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            tempMatrixB = [vector[i] for vector in matrixB]
            outMatrix[j].append(vectordot(matrixA[j], tempMatrixB))
    
    return outMatrix

def dot(matrixA, matrixB):
    #Matrix with matrix. One must be transposed
    if isinstance(matrixA[0], list) and isinstance(matrixB[0], list):
        if len(matrixA)!=len(matrixB[0]):
            matrixB = transpose(matrixB)
            assert len(matrixA)==len(matrixB[0]), f"sizes of matrix1: {len(matrixA)} and sizes of matrix2: {len(matrixB[0])} aren't compatible!"

        outMatrix = [[] for i in range(len(matrixA))]
        for i in range(len(matrixA)):
            for j in range(len(matrixB[0])):
                tempMatrixB = [vector[i] for vector in matrixB]
                outMatrix[j].append(vectordot(matrixA[j], tempMatrixB))

    #Simple vector multiplication
    if not isinstance(matrixA[0], list) and not isinstance(matrixB[0], list):
        return vectordot(matrixA, matrixB)
    
    #Vector with matrix
    if not isinstance(matrixA[0], list) and isinstance(matrixB[0], list):
        matrixA = [matrixA]
        

    #Matrix with vector (I don't think this is common)
    if isinstance(matrixA[0], list) and not isinstance(matrixB[0], list):
        matrixB = [matrixB]

    outMatrix = []
    for i in range(len(matrixB)):
        outMatrix.append(vectordot(matrixA[0], matrixB[i]))
        #Optional
        outMatrix[-1] = round(outMatrix[-1], 2)

    
    return outMatrix

def addBias(matrixA, biasVect):
    if not isinstance(matrixA[0], list):
        output = []
        for i in range(len(matrixA)):
            output.append(matrixA[i]+biasVect[i])
        return output

    output = [[] for n in matrixA]
    for i in range(len(matrixA)):
        for j in range(len(matrixA[0])):
            output[i].append(matrixA[i][j]+biasVect[j])

            

    return output    