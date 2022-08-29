class Library ():

    def __init__(self):
        
        self.listof_lendbooks=[]
        self.listofbooks = []
        
        while True:
            book = input("Please enter books name, for stop entering type 'nomore': ")        
            
            if book in self.listofbooks :
                print('This book is already in Library, please enter different book: ')
                
            else:    
                self.listofbooks.append(book)
            self.listofbooks=list(set(self.listofbooks))
            
            if book == '0':
                self.library_name = input("Please enter library name: ")
                self.listofbooks.remove('0')
                break
                
                
    def Displaybook(self):
        print(self.listofbooks) 
        
        
    def Addbook(self):
        
        while True:           
            addbook=input("Please input new books name, for stop entering type 'nomore': ")
            
            if addbook in self.listofbooks :
                print('This book is already in Library, please enter different book: ')
                
            else:    
                self.listofbooks.append(addbook)
                self.listofbooks=list(set(self.listofbooks))
                
            if addbook == '0':
                self.listofbooks.remove('0')
                break   
                
       
     
    def Lendbook(self):      
               
        while True:
            lendbook=input("Please enter your desired book, for stop entering type 'nomore': ")
            if lendbook in self.listofbooks:
                self.listofbooks.remove(lendbook)
                self.listof_lendbooks.append(lendbook)
                
            elif lendbook not in self.listofbooks and lendbook != '0' :
                print("This book isn't avelabile now")    
                
            elif lendbook == '0':
                break    
                
    def Returnbook(self):
        
        while True:
            Returnbook=input("Please enter book name to return , for stop entering type 'nomore': ")
            if Returnbook in self.listof_lendbooks:
                self.listof_lendbooks.remove(Returnbook)
                self.listofbooks.append(Returnbook)
                
            elif Returnbook not in self.listof_lendbooks and Returnbook != '0' :
                print("You don't have this book")    
                
            elif Returnbook == '0':
                break  
        
        