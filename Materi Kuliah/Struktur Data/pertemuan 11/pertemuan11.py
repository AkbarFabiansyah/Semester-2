class Queue:
    def __init__(self):
        self.queue = []

    # Fungsi Enqueue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} berhasil ditambahkan ke antrean.")

# Contoh penggunaan
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
