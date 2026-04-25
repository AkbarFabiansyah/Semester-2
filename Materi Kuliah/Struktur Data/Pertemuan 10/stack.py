class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
#methode is_empty
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

#methode push untuk menambahkan data ke stack
    def push(self, data):
        new_node = node(data)
        new_node.next = self.top
        self.top = new_node

#methode pop untuk menghapus data teratas dan mengembalikan nilainya
    def pop(self):
        if self.top is None:
            print("Stack kosong")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
#methode peek untuk melihat data teratas tanpa menghapusnya
    def peek(self):
        if self.top is None:
            print("Stack kosong")
            return None
        return self.top.data
#mwthode display untuk menampilkan isi stack
    def display(self):
        if self.is_empty():
            print("stack kosong")
            return
        current = self.top
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes) + " -> none")
        
#contoh penggunaan
mystack  = stack()
print (mystack.is_empty())
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.display()
print(mystack.peek())
print(mystack.pop())
print(mystack.peek())
mystack.display()   