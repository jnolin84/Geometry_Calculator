#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:36:34 2021

@author: jeremy
"""
#Rectangle Class
class Rectangle():
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    #perimeter function
    def perimeter(self):
        return self.length1 + self.length1 + self.length2 + self.length2

    #area function
    def area_rectangle(self):
        return self.length1 * self.length2
    
#Triangle class
class Triangle():
    def __init__(self, height, base):
        self.height = height
        self.base = base

    #area function
    def area_triangle(self):
        return 0.5 * self.base * self.height

#CIrcle class
class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    #area function
    def area_circle(self):
        return (self.pi * ((self.radius) ** 2))

    #circumference
    def cir_circumference(self):
        return (2 * self.pi * self.radius)
        

print('Welcome to the Geometry Formula Calculator!')

while True:
    try:
        start = raw_input('Would you like to start? \n(1) yes \n(2) no')
    except ValueError:
        print('Not a valid response')
    else:
        if start == '1':

            shape = raw_input('\nWhich shape would you like to work with? \n(1) Rectangle \n(2) Triangle \n(3) Circle')

    #Rectangle calculator
            if shape == '1':
                print ('\nYou selected a rectangle.')
                print('Select from the following options: ')

        #choose formula from menu
                formula = input('(1) Perimeter \n(2) Area')
                print('\nTwo side lengths are required.')

        #user input for side lengths
                while True:
                    try:
                        length_1 = int(raw_input('Enter length 1: '))
                        break
                    except ValueError:
                        print('You did not enter a valid number.  Try again.')
                while True:
                    try:
                        length_2 = int(raw_input('Enter length 2: '))
                        break
                    except ValueError:
                        print('You did not enter a valid number.  Try again.')


        #instance of rectangle
                rect = Rectangle(length_1, length_2)

        #perimeter
                if formula == 1:
                    per_rect = rect.perimeter()
                    print('The perimeter of the rectangle is ' + str(per_rect))
                elif formula == 2:
                    area_rect = rect.area_rectangle()
                    print('\nThe area of the rectangle is ' + str(area_rect))

            if shape == '2':
                print('\nYou have selected a triangle.')
                print('\nA height and a base are required.')

                while True:
                    try:
                        height = int(raw_input('Enter height: '))
                        break
                    except ValueError:
                        print('You did not enter a valid number.  Try again.')

                while True:
                    try:
                        base = int(raw_input('Enter base: '))
                        break
                    except ValueError:
                        print('You did not enter a valid number.  Try again.')

                tri = Triangle(height, base)
                area_t = tri.area_triangle()
                print('\nThe area of the triangle is ' + str(area_t))

            if shape == '3':
                print('\nYou have selected a circle.')
                print('\nA radius is required.')

                while True:
                    try:
                        radius = int(raw_input('Enter radius: '))
                        break
                    except ValueError:
                        print('You did not enter a valid number.  Try again.')

                circle = Circle(radius)

                formula = raw_input('\n(1) Area \n(2) Circumference')
                if formula == "1":
                    area_circ = circle.area_circle()
                    print('\nThe area of the circle is ' + str(area_circ))
                elif formula == '2':
                    circ_circ = circle.cir_circumference()
                    print('The circumference of the circle is ' + str(circ_circ))

        elif start == '2':
            print('Goodbye')
            break
        else:
            print('You did not select a valid response.')
            print('Try again.')





