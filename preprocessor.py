def encodeChestPain(binIndex,length=4):

    chestArr = [0]*length
    chestArr[binIndex] = 1
    return chestArr

def encodeEcg(binIndex,length=3):

    ecgArr = [0]*length
    ecgArr[binIndex]= 1
    return ecgArr

def encodeSt(binIndex,length=3):

    stArr = [0]*length
    stArr[binIndex] = 1
    return stArr

def binAge(age):
    
    if age < 31:
        return 0
    elif age < 34:
        return 1
    elif age < 38:
        return 2
    elif age < 41:
        return 3
    elif age < 44:
        return 4
    elif age < 47:
        return 5
    elif age < 51:
        return 6
    elif age < 54:
        return 7
    elif age < 57:
        return 8
    elif age < 60:
        return 9
    elif age < 64:
        return 10
    elif age < 67:
        return 11
    elif age < 70:
        return 12
    elif age < 74:
        return 13
    else:
        return 14

def encodeAge(binIndex,length=15):

    ageArr = [0]*length
    ageArr[binIndex] = 1
    return ageArr

def encodeChol(chol):

    if chol < 200:
        return 0
    elif chol < 240:
        return 1
    elif chol < 300:
        return 2
    else:
        return 3

def binBp(ecg):

    if ecg < 90:
        return 0
    elif ecg < 120:
        return 1
    elif ecg < 130:
        return 2
    elif ecg < 140:
        return 3
    else:
        return 4

def encodeBp(binIndex,length=5):

    ecgArr = [0]*length
    ecgArr[binIndex] = 1
    return ecgArr

def preprocess(arr1,arr2):

    chestPainEncoded = encodeChestPain(arr2[0])
    arr1.extend(chestPainEncoded)

    ecgEncoded = encodeEcg(arr2[1])
    arr1.extend(ecgEncoded)

    stEncoded = encodeSt(arr2[2])
    arr1.extend(stEncoded)

    ageEncoded = encodeAge(binAge(arr1[0]))
    arr1.extend(ageEncoded)

    cholEncoded = encodeChol(arr2[3])
    arr1.append(cholEncoded)

    bpEncoded = encodeBp(binBp(arr2[4]))
    arr1.extend(bpEncoded)
    
    return arr1


