from asyncore import write
from settings import *
import pygame
import os
import sys
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image, ImageChops, ImageEnhance, ImageOps #llama a las imagenes
import math # librerias matematica
import math
import csv
import numpy as np
from map import collision_walls
from ray_casting import *



#matrix_q = np.zeros((17, 17), int)
matrix_q = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]


class Player:

    def __init__(self):

        self.arrayPath = []
        self.x, self.y = player_pos   ##### 
        self.sumaPasos=0
        #self.niño = 1
        
        self.posicion_previa_x = int(self.x/100)
        self.posicion_previa_y = int(self.y/100)
    
    

        self.angle = player_angle
        self.sensitivity = 0.004
        
        # collision parameters
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.collision_list = collision_walls

    @property
    def pos(self):
        return (self.x, self.y)  #######

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_list)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        
        self.posicion_previa_x = int(self.x/100)
        self.posicion_previa_y = int(self.y/100)

        self.x += dx
        self.y += dy

        

        ##print(self.x, self.y)
        index_x = int(self.x/100)   #8
        index_y = int(self.y/100)   #15

        self.cambio(index_x,index_y,self.posicion_previa_x,self.posicion_previa_y)

        #matrix_q[index_x][index_y] +=1    #matrix[8][15] +=1
        #print("......")
        #print(self.posicion_previa_x,self.posicion_previa_y)

         
        #print(index_x,index_y)
        
            #print(m)

    def movement(self):
        self.keys_control()
        #self.mouse_control()
        self.rect.center = self.x, self.y
        #self.angle %= DOUBLE_PI

    
    
    def cambio(self,index_x,index_y,posicion_previa_x,posicion_previa_y):

        if (index_x != posicion_previa_x ):
            matrix_q[index_y][index_x] +=1  
            self.arrayPath.append((index_y,index_x))
            
           
        if (index_y != posicion_previa_y ):
            matrix_q[index_y][index_x] +=1  
            self.arrayPath.append((index_y,index_x))    

        

    



    def keys_control(self):

        #movematrix[16][16]=[]
        #index_x = posx//100
        #index_y = posy//100

        
        #new[index][index_y] += 1
        
        
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_p]:

            ventana = Tk()
            ventana.title("Datos del Jugador")
            #ventana.geometry("630x450")
            ventana.geometry("280x220")
            

            L1=Label(ventana,text="Numero de Jugador: ")  #Label -> la parte escrita 
            L1.place(x=8,y=8)
            E1=Entry(ventana)                       #Entry -> la parte de los cuadros
            E1.place(x=135,y=8)

            L2=Label(ventana,text="Nombre del Jugador: ")  #Label -> la parte escrita 
            L2.place(x=8,y=50)
            E2=Entry(ventana)                       #Entry -> la parte de los cuadros
            E2.place(x=135,y=50)

            L3=Label(ventana,text="Edad del Jugador: ")  #Label -> la parte escrita 
            L3.place(x=8,y=90)
            E3=Entry(ventana)                       #Entry -> la parte de los cuadros
            E3.place(x=135,y=90)
            ventana['bg'] = '#49A'

            def ingresoDatos():
                numeroJ = E1.get()
                nombreJ = E2.get()
                edadJ = E3.get()
                nombrePlayer = 'C:/Users/carlo/OneDrive/Escritorio/Proy. Titulacion/Maze/juego.main/datos/jugador'+numeroJ+'.txt'
                f = open (nombrePlayer,'w') #concatenar  #concatenar 
                #writer = csv.writer(f)
                f.write('Proyecto de Titulacion - Universidad Yachay Tech \n')
                #//escuela = 'Escuela Urcuqui' + '\n'
                #f.write(escuela )
                nombre = 'Nombre del Jugador: ' + nombreJ +'\n'
                edad = 'Edad del jugador: ' + edadJ + '\n'
                f.write(nombre)
                f.write(edad)

                f.write("................Datos de Exploracion...............\n")
                self.sumaPasos = sum([sum(row)for row in matrix_q])            
                sumaT= "\n"+ 'Los movimientos dados = ' + str(self.sumaPasos) +'\n'
                print(sumaT)
                f.write(sumaT)
                paso = self.arrayPath
                print(paso)
                a=str(paso)
                f.write("\n"+"Path " +"\n"+ a + "\n")
                
                #f.write(a)
                #for p in paso:
                    #writer.writerow(p)

                #f.write("....................FIN.....................................\n")
                f.close()

            def newplayer():
                self.sumaPasos = 0
                self.x, self.y = player_pos 
                self.arrayPath = []
                for i in range(len(matrix_q)):
                    for j in range(len(matrix_q)):
                        matrix_q[i][j] = 0
                ventana.quit()
                ventana.destroy()                
            
            B1=Button(ventana, text="Guardar" , command= ingresoDatos)
            B1.place(x=50,y=150)
            B2=Button(ventana, text="Nuevo Jugador" ,  command=newplayer)
            B2.place(x=155 ,y=150)

           




            #print(numeroJ,nombreJ,edadJ)
            
            ventana.mainloop()
            #crear una Variable para player si no funciona la concatenacion 
            #niño = input("Ingrese numero de Jugador: ")
            #jugadorMaze="jugador{}".format(self.niño)#
            
            #f.write(".........................................................\n")

            #nom = input("Ingrese su Nombre: ")
            #ed = input ("Cuantos años tiene: ")
           

            
            #leer con dos for y un tab 

            #for m in matrix_q:
                #print(m)
         
            

            #f.write(self.arrayPath)
            
        if keys[pygame.K_END]:


            self.sumaPasos = 0
            self.x, self.y = player_pos 
            self.arrayPath = []
            for i in range(len(matrix_q)):
                for j in range(len(matrix_q)):
                    matrix_q[i][j] = 0
            #matrix_q=[]
             


        if keys[pygame.K_UP]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
            self.detect_collision(dx, dy)

            #print("valor x", dx, "valor y",dy)


        if keys[pygame.K_DOWN]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            self.detect_collision(dx, dy)


        if keys[pygame.K_LEFT]:
            self.angle -= 0.01 # 0.13

        if keys[pygame.K_RIGHT]:
            self.angle += 0.01






