import numpy as np

# Caso de prueba
def imageE(nxC, nyC):
    gameState = np.zeros((nxC, nyC))

    gameState[60, 4] = 1
    gameState[60, 17] = 1
    gameState[60, 18] = 1
    gameState[60, 80] = 1
    gameState[60, 81] = 1
    gameState[60, 94] = 1
    gameState[61, 4] = 1
    gameState[61, 5] = 1
    gameState[61, 6] = 1
    gameState[61, 18] = 1
    gameState[61, 80] = 1
    gameState[61, 92] = 1
    gameState[61, 93] = 1
    gameState[61, 94] = 1
    gameState[62, 7] = 1
    gameState[62, 18] = 1
    gameState[62, 20] = 1
    gameState[62, 21] = 1
    gameState[62, 27] = 1
    gameState[62, 28] = 1
    gameState[62, 70] = 1
    gameState[62, 71] = 1
    gameState[62, 77] = 1
    gameState[62, 78] = 1
    gameState[62, 80] = 1
    gameState[62, 91] = 1
    gameState[63, 6] = 1
    gameState[63, 7] = 1
    gameState[63, 19] = 1
    gameState[63, 27] = 1
    gameState[63, 29] = 1
    gameState[63, 69] = 1
    gameState[63, 71] = 1
    gameState[63, 79] = 1
    gameState[63, 91] = 1
    gameState[63, 92] = 1
    gameState[64, 23] = 1
    gameState[64, 28] = 1
    gameState[64, 29] = 1
    gameState[64, 30] = 1
    gameState[64, 68] = 1
    gameState[64, 69] = 1
    gameState[64, 70] = 1
    gameState[64, 75] = 1
    gameState[65, 21] = 1
    gameState[65, 24] = 1
    gameState[65, 29] = 1
    gameState[65, 30] = 1
    gameState[65, 31] = 1
    gameState[65, 67] = 1
    gameState[65, 68] = 1
    gameState[65, 69] = 1
    gameState[65, 74] = 1
    gameState[65, 77] = 1
    gameState[66, 9] = 1
    gameState[66, 22] = 1
    gameState[66, 23] = 1
    gameState[66, 28] = 1
    gameState[66, 29] = 1
    gameState[66, 30] = 1
    gameState[66, 68] = 1
    gameState[66, 69] = 1
    gameState[66, 70] = 1
    gameState[66, 75] = 1
    gameState[66, 76] = 1
    gameState[66, 89] = 1
    gameState[67, 9] = 1
    gameState[67, 19] = 1
    gameState[67, 27] = 1
    gameState[67, 29] = 1
    gameState[67, 36] = 1
    gameState[67, 37] = 1
    gameState[67, 61] = 1
    gameState[67, 62] = 1
    gameState[67, 69] = 1
    gameState[67, 71] = 1
    gameState[67, 79] = 1
    gameState[67, 89] = 1
    gameState[68, 8] = 1
    gameState[68, 10] = 1
    gameState[68, 19] = 1
    gameState[68, 20] = 1
    gameState[68, 27] = 1
    gameState[68, 28] = 1
    gameState[68, 36] = 1
    gameState[68, 38] = 1
    gameState[68, 60] = 1
    gameState[68, 62] = 1
    gameState[68, 70] = 1
    gameState[68, 71] = 1
    gameState[68, 78] = 1
    gameState[68, 79] = 1
    gameState[68, 88] = 1
    gameState[68, 90] = 1
    gameState[69, 7] = 1
    gameState[69, 8] = 1
    gameState[69, 10] = 1
    gameState[69, 11] = 1
    gameState[69, 18] = 1
    gameState[69, 20] = 1
    gameState[69, 38] = 1
    gameState[69, 60] = 1
    gameState[69, 78] = 1
    gameState[69, 80] = 1
    gameState[69, 87] = 1
    gameState[69, 88] = 1
    gameState[69, 90] = 1
    gameState[69, 91] = 1
    gameState[70, 6] = 1
    gameState[70, 12] = 1
    gameState[70, 38] = 1
    gameState[70, 39] = 1
    gameState[70, 59] = 1
    gameState[70, 60] = 1
    gameState[70, 86] = 1
    gameState[70, 92] = 1
    gameState[71, 9] = 1
    gameState[71, 89] = 1
    gameState[72, 6] = 1
    gameState[72, 7] = 1
    gameState[72, 11] = 1
    gameState[72, 12] = 1
    gameState[72, 86] = 1
    gameState[72, 87] = 1
    gameState[72, 91] = 1
    gameState[72, 92] = 1
    gameState[75, 11] = 1
    gameState[75, 12] = 1
    gameState[75, 13] = 1
    gameState[75, 85] = 1
    gameState[75, 86] = 1
    gameState[75, 87] = 1
    gameState[76, 11] = 1
    gameState[76, 13] = 1
    gameState[76, 14] = 1
    gameState[76, 84] = 1
    gameState[76, 85] = 1
    gameState[76, 87] = 1
    gameState[77, 13] = 1
    gameState[77, 14] = 1
    gameState[77, 84] = 1
    gameState[77, 85] = 1
    gameState[78, 12] = 1
    gameState[78, 13] = 1
    gameState[78, 85] = 1
    gameState[78, 86] = 1
    gameState[79, 10] = 1
    gameState[79, 12] = 1
    gameState[79, 86] = 1
    gameState[79, 88] = 1
    gameState[80, 8] = 1
    gameState[80, 9] = 1
    gameState[80, 12] = 1
    gameState[80, 86] = 1
    gameState[80, 89] = 1
    gameState[80, 90] = 1
    gameState[86, 9] = 1
    gameState[86, 10] = 1
    gameState[86, 11] = 1
    gameState[86, 12] = 1
    gameState[86, 13] = 1
    gameState[86, 85] = 1
    gameState[86, 86] = 1
    gameState[86, 87] = 1
    gameState[86, 88] = 1
    gameState[86, 89] = 1
    gameState[87, 8] = 1
    gameState[87, 10] = 1
    gameState[87, 11] = 1
    gameState[87, 12] = 1
    gameState[87, 14] = 1
    gameState[87, 84] = 1
    gameState[87, 86] = 1
    gameState[87, 87] = 1
    gameState[87, 88] = 1
    gameState[87, 90] = 1
    gameState[88, 9] = 1
    gameState[88, 13] = 1
    gameState[88, 85] = 1
    gameState[88, 89] = 1
    gameState[89, 10] = 1
    gameState[89, 11] = 1
    gameState[89, 12] = 1
    gameState[89, 86] = 1
    gameState[89, 87] = 1
    gameState[89, 88] = 1
    gameState[90, 11] = 1
    gameState[90, 87] = 1
    gameState[92, 8] = 1
    gameState[92, 9] = 1
    gameState[92, 89] = 1
    gameState[92, 90] = 1
    gameState[93, 9] = 1
    gameState[93, 89] = 1
    gameState[94, 6] = 1
    gameState[94, 7] = 1
    gameState[94, 8] = 1
    gameState[94, 90] = 1
    gameState[94, 91] = 1
    gameState[94, 92] = 1
    gameState[95, 6] = 1
    gameState[95, 92] = 1
    gameState[98, 5] = 1
    gameState[98, 6] = 1
    gameState[98, 92] = 1
    gameState[98, 93] = 1
    gameState[99, 5] = 1
    gameState[99, 47] = 1
    gameState[99, 48] = 1
    gameState[99, 50] = 1
    gameState[99, 51] = 1
    gameState[99, 93] = 1
    gameState[100, 6] = 1
    gameState[100, 8] = 1
    gameState[100, 47] = 1
    gameState[100, 51] = 1
    gameState[100, 90] = 1
    gameState[100, 92] = 1
    gameState[101, 45] = 1
    gameState[101, 48] = 1
    gameState[101, 50] = 1
    gameState[101, 53] = 1
    gameState[102, 8] = 1
    gameState[102, 10] = 1
    gameState[102, 45] = 1
    gameState[102, 47] = 1
    gameState[102, 51] = 1
    gameState[102, 53] = 1
    gameState[102, 88] = 1
    gameState[102, 90] = 1
    gameState[103, 46] = 1
    gameState[103, 52] = 1
    gameState[104, 10] = 1
    gameState[104, 12] = 1
    gameState[104, 86] = 1
    gameState[104, 88] = 1
    gameState[106, 12] = 1
    gameState[106, 14] = 1
    gameState[106, 84] = 1
    gameState[106, 86] = 1
    gameState[107, 6] = 1
    gameState[107, 7] = 1
    gameState[107, 13] = 1
    gameState[107, 14] = 1
    gameState[107, 84] = 1
    gameState[107, 85] = 1
    gameState[107, 91] = 1
    gameState[107, 92] = 1
    gameState[108, 6] = 1
    gameState[108, 47] = 1
    gameState[108, 48] = 1
    gameState[108, 50] = 1
    gameState[108, 51] = 1
    gameState[108, 92] = 1
    gameState[109, 7] = 1
    gameState[109, 9] = 1
    gameState[109, 47] = 1
    gameState[109, 51] = 1
    gameState[109, 89] = 1
    gameState[109, 91] = 1
    gameState[110, 45] = 1
    gameState[110, 48] = 1
    gameState[110, 50] = 1
    gameState[110, 53] = 1
    gameState[111, 9] = 1
    gameState[111, 11] = 1
    gameState[111, 45] = 1
    gameState[111, 47] = 1
    gameState[111, 51] = 1
    gameState[111, 53] = 1
    gameState[111, 87] = 1
    gameState[111, 89] = 1
    gameState[112, 46] = 1
    gameState[112, 52] = 1
    gameState[113, 11] = 1
    gameState[113, 13] = 1
    gameState[113, 85] = 1
    gameState[113, 87] = 1
    gameState[115, 13] = 1
    gameState[115, 15] = 1
    gameState[115, 83] = 1
    gameState[115, 85] = 1
    gameState[116, 14] = 1
    gameState[116, 15] = 1
    gameState[116, 83] = 1
    gameState[116, 84] = 1
    gameState[117, 47] = 1
    gameState[117, 48] = 1
    gameState[117, 50] = 1
    gameState[117, 51] = 1
    gameState[118, 9] = 1
    gameState[118, 10] = 1
    gameState[118, 47] = 1
    gameState[118, 51] = 1
    gameState[118, 88] = 1
    gameState[118, 89] = 1
    gameState[119, 9] = 1
    gameState[119, 45] = 1
    gameState[119, 48] = 1
    gameState[119, 50] = 1
    gameState[119, 53] = 1
    gameState[119, 89] = 1
    gameState[120, 10] = 1
    gameState[120, 12] = 1
    gameState[120, 45] = 1
    gameState[120, 47] = 1
    gameState[120, 51] = 1
    gameState[120, 53] = 1
    gameState[120, 86] = 1
    gameState[120, 88] = 1
    gameState[121, 46] = 1
    gameState[121, 52] = 1
    gameState[122, 12] = 1
    gameState[122, 14] = 1
    gameState[122, 84] = 1
    gameState[122, 86] = 1
    gameState[124, 14] = 1
    gameState[124, 16] = 1
    gameState[124, 82] = 1
    gameState[124, 84] = 1
    gameState[125, 15] = 1
    gameState[125, 16] = 1
    gameState[125, 82] = 1
    gameState[125, 83] = 1
    gameState[126, 47] = 1
    gameState[126, 48] = 1
    gameState[126, 50] = 1
    gameState[126, 51] = 1
    gameState[127, 10] = 1
    gameState[127, 11] = 1
    gameState[127, 47] = 1
    gameState[127, 51] = 1
    gameState[127, 87] = 1
    gameState[127, 88] = 1
    gameState[128, 10] = 1
    gameState[128, 45] = 1
    gameState[128, 48] = 1
    gameState[128, 50] = 1
    gameState[128, 53] = 1
    gameState[128, 88] = 1
    gameState[129, 11] = 1
    gameState[129, 13] = 1
    gameState[129, 45] = 1
    gameState[129, 47] = 1
    gameState[129, 51] = 1
    gameState[129, 53] = 1
    gameState[129, 85] = 1
    gameState[129, 87] = 1
    gameState[130, 46] = 1
    gameState[130, 52] = 1
    gameState[131, 13] = 1
    gameState[131, 15] = 1
    gameState[131, 83] = 1
    gameState[131, 85] = 1
    gameState[133, 15] = 1
    gameState[133, 17] = 1
    gameState[133, 81] = 1
    gameState[133, 83] = 1
    gameState[134, 16] = 1
    gameState[134, 17] = 1
    gameState[134, 81] = 1
    gameState[134, 82] = 1
    gameState[138, 13] = 1
    gameState[138, 14] = 1
    gameState[138, 84] = 1
    gameState[138, 85] = 1
    gameState[139, 13] = 1
    gameState[139, 85] = 1
    gameState[140, 14] = 1
    gameState[140, 16] = 1
    gameState[140, 82] = 1
    gameState[140, 84] = 1
    gameState[142, 16] = 1
    gameState[142, 18] = 1
    gameState[142, 80] = 1
    gameState[142, 82] = 1
    gameState[143, 17] = 1
    gameState[143, 18] = 1
    gameState[143, 80] = 1
    gameState[143, 81] = 1
    
    return gameState