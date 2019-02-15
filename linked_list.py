from mylistiterator import MyListIterator

class MyList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def __contains__(self,target):
		curNode = self.head
		while (curNode is not None) and \
		(curNode.data!=target):
			curNode = curNode.next

		return curNode is not None

	def add(self, item):
		assert item != None
		item.next = self.head
		self.head = item
		self.size += 1 
     
	def remove(self, target):
		predNode = None
		curNode = self.head
		while (curNode is not None) and \
		(curNode.data != target):
			predNode = curNode
			curNode = curNode.next

		if curNode is not None:
			self.size -= 1 
			if curNode is self.head:
				self.head = curNode.next
			else:
				predNode.next = curNode.next
  
	def search(self, target):
		curNode = self.head
		while (curNode is not None) and \
		(curNode.data!=target):
			curNode = curNode.next

		return curNode 

	def __iter__(self):
		return MyListIterator(self.head)
		



class ListNode:
	def __init__(self, data=None):
		self.data = data 
		self.next = None
		
	def get_data(self):
		return self.data
		
      




