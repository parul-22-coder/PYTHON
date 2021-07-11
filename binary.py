import pickle
#cars=["BMW","suzuki","audi"]
#with open("cars.pickle",'wb')as  f:
  #  pickle.dump(cars,f)

#with ("cars.pickle",'rb')as f:
#cars2=pickle.load(f)
#print(cars2)
file="cars.pickle"
fileobj=open(file,'rb')
cars=pickle.load(fileobj)
print(cars)