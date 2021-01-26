from net import game 
net=game()
net.isserver=bool(input("Am I Server ?"))
if net.isserver:
    net.serve()
else:
    net.connect()
    net.sendsrv()
    