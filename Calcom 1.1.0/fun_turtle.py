from turtle import *
print('This part can draw polygons. Describe your shape...')
sides = int(input('Enter the number of sides: '))
size = int(input('Size of shape (Number from 10 - 125 for best results): '))
colour = input('Color of Shape: ')
def polygon(sides, size, colour):
    pendown()
    color('black', colour)
    begin_fill()
    for i in range(sides):
        forward(size)
        right(360-((sides-2 * 180)/sides)+ 1)
    end_fill()
polygon(sides, size, colour)