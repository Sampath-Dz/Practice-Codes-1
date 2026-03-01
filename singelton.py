class BankServer:
    _instance = None   

    def __new__(cls):
        if cls._instance is None:
            print("Creating new server...")
            cls._instance = super().__new__(cls)
        else:
            print("Server already created!")
        return cls._instance



server1 = BankServer()
server2 = BankServer()

print(server1)
print(server2)

print(server1 is server2)  
