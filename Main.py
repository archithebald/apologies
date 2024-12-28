from turtle import *
from time import sleep

class App:
    def __init__(self):
        setup(1280, 720)
        window = Screen()
        window.title("Mes plus plates excuses")
        window.bgcolor("black")
        pensize(10)
        
        pencolor("white")
        
        self.sentence_offset = 90
        
        self.y = 150
        self.x = -280
        
        penup()
        goto(self.x, self.y)
        pendown()
        
        #self.write_d(self.sentence_offset, 0)
        #self.write_e(self.sentence_offset+20, 0)
        #self.write_s(self.sentence_offset, -100)
        #self.write_o(self.sentence_offset, 100)
        #self.write_l(self.sentence_offset-20, 0)
        #self.write_e(self.sentence_offset-500, -150)
        
        #pencolor("#ffc8dd")
        #self.write_e(self.sentence_offset-25, 0)
        #pencolor("#c1121f")
        #self.write_m(self.sentence_offset+35, 0)   
        #pencolor("#f4a261")
        #self.write_i(self.sentence_offset-45, 0)  
        #pencolor("#ffc8dd")
        #self.write_l(self.sentence_offset-20, 0)
        #pencolor("#c1121f")
        #self.write_i(self.sentence_offset-35, 0)
        #pencolor("#f4a261")
        #self.write_e(self.sentence_offset, 0)   
        #pencolor("#ffc8dd")
        #pencolor("white")
        self.write_emoji(self.sentence_offset, 0)
        
        window.mainloop()
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
        goto(self.x, self.y)
    
    def reset(self, x, y):
        penup()
        setheading(0)
        heading()
        self.move(x, y)
    
    def arc_circle(self, times: int, pixel: float, side: str):
        for i in range(times):
            forward(pixel)
            if side == "left":
                left(1)
            else:
                right(1)
    
    def write_d(self, x, y):
        pendown()
        right(90)
        forward(105)
        left(90)
        self.arc_circle(180, .9, "left")
        self.reset(x, y)
    
    def write_e(self, x, y):
        def get_back():
            backward(30)
            right(90)
            
        def go_forward():
            forward(50)
            left(90)
            forward(30)
            
        pendown()
        forward(30)
        penup()
        get_back()
        pendown()
        go_forward()
        penup()
        get_back()
        pendown()
        go_forward()
        
        self.reset(x, y)
    
    def write_s(self, x, y):
        pendown()
        
        left(180)
        
        forward(15)
        self.arc_circle(180, .45, "left")
        self.arc_circle(180, .45, "right")
        forward(20)
        
        self.reset(x, y)

    def write_o(self, x, y):
        pendown()
        
        circle(50)
        
        self.reset(x, y)
    
    def write_l(self, x, y):
        pendown()
        
        right(90)
        forward(100)
        left(90)
        forward(30)
        
        self.reset(x, y)
    
    def write_m(self, x, y):
        pendown()
        
        right(90)
        forward(100)
        backward(100)
        left(50)
        forward(50)
        left(80)
        forward(50)
        right(130)
        forward(100)
        
        self.reset(x, y)  
    
    def write_i(self, x, y):
        pendown()
        
        right(90)
        forward(100)
        left(90)
        forward(10)
        backward(20)
        penup()
        forward(10)
        left(90)
        pendown()
        forward(100)
        left(90)
        forward(10)
        backward(20)
        
        self.reset(x, y)
        
    def write_emoji(self, x, y):
        pendown()
        
        circle(1)
        penup()
        right(90)
        forward(25)
        left(90)
        pendown()
        circle(1)
        
        self.reset(x, y)
        
if __name__ == "__main__":
    App()