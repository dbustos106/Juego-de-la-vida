import numpy as np

# Caso de prueba
def imageA(nxC, nyC):
    gameState = np.zeros((nxC, nyC))

    gameState[1, 81] = 1
    gameState[1, 82] = 1
    gameState[2, 81] = 1
    gameState[2, 82] = 1
    gameState[8, 81] = 1
    gameState[8, 82] = 1
    gameState[8, 83] = 1
    gameState[9, 80] = 1
    gameState[9, 81] = 1
    gameState[9, 83] = 1
    gameState[9, 84] = 1
    gameState[10, 80] = 1
    gameState[10, 81] = 1
    gameState[10, 83] = 1
    gameState[10, 84] = 1
    gameState[11, 80] = 1
    gameState[11, 81] = 1
    gameState[11, 82] = 1
    gameState[11, 83] = 1
    gameState[11, 84] = 1
    gameState[12, 79] = 1
    gameState[12, 80] = 1
    gameState[12, 84] = 1
    gameState[12, 85] = 1
    gameState[15, 82] = 1
    gameState[15, 83] = 1
    gameState[16, 80] = 1
    gameState[16, 81] = 1
    gameState[16, 82] = 1
    gameState[16, 83] = 1
    gameState[16, 84] = 1
    gameState[17, 84] = 1
    gameState[18, 80] = 1
    gameState[18, 81] = 1
    gameState[18, 82] = 1
    gameState[19, 80] = 1
    gameState[20, 81] = 1
    gameState[20, 82] = 1
    gameState[21, 81] = 1
    gameState[21, 82] = 1
    gameState[24, 81] = 1
    gameState[24, 82] = 1
    gameState[24, 86] = 1
    gameState[24, 87] = 1
    gameState[25, 81] = 1
    gameState[25, 83] = 1
    gameState[25, 85] = 1
    gameState[25, 87] = 1
    gameState[26, 74] = 1
    gameState[26, 76] = 1
    gameState[26, 82] = 1
    gameState[26, 83] = 1
    gameState[26, 84] = 1
    gameState[26, 85] = 1
    gameState[26, 86] = 1
    gameState[27, 74] = 1
    gameState[27, 75] = 1
    gameState[27, 83] = 1
    gameState[27, 84] = 1
    gameState[27, 85] = 1
    gameState[28, 75] = 1
    gameState[28, 84] = 1
    gameState[33, 68] = 1
    gameState[34, 66] = 1
    gameState[34, 67] = 1
    gameState[34, 87] = 1
    gameState[35, 67] = 1
    gameState[35, 68] = 1
    gameState[35, 75] = 1
    gameState[35, 76] = 1
    gameState[35, 86] = 1
    gameState[35, 87] = 1
    gameState[35, 88] = 1
    gameState[36, 75] = 1
    gameState[36, 77] = 1
    gameState[36, 85] = 1
    gameState[36, 89] = 1
    gameState[37, 75] = 1
    gameState[37, 84] = 1
    gameState[37, 86] = 1
    gameState[37, 87] = 1
    gameState[37, 88] = 1
    gameState[37, 90] = 1
    gameState[38, 85] = 1
    gameState[38, 86] = 1
    gameState[38, 87] = 1
    gameState[38, 88] = 1
    gameState[38, 89] = 1
    gameState[43, 82] = 1
    gameState[43, 83] = 1
    gameState[43, 84] = 1
    gameState[44, 82] = 1
    gameState[45, 83] = 1
    gameState[48, 53] = 1
    gameState[49, 51] = 1
    gameState[49, 52] = 1
    gameState[50, 52] = 1
    gameState[50, 53] = 1
    gameState[52, 84] = 1
    gameState[52, 85] = 1
    gameState[52, 86] = 1
    gameState[53, 83] = 1
    gameState[53, 87] = 1
    gameState[54, 82] = 1
    gameState[54, 88] = 1
    gameState[55, 82] = 1
    gameState[55, 83] = 1
    gameState[55, 85] = 1
    gameState[55, 87] = 1
    gameState[55, 88] = 1
    gameState[58, 85] = 1
    gameState[59, 84] = 1
    gameState[59, 86] = 1
    gameState[60, 84] = 1
    gameState[60, 86] = 1
    gameState[61, 85] = 1
    gameState[63, 84] = 1
    gameState[63, 85] = 1
    gameState[64, 84] = 1
    gameState[64, 85] = 1
    gameState[79, 38] = 1
    gameState[79, 39] = 1
    gameState[79, 40] = 1
    gameState[80, 38] = 1
    gameState[80, 42] = 1
    gameState[80, 43] = 1
    gameState[81, 39] = 1
    gameState[81, 40] = 1
    gameState[81, 41] = 1
    gameState[81, 42] = 1
    gameState[81, 43] = 1
    gameState[83, 39] = 1
    gameState[83, 40] = 1
    gameState[83, 41] = 1
    gameState[83, 42] = 1
    gameState[83, 43] = 1
    gameState[84, 38] = 1
    gameState[84, 42] = 1
    gameState[84, 43] = 1
    gameState[85, 38] = 1
    gameState[85, 39] = 1
    gameState[85, 40] = 1
    gameState[90, 38] = 1
    gameState[90, 39] = 1
    gameState[90, 40] = 1
    gameState[91, 38] = 1
    gameState[91, 42] = 1
    gameState[91, 43] = 1
    gameState[92, 39] = 1
    gameState[92, 40] = 1
    gameState[92, 41] = 1
    gameState[92, 42] = 1
    gameState[92, 43] = 1
    gameState[93, 13] = 1
    gameState[93, 15] = 1
    gameState[94, 7] = 1
    gameState[94, 8] = 1
    gameState[94, 16] = 1
    gameState[94, 39] = 1
    gameState[94, 40] = 1
    gameState[94, 41] = 1
    gameState[94, 42] = 1
    gameState[94, 43] = 1
    gameState[95, 8] = 1
    gameState[95, 12] = 1
    gameState[95, 17] = 1
    gameState[95, 20] = 1
    gameState[95, 21] = 1
    gameState[95, 38] = 1
    gameState[95, 42] = 1
    gameState[95, 43] = 1
    gameState[96, 5] = 1
    gameState[96, 6] = 1
    gameState[96, 7] = 1
    gameState[96, 12] = 1
    gameState[96, 13] = 1
    gameState[96, 15] = 1
    gameState[96, 18] = 1
    gameState[96, 20] = 1
    gameState[96, 21] = 1
    gameState[96, 38] = 1
    gameState[96, 39] = 1
    gameState[96, 40] = 1
    gameState[97, 5] = 1
    gameState[97, 16] = 1
    gameState[97, 17] = 1
    gameState[102, 5] = 1
    gameState[102, 16] = 1
    gameState[102, 17] = 1
    gameState[103, 5] = 1
    gameState[103, 6] = 1
    gameState[103, 7] = 1
    gameState[103, 12] = 1
    gameState[103, 13] = 1
    gameState[103, 15] = 1
    gameState[103, 18] = 1
    gameState[103, 20] = 1
    gameState[103, 21] = 1
    gameState[103, 38] = 1
    gameState[103, 39] = 1
    gameState[103, 40] = 1
    gameState[104, 8] = 1
    gameState[104, 12] = 1
    gameState[104, 17] = 1
    gameState[104, 20] = 1
    gameState[104, 21] = 1
    gameState[104, 38] = 1
    gameState[104, 42] = 1
    gameState[104, 43] = 1
    gameState[105, 7] = 1
    gameState[105, 8] = 1
    gameState[105, 16] = 1
    gameState[105, 39] = 1
    gameState[105, 40] = 1
    gameState[105, 41] = 1
    gameState[105, 42] = 1
    gameState[105, 43] = 1
    gameState[106, 13] = 1
    gameState[106, 15] = 1
    gameState[107, 39] = 1
    gameState[107, 40] = 1
    gameState[107, 41] = 1
    gameState[107, 42] = 1
    gameState[107, 43] = 1
    gameState[108, 38] = 1
    gameState[108, 42] = 1
    gameState[108, 43] = 1
    gameState[109, 38] = 1
    gameState[109, 39] = 1
    gameState[109, 40] = 1
    gameState[114, 38] = 1
    gameState[114, 39] = 1
    gameState[114, 40] = 1
    gameState[115, 38] = 1
    gameState[115, 42] = 1
    gameState[115, 43] = 1
    gameState[116, 39] = 1
    gameState[116, 40] = 1
    gameState[116, 41] = 1
    gameState[116, 42] = 1
    gameState[116, 43] = 1
    gameState[118, 39] = 1
    gameState[118, 40] = 1
    gameState[118, 41] = 1
    gameState[118, 42] = 1
    gameState[118, 43] = 1
    gameState[119, 38] = 1
    gameState[119, 42] = 1
    gameState[119, 43] = 1
    gameState[120, 38] = 1
    gameState[120, 39] = 1
    gameState[120, 40] = 1
    gameState[135, 84] = 1
    gameState[135, 85] = 1
    gameState[136, 84] = 1
    gameState[136, 85] = 1
    gameState[138, 85] = 1
    gameState[139, 84] = 1
    gameState[139, 86] = 1
    gameState[140, 84] = 1
    gameState[140, 86] = 1
    gameState[141, 85] = 1
    gameState[144, 82] = 1
    gameState[144, 83] = 1
    gameState[144, 85] = 1
    gameState[144, 87] = 1
    gameState[144, 88] = 1
    gameState[145, 82] = 1
    gameState[145, 88] = 1
    gameState[146, 83] = 1
    gameState[146, 87] = 1
    gameState[147, 84] = 1
    gameState[147, 85] = 1
    gameState[147, 86] = 1
    gameState[149, 52] = 1
    gameState[149, 53] = 1
    gameState[150, 51] = 1
    gameState[150, 52] = 1
    gameState[151, 53] = 1
    gameState[154, 83] = 1
    gameState[155, 82] = 1
    gameState[156, 82] = 1
    gameState[156, 83] = 1
    gameState[156, 84] = 1
    gameState[161, 85] = 1
    gameState[161, 86] = 1
    gameState[161, 87] = 1
    gameState[161, 88] = 1
    gameState[161, 89] = 1
    gameState[162, 75] = 1
    gameState[162, 84] = 1
    gameState[162, 86] = 1
    gameState[162, 87] = 1
    gameState[162, 88] = 1
    gameState[162, 90] = 1
    gameState[163, 75] = 1
    gameState[163, 77] = 1
    gameState[163, 85] = 1
    gameState[163, 89] = 1
    gameState[164, 67] = 1
    gameState[164, 68] = 1
    gameState[164, 75] = 1
    gameState[164, 76] = 1
    gameState[164, 86] = 1
    gameState[164, 87] = 1
    gameState[164, 88] = 1
    gameState[165, 66] = 1
    gameState[165, 67] = 1
    gameState[165, 87] = 1
    gameState[166, 68] = 1
    gameState[171, 75] = 1
    gameState[171, 84] = 1
    gameState[172, 74] = 1
    gameState[172, 75] = 1
    gameState[172, 83] = 1
    gameState[172, 84] = 1
    gameState[172, 85] = 1
    gameState[173, 74] = 1
    gameState[173, 76] = 1
    gameState[173, 82] = 1
    gameState[173, 83] = 1
    gameState[173, 84] = 1
    gameState[173, 85] = 1
    gameState[173, 86] = 1
    gameState[174, 81] = 1
    gameState[174, 83] = 1
    gameState[174, 85] = 1
    gameState[174, 87] = 1
    gameState[175, 81] = 1
    gameState[175, 82] = 1
    gameState[175, 86] = 1
    gameState[175, 87] = 1
    gameState[178, 81] = 1
    gameState[178, 82] = 1
    gameState[179, 81] = 1
    gameState[179, 82] = 1
    gameState[180, 80] = 1
    gameState[181, 80] = 1
    gameState[181, 81] = 1
    gameState[181, 82] = 1
    gameState[182, 84] = 1
    gameState[183, 80] = 1
    gameState[183, 81] = 1
    gameState[183, 82] = 1
    gameState[183, 83] = 1
    gameState[183, 84] = 1
    gameState[184, 82] = 1
    gameState[184, 83] = 1
    gameState[187, 79] = 1
    gameState[187, 80] = 1
    gameState[187, 84] = 1
    gameState[187, 85] = 1
    gameState[188, 80] = 1
    gameState[188, 81] = 1
    gameState[188, 82] = 1
    gameState[188, 83] = 1
    gameState[188, 84] = 1
    gameState[189, 80] = 1
    gameState[189, 81] = 1
    gameState[189, 83] = 1
    gameState[189, 84] = 1
    gameState[190, 80] = 1
    gameState[190, 81] = 1
    gameState[190, 83] = 1
    gameState[190, 84] = 1
    gameState[191, 81] = 1
    gameState[191, 82] = 1
    gameState[191, 83] = 1
    gameState[197, 81] = 1
    gameState[197, 82] = 1
    gameState[198, 81] = 1
    gameState[198, 82] = 1

    return gameState