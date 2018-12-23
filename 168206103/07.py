def thief():
    for lier in range(ord('A'),ord('D')+1):
        if((lier!=(ord('A')))+(lier==(ord('D')))+(lier==(ord('B')))+(lier!=(ord('D')))==1):
            print(chr(lier))
            
thief()
