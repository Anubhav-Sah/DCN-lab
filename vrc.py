def sender(data):
    onces=data.count('1')

    print("Data is shared successfull")

    if onces%2==0:
        return data+"0"
    else:
        return data+"1"
    
def reciver(data):
    print("Data recived...")
    print("Vaidating data...")
    onces= data.count('1')

    if onces%2==0:
        print("Data is original")
    else:
        print("Data is corrupted")
    

data="1010"

reciver(sender(data)+"1")