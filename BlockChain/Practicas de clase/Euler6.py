def main():
    squareNum = 0
    sumsquareNum = 0
    for i in range(1, 101):
        squareNum += pow(i,2)
        sumsquareNum += i
    sumsquareNum = pow(sumsquareNum,2)
    res = sumsquareNum - squareNum
    print(f' Square of 100: {squareNum}\n Square of the sum of the first 100 numbers: {sumsquareNum}\n Difference between both: {res}')
    
if __name__ == "__main__":
    main()