from myclass import Car 
from linked_list import MyList, ListNode
from linked_class import Queue
car1 = Car()   

car2 = Car()
types = "sedan" 
label = "nissan"
color = "red"
car2.change_inf(types, label, color) 

car3 = Car()
types = "crossover" 
label = "volvo"
color = "white"
car3.change_inf(types, label, color) 

car4 = Car()
types = "crossover" 
label = "jaguar"
color = "white"
car4.change_inf(types, label, color) 

my_Queue = Queue()
print(my_Queue.isEmpty())
my_Queue.enqueue(car1)
my_Queue.enqueue(car2)
my_Queue.enqueue(car3)
my_Queue.enqueue(car4)

print(my_Queue.isEmpty())
print(my_Queue.length())
my_Queue.dequeue().disp_inf()
print(my_Queue.length())
my_Queue.dequeue().disp_inf()



 
