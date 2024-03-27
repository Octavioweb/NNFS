def dot(tensor1, tensor2):
    # print(tensor1, tensor2)
    # We only consider matrix*matrix 
    # vector*matrix
    # vector * vector

    # Matrix Matrix
    if isinstance(tensor1[0], list):
        
        matrixA = tensor1
        matrixB = tensor2
        
        assert len(matrixA[0])==len(matrixB), f"sizes mA: {len(matrixA)} mB: {len(matrixB[0])} arent compatible, do you need to transpose something?"

        outMatrix = [[] for i in range(len(matrixA))]
        for i in range(len(matrixA)):
            for j in range(len(matrixB[0])):
                tempMatrixB = [vector[j] for vector in matrixB]
                outMatrix[i].append(vectorDot(matrixA[i], tempMatrixB))
    
        return outMatrix
    
    # Vector Matrix
    elif not isinstance(tensor1[0], list) and isinstance(tensor2[0], list):
        vector = tensor1
        matrix = tensor2
        outMatrix = []
        for i in range(len(matrix)):
            outMatrix.append(vectorDot(vector, matrix[i]))
            #Optional
            outMatrix[-1] = round(outMatrix[-1], 10)
        
        return outMatrix

    # Vector Vector
    elif isinstance(tensor1[0], list) and isinstance(tensor2[0], list):
        return vectorDot(tensor1, tensor2)


def vectorDot(vectA, vectB):
    assert len(vectA)==len(vectB), f"both vectors must be same size. SizeA = {len(vectA)}, sizeB = {len(vectB)}"
    
    result = 0
    for i in range(len(vectA)):
        result += (vectA[i] * vectB[i])

    return result

def transpose(matrix):
    if not isinstance(matrix[0], list):
        print("this is a vector, not a matrix!")
        return matrix

    outMatrix = [[] for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            outMatrix[i].append(matrix[j][i])
        
    return outMatrix

def addBias(tensor, biasVect):
    # print(tensor, biasVect)
    # Vector Vector
    if not isinstance(tensor[0], list):
        vector = tensor
        output = []
        for i in range(len(vector)):
            output.append(vector[i]+biasVect[i])
            output[-1] = round(output[-1], 10)

        return output    
    
    # Matrix Vector
    elif isinstance(tensor[0], list):
        matrix = tensor
        output = [[] for n in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output[i].append(matrix[i][j]+biasVect[j])
                output[i][-1] = round(output[i][-1], 10)

        return output
