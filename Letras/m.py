import numpy as np

# Caso de prueba
def imageM(nxC, nyC):
    gameState = np.zeros((nxC, nyC))

    gameState[146,99] = 1
    gameState[146,98] = 1

    gameState[147,98] = 1

    gameState[148,96] = 1
    gameState[148,98] = 1

    gameState[149,97] = 1
    gameState[149,96] = 1

    gameState[155,96] = 1

    gameState[156,96] = 1
    gameState[156,95] = 1
    gameState[156,94] = 1

    gameState[157,93] = 1

    gameState[158,93] = 1
    gameState[158,94] = 1

    gameState[163,91] = 1

    gameState[164,90] = 1
    gameState[164,91] = 1
    gameState[164,92] = 1

    gameState[165,89] = 1
    gameState[165,90] = 1
    gameState[165,91] = 1
    gameState[165,92] = 1
    gameState[165,93] = 1

    gameState[166,90] = 1
    gameState[166,92] = 1
    gameState[166,88] = 1
    gameState[166,94] = 1

    gameState[167,88] = 1
    gameState[167,94] = 1
    gameState[167,89] = 1
    gameState[167,93] = 1

    gameState[170,88] = 1
    gameState[170,89] = 1

    gameState[171,88] = 1
    gameState[171,89] = 1

    gameState[172,87] = 1
    
    gameState[173,87] = 1
    gameState[173,88] = 1
    gameState[173,89] = 1

    gameState[174,91] = 1

    gameState[175,87] = 1
    gameState[175,88] = 1
    gameState[175,89] = 1
    gameState[175,90] = 1
    gameState[175,91] = 1

    gameState[176,89] = 1
    gameState[176,90] = 1

    gameState[179,92] = 1
    gameState[179,91] = 1
    gameState[179,87] = 1
    gameState[179,86] = 1

    gameState[180,87] = 1
    gameState[180,88] = 1
    gameState[180,89] = 1
    gameState[180,90] = 1
    gameState[180,91] = 1

    gameState[181,87] = 1
    gameState[181,88] = 1
    gameState[181,90] = 1
    gameState[181,91] = 1

    gameState[182,87] = 1
    gameState[182,88] = 1
    gameState[182,90] = 1
    gameState[182,91] = 1

    gameState[183,88] = 1
    gameState[183,89] = 1
    gameState[183,90] = 1

    gameState[187,87] = 1
    gameState[187,86] = 1

    gameState[188,87] = 1

    gameState[189,86] = 1
    gameState[189,85] = 1
    gameState[189,84] = 1
    gameState[189,84] = 1
    gameState[190,84] = 1
    
    ##### 

    gameState[179,83] = 1    
    gameState[179,82] = 1    
    gameState[178,82] = 1    
    gameState[177,82] = 1    
    gameState[176,81] = 1    
    gameState[176,80] = 1    
    gameState[177,80] = 1  

    gameState[177,74] = 1  
    gameState[176,74] = 1  
    gameState[177,73] = 1  
    gameState[172,74] = 1  
    gameState[171,74] = 1  
    gameState[171,73] = 1  
    gameState[172,71] = 1
    gameState[173,70] = 1
    gameState[174,70] = 1
    gameState[175,70] = 1
    gameState[176,71] = 1

    gameState[172,63] = 1
    gameState[171,62] = 1
    gameState[170,62] = 1
    gameState[173,62] = 1
    gameState[174,62] = 1
    gameState[169,60] = 1
    gameState[175,60] = 1
    gameState[175,58] = 1
    gameState[169,58] = 1
    gameState[170,58] = 1
    gameState[174,58] = 1
    gameState[172,58] = 1
    ###
    gameState[170,51] = 1
    gameState[169,51] = 1
    gameState[170,50] = 1
    gameState[169,49] = 1
    gameState[168,49] = 1
    gameState[167,49] = 1
    gameState[167,48] = 1

    gameState[154,89] = 1
    gameState[153,89] = 1
    gameState[151,89] = 1
    gameState[149,89] = 1
    gameState[148,89] = 1

    gameState[148,88] = 1
    gameState[154,88] = 1
    
    gameState[149,87] = 1
    gameState[153,87] = 1
    gameState[152,86] = 1
    gameState[151,86] = 1
    gameState[150,86] = 1

    gameState[151,72] = 1
    gameState[150,72] = 1
    gameState[149,72] = 1
    gameState[148,72] = 1
    gameState[147,72] = 1
    gameState[146,71] = 1
    gameState[148,71] = 1
    gameState[149,71] = 1
    gameState[150,71] = 1
    gameState[152,71] = 1
    gameState[151,70] = 1
    gameState[147,70] = 1
    gameState[148,69] = 1
    gameState[149,69] = 1
    gameState[150,69] = 1
    gameState[149,68] = 1

    gameState[151,66] = 1
    gameState[151,65] = 1
    gameState[152,66] = 1
    gameState[152,64] = 1
    gameState[153,64] = 1
    gameState[154,64] = 1
    gameState[154,63] = 1
    
    #### Colapsadores

    gameState[161,4] = 1
    gameState[162,4] = 1
    gameState[161,3] = 1
    gameState[162,2] = 1
    gameState[163,2] = 1
    gameState[164,2] = 1
    gameState[164,1] = 1

    gameState[154,3] = 1
    gameState[155,3] = 1
    gameState[154,2] = 1
    gameState[156,2] = 1
    gameState[156,1] = 1
    gameState[156,0] = 1
    gameState[157,0] = 1

    #### Disparador simple

    gameState[107,69] = 1
    gameState[106,69] = 1
    gameState[106,68] = 1
    gameState[107,68] = 1
    
    gameState[107,56] = 1
    gameState[106,56] = 1
    gameState[105,56] = 1
    gameState[104,57] = 1
    gameState[103,57] = 1

    gameState[108,57] = 1
    gameState[109,57] = 1
    gameState[108,55] = 1
    gameState[104,55] = 1

    gameState[107,54] = 1
    gameState[106,53] = 1
    gameState[105,54] = 1

    gameState[105,48] = 1
    gameState[104,48] = 1
    gameState[103,48] = 1
    gameState[103,46] = 1
    gameState[105,46] = 1

    gameState[106,45] = 1
    gameState[105,45] = 1
    gameState[104,45] = 1
    gameState[103,45] = 1
    gameState[102,45] = 1

    gameState[101,43] = 1
    gameState[102,43] = 1
    gameState[106,43] = 1
    gameState[107,43] = 1
    gameState[101,44] = 1
    gameState[102,44] = 1
    gameState[106,44] = 1
    gameState[107,44] = 1

    gameState[104,40] = 1
    gameState[103,39] = 1
    gameState[102,39] = 1
    gameState[101,37] = 1
    gameState[102,35] = 1
    gameState[104,34] = 1
    gameState[105,34] = 1
    gameState[105,35] = 1
    
    # Segundo disparador simple
    
    gameState[92,69] = 1
    gameState[93,69] = 1
    gameState[92,68] = 1
    gameState[93,68] = 1
    
    gameState[92,56] = 1
    gameState[93,56] = 1
    gameState[94,56] = 1
    gameState[91,57] = 1
    gameState[90,57] = 1
    
    gameState[95,57] = 1
    gameState[96,57] = 1
    gameState[91,55] = 1
    gameState[95,55] = 1
    
    gameState[92,54] = 1
    gameState[93,53] = 1
    gameState[94,54] = 1
    
    gameState[94,48] = 1
    gameState[95,48] = 1
    gameState[96,48] = 1
    gameState[94,46] = 1
    gameState[96,46] = 1
    
    gameState[93,45] = 1
    gameState[94,45] = 1
    gameState[95,45] = 1
    gameState[96,45] = 1
    gameState[97,45] = 1
    

    gameState[92,43] = 1
    gameState[93,43] = 1
    gameState[97,43] = 1
    gameState[98,43] = 1
    gameState[92,44] = 1
    gameState[93,44] = 1
    gameState[97,44] = 1
    gameState[98,44] = 1

    
    gameState[95,40] = 1
    gameState[96,39] = 1
    gameState[97,39] = 1
    gameState[98,37] = 1
    gameState[97,35] = 1
    gameState[95,34] = 1
    gameState[94,34] = 1
    gameState[94,35] = 1

    # Segundos colapsores

    gameState[37,4] = 1
    gameState[38,4] = 1
    gameState[38,3] = 1
    gameState[37,2] = 1
    gameState[36,2] = 1
    gameState[35,2] = 1
    gameState[35,1] = 1

    gameState[45,3] = 1
    gameState[44,3] = 1
    gameState[45,2] = 1
    gameState[43,2] = 1
    gameState[43,1] = 1
    gameState[43,0] = 1
    gameState[42,0] = 1

    # Segundo disparador compuesto
    
    gameState[53,99] = 1
    gameState[53,98] = 1

    gameState[52,98] = 1

    gameState[51,96] = 1
    gameState[51,98] = 1

    gameState[50,97] = 1
    gameState[50,96] = 1

    gameState[44,96] = 1

    gameState[43,96] = 1
    gameState[43,95] = 1
    gameState[43,94] = 1

    gameState[42,93] = 1
    
    gameState[41,93] = 1
    gameState[41,94] = 1

    gameState[36,91] = 1

    gameState[35,90] = 1
    gameState[35,91] = 1
    gameState[35,92] = 1

    gameState[34,89] = 1
    gameState[34,90] = 1
    gameState[34,91] = 1
    gameState[34,92] = 1
    gameState[34,93] = 1
    
    gameState[33,90] = 1
    gameState[33,92] = 1
    gameState[33,88] = 1
    gameState[33,94] = 1
    
    gameState[32,88] = 1
    gameState[32,94] = 1
    gameState[32,89] = 1
    gameState[32,93] = 1
    
    gameState[29,88] = 1
    gameState[29,89] = 1

    gameState[28,88] = 1
    gameState[28,89] = 1

    gameState[27,87] = 1
    
    gameState[26,87] = 1
    gameState[26,88] = 1
    gameState[26,89] = 1

    gameState[25,91] = 1

    gameState[24,87] = 1
    gameState[24,88] = 1
    gameState[24,89] = 1
    gameState[24,90] = 1
    gameState[24,91] = 1

    gameState[23,89] = 1
    gameState[23,90] = 1

    gameState[20,92] = 1
    gameState[20,91] = 1
    gameState[20,87] = 1
    gameState[20,86] = 1

    gameState[19,87] = 1
    gameState[19,88] = 1
    gameState[19,89] = 1
    gameState[19,90] = 1
    gameState[19,91] = 1

    gameState[18,87] = 1
    gameState[18,88] = 1
    gameState[18,90] = 1
    gameState[18,91] = 1

    gameState[17,87] = 1
    gameState[17,88] = 1
    gameState[17,90] = 1
    gameState[17,91] = 1

    gameState[16,88] = 1
    gameState[16,89] = 1
    gameState[16,90] = 1

    gameState[12,87] = 1
    gameState[12,86] = 1

    gameState[11,87] = 1
    
    gameState[10,86] = 1
    gameState[10,85] = 1
    gameState[9,84] = 1
    gameState[10,84] = 1
    gameState[10,84] = 1
    
    ##### 

    gameState[20,83] = 1    
    gameState[20,82] = 1 

    gameState[21,82] = 1 

    gameState[22,82] = 1    
    gameState[23,81] = 1    
    gameState[22,80] = 1    
    gameState[23,80] = 1  
    
    gameState[22,74] = 1  
    gameState[23,74] = 1  
    gameState[22,73] = 1  
    gameState[27,74] = 1  
    gameState[28,74] = 1  
    gameState[28,73] = 1  
    gameState[27,71] = 1
    gameState[26,70] = 1
    gameState[25,70] = 1
    gameState[24,70] = 1
    gameState[23,71] = 1

    gameState[27,63] = 1
    gameState[28,62] = 1
    gameState[29,62] = 1
    gameState[26,62] = 1
    gameState[25,62] = 1
    gameState[24,60] = 1
    gameState[30,60] = 1
    gameState[24,58] = 1
    gameState[30,58] = 1
    gameState[25,58] = 1
    gameState[29,58] = 1
    gameState[27,58] = 1
    ###
    gameState[29,51] = 1
    gameState[30,51] = 1
    gameState[29,50] = 1
    gameState[30,49] = 1
    gameState[31,49] = 1
    gameState[32,49] = 1
    gameState[32,48] = 1
    
    gameState[45,89] = 1
    gameState[46,89] = 1
    gameState[48,89] = 1
    gameState[50,89] = 1
    gameState[51,89] = 1

    gameState[45,88] = 1
    gameState[51,88] = 1
    
    gameState[46,87] = 1
    gameState[50,87] = 1
    gameState[47,86] = 1
    gameState[48,86] = 1
    gameState[49,86] = 1
    
    gameState[48,72] = 1
    gameState[49,72] = 1
    gameState[50,72] = 1
    gameState[51,72] = 1
    gameState[52,72] = 1
    gameState[53,71] = 1
    gameState[47,71] = 1
    gameState[49,71] = 1
    gameState[50,71] = 1
    gameState[51,71] = 1
    gameState[52,70] = 1
    gameState[48,70] = 1
    gameState[49,69] = 1
    gameState[50,69] = 1
    gameState[51,69] = 1
    gameState[50,68] = 1
    
    gameState[48,66] = 1
    gameState[48,65] = 1
    gameState[47,66] = 1
    gameState[47,64] = 1
    gameState[46,64] = 1
    gameState[45,64] = 1
    gameState[45,63] = 1
    
    return gameState