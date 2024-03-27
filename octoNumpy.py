def dot(vectA, vectB):
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

def vectorMatrixDot(vetor, matrix):
    outMatrix = []
    for i in range(len(matrix)):
        outMatrix.append(dot(vetor, matrix[i]))
        #Optional
        outMatrix[-1] = round(outMatrix[-1], 2)
    
    return outMatrix

def matrixMatrixDot(matrixA, matrixB):
    assert len(matrixA)==len(matrixB[0]), "sizes arent compatible, do you need to transpose something?"

    outMatrix = [[] for i in range(len(matrixA))]
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            tempMatrixB = [vector[i] for vector in matrixB]
            outMatrix[j].append(dot(matrixA[j], tempMatrixB))
    
    return outMatrix

def matrixAddBias(matrixA, biasVect):

    output = [[] for n in matrixA]
    for i in range(len(matrixA)):
        for j in range(len(matrixA[0])):
            output[i].append(matrixA[i][j]+biasVect[j])
            output[i][-1] = round(output[i][-1], 3)

    return output

def vectorAddBias(vector, biasVect):
    output = []
    for i in range(len(vector)):
        output.append(vector[i]+biasVect[i])
        output[-1] = round(output[-1], 3)

    return output    