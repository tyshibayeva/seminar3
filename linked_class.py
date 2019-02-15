from linked_list import MyList, ListNode

class Queue:
	def __init__(self):
		self.my_queue = MyList()
		
	def length(self):
		return self.my_queue.__len__()
		
	def isEmpty(self):
		if self.length() == 0:
			return True
		return False
		
	def dequeue(self):
		if not self.isEmpty():
			count = 0
			for elem in self.my_queue:
				count += 1
				if count == self.length():
					data = elem
					
			self.my_queue.remove(data)	
			return data
				
		print("The stack contains no items!")
		return ""
			
		
	def enqueue(self, item):
		elem =  ListNode(item)
		self.my_queue.add(elem)
