class Library:
    def __init__(self):
        self.namebook = []
    
    def add_book(self): 
        while True:
            choice = input("พิมพ์ Add เพื่อเพิ่มและพิมพ์ Exit เพื่ออก : ")
            if choice == 'Add':
                book = {}
                book['book'] = str(input('ใส่ชื่อหนังสือ : '))
                book['name'] = str(input('ใส่ชื่อผู้แต่ง : '))
                book['page'] = str(input('ใส่จำนวนหน้ากระดาษ : '))
                book['price'] = str(input('ใส่ราคาหนังสือ : '))
                self.namebook.append(book)
            elif choice == 'Exit':
                break
    def show_books(self):
        print('รายชื่อหนังสือในห้องสมุดทั้งหมด : ')
        for show_book in self.namebook:
            print(show_book)
    
    def find_book(self):
        namebook = str(input('ค้นหาชื่อหนังสือ : '))
        i = 0 
        for i in self.namebook:
            if namebook == i['book']:
                print(i)

u1 = Library()
u1.add_book()
u1.show_books()
u1.find_book()