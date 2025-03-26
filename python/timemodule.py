import time

epc = time.time()
localtime1 = time.localtime(epc)
print("Current Local Time: ", localtime1)
print("Current Hour: ", localtime1.tm_hour)
