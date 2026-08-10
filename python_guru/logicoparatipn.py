#And,OR,NOT

math=20
science=15

print(math>10 and science>10) #True
print(math>10 or science>10) #True
print(not math>10) 
print(not(math>10 and science>10)) #False

print(math>10 and science<10) #True
print(math<10 or science>10) #True
print(not(math>10 and science>10)) #False