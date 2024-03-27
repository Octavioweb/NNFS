## Haciendo funciones de cero, a lo bestia

#dot product


def dot(vectA, vectB):
    assert len(vectA)==len(vectB), "both vectors must be same size"
    
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
            outMatrix[j].append(dot(matrixA[j], tempMatrixB))
    
    return outMatrix

def addBias(matrixA, biasVect):
    
    output = [[] for n in matrixA]
    for i in range(len(matrixA)):
        for j in range(len(matrixA[0])):
            output[i].append(matrixA[i][j]+biasVect[j])

            #Optional
            output[i][-1] = round(output[i][-1], 2)

    return output        


inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]

output = matrixDot(inputs, transpose(weights))
output2 = addBias(output, biases)
print(output2)

"""print(matrixDot(
[[1,2,3],
 [4,5,6],
 [7,8,9],
 [10,11,12],
 [13,14,15]],

[[1,4,7,10,13],
 [2,5,8,11,14],
 [3,6,9,12,15]]))

print(transpose([[1,2,3], [4,5,6], [7,8,9],[10,11,12],[13,14,15]]))

[[1,2,3],
 [4,5,6],
 [7,8,9],
 [10,11,12],
 [13,14,15]]

[[1,4,7,10,13],
 [2,5,8,11,14],
 [3,6,9,12,15]]

# print(dot([1,2,3,4], [5,6,7,8]))

input = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
biases = [2.0, 3.0, 0.5]

neuron = dot(input, weights) 
print(neuron)"""