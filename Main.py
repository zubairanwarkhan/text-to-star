# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 23:51:43 2018

@author: Ayesha Khan
"""

#Main

def function_a():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==1 and i>1) or (j==5 and i>1) or (i==3) or (i==1 and (j>1 and j<5))):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()
        
        
          

def function_b():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==3 and j<5) or (i==5 and j<5) or (i==2 and j==1) or (i==4 and j==1) or (i==2 and j==5) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()


                

def function_c():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (i==5) or (j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()


                

def function_d():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==5 and j<5) or (j==1) or (i>1 and i<5 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_e():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==3 and j<5) or (i==5 and j<5) or (i==2 and j==1) or (i==4 and j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()


                

def function_f():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (j==1) or (i==3 and j<5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_g():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (j==1) or (i==5) or (i==3 and j>2) or (i==4 and j>4)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_h():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==1 or j==5) or i==3):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_i():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (i==5) or (j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_j():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (i==5 and j<4) or (j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_k():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==5) or (i==2 and j==4) or (i==3 and j==3) or (i==1 and j==1) or (i==2 and j<2) or (i==3 and j<3) or (i==4 and j==4) or (i==5 and j==5) or (i==4 and j<2) or (i==5 and j<2)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_l():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==5) or (j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_m():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==1 or j==5) or (i==2 and j==4) or (i==2 and j==2) or (i==3 and j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_n():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==1 or j==5) or (i==2 and j==2) or (i==3 and j==3) or (i==4 and j==4)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_o():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1 and j<5) or (j==1 and i>1 and i<5) or (i==5 and j>1 and j<5) or (j==5 and i>1 and i<5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_p():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==3 and j<5) or (i==2 and (j==1 or j==5)) or j==1):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_q():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1 and j<5) or (j==1 and i>1 and i<5) or (i==5 and j>1 and j<5) or (j==5 and i>1 and i<5) or (i==4 and j==4) or (i==5 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_r():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==3 and j<5) or (i==2 and (j==1 or j==5)) or j==1 or (i==4 and j==3) or (i==5 and j==4)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_s():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1) or (i==3 and j<5 and j>1) or (i==5 and j<5) or (i==2 and j==1) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_t():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_u():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==1 and i<5) or (i==5 and j>1 and j<5) or (j==5 and i<5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()



def function_v():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and (j==5 or j==1)) or (i==2 and (j==5 or j==1)) or (i==3 and (j==5 or j==1)) or (i==4 and (j==2 or j==4)) or (i==5 and j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()



def function_w():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==1) or (j==5) or (i==4 and (j==2 or j==4)) or (i==3 and j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_x():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and (j==5 or j==1)) or (i==2 and (j==4 or j==2)) or (i==3 and j==3) or (i==4 and (j==2 or j==4)) or (i==5 and (j==1 or j==5)) ):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_y():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and (j==5 or j==1)) or (i==2 and (j==2 or j==4)) or (i==3 and j==3) or (i==4 and j==3) or (i==5 and j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_z():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (i==5) or (i==2 and j==4) or (i==3 and j==3) or (i==4 and j==2)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_1():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<4) or (j==3) or (i==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_2():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==3 and j==4) or (i==2 and j==5) or (i==4 and j==3) or i==5):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_3():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==3 and j<5 and j>1) or (i==5 and j<5) or (i==2 and j==5) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_4():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==3) or (i==3 and j<5) or (i==2 and j==2)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_5():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j<5) or (i==3 and j<5) or (i==5 and j<5) or (i==2 and j==1) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_6():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1 and j<5) or (i==3 and j<5) or (i==5 and j>1 and j<5) or (i==2 and j==1) or (i==4 and j==1) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()



def function_7():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (i==2 and j==4) or (i==3 and j==3) or (i==4 and j==2) or (i==5 and j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_8():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1 and j<5) or (i==3 and j>1 and j<5) or (i==5 and j>1 and j<5) or (i==2 and j==1) or (i==4 and j==1) or (i==2 and j==5) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_9():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1 and j<5) or (i==3 and j>1) or (i==5 and j<5) or (i==2 and j==1) or (i==2 and j==5) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()


def function_zero():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1 and j<5) or (j==1 and i>1 and i<5) or (i==5 and j>1 and j<5) or (j==5 and i>1 and i<5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()



def function_exclaim():
    
    for i in range (1,6):
        for j in range(1,6):
            if (j==3 and i != 4):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_at():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1) or (i==5 and j<4) or (i==2 and j!=2) or (i==3 and j!=3) or (i==4 and j!=2)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_hash():
    
    for i in range (1,7):
        for j in range(1,7):
            if ((j==2) or (j==5) or (i==2) or (i==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_dollar():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j>1) or (i==3 and j<5 and j>1) or (i==5 and j<5) or (i==2 and j==1) or (i==4 and j==5) or (j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_percent():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==5) or (i==2 and (j==2 or j==4)) or (i==3 and j==3) or (i==4 and (j==2 or j==4)) or (i==5 and j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_power():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==3) or (i==2 and (j==2 or j==4)) or (i==3 and (j==1 or j==5))):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_fslash():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==5) or (i==2 and j==4) or (i==3 and j==3) or (i==4 and j==2) or (i==5 and j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_bslash():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==1) or (i==2 and j==2) or (i==3 and j==3) or (i==4 and j==4) or (i==5 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_plus():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==3) or (j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_minus():
    
    for i in range (1,6):
        for j in range(1,6):
            if (i==3):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_equals():
    
    for i in range (1,6):
        for j in range(1,6):
            if (i==2 or i==4):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_uscore():
    
    for i in range (1,6):
        for j in range(1,6):
            if (i==5):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_astrix():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and (j==5 or j==1)) or (i==2 and (j==4 or j==2)) or (i==3 and j==3) or (i==4 and (j==2 or j==4)) or (i==5 and (j==1 or j==5)) or (j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_sq_br_op():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==1) or (j==2 and (i<2 or i>4))):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_sq_br_clo():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==5) or (j==4 and (i<2 or i>4))):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_parnth_op():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==2 and (i<2 or i>4)) or (i==2 and j==1) or (i==3 and j==1) or (i==4 and j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_parnth_clo():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((j==4 and (i<2 or i>4)) or (i==2 and j==5) or (i==3 and j==5) or (i==4 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_curly_op():
    
    for i in range (1,8):
        for j in range(1,8):
            if ((j==3 and (i<2 or i>6)) or (j==4 and (i<2 or i>6)) or (j==2 and (i==2 or i==3 or i==5 or i==6) or (j==1 and i==4))):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_curly_clo():
    
    for i in range (1,8):
        for j in range(1,8):
            if ((j==3 and (i<2 or i>6)) or (j==4 and (i<2 or i>6)) or (j==5 and (i==2 or i==3 or i==5 or i==6) or (j==6 and i==4))):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_less_than():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==5) or (i==2 and j==4) or (i==3 and j==3) or (i==4 and j==4) or (i==5 and j==5)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_greater_than():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==1) or (i==2 and j==2) or (i==3 and j==3) or (i==4 and j==2) or (i==5 and j==1)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_question():
    
    for i in range (1,8):
        for j in range(1,8):
            if ((i==1 and (j>1 and j<6)) or (i==2 and (j==1 or j==6)) or (i==3 and j==6) or (i==4 and (j==5 or j==4)) or (i==5 and j==4) or (i==7 and j==4)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_fullstop():
    
    for i in range (1,6):
        for j in range(1,6):
            if (i==3 and j==3):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_comma():
    
    for i in range (1,6):
        for j in range(1,6):
            if (((i==1 or i==2) and (j==4 or j==5)) or (i==3 and j==5) or (i==4 and j==4)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_inv_comma_op():
    
    for i in range (1,6):
        for j in range(1,6):
            if (((i==1 or i==2) and (j==1 or j==2)) or (i==3 and j==1) or (i==4 and j==2)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_inv_comma_clo():
    
    for i in range (1,6):
        for j in range(1,6):
            if (((i==1 or i==2) and (j==4 or j==5)) or (i==3 and j==5) or (i==4 and j==4)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_colon():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==2 and j==3) or (i==4 and j==3)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()




def function_semi_colon():
    
    for i in range (1,6):
        for j in range(1,6):
            if ((i==1 and j==3) or (i==3 and j==3) or (i==4 and j==2)):
                print('*', end=" ")
            else: print(" ", end=" ")
        print()
        
        
        
        

user_input = input("Enter your name\n")

f_list = [i for i in user_input]


dict = {"a": function_a, "b": function_b, "c": function_c, "d": function_d, "e": function_e, "f": function_f, "g": function_g, "h": function_h, "i": function_i, "j": function_j, "k": function_k, "l": function_l, "m": function_m, "n": function_n, "o": function_o, "p": function_p, "q": function_q, "r": function_r, "s": function_s, "t": function_t, "u": function_u, "v": function_v, "w": function_w, "x": function_x, "y": function_y, "z": function_z, "1": function_1, "2": function_2, "3": function_3, "4": function_4, "5": function_5, "6": function_6, "7": function_7, "8": function_8, "9": function_9, "0": function_zero, "!": function_exclaim, "@": function_at, "#": function_hash, "$": function_dollar, "%": function_percent, "^": function_power, "*": function_astrix, "(": function_parnth_op, ")": function_parnth_clo, "-": function_minus, "_": function_uscore, "+": function_plus, "=": function_equals, "/": function_bslash, "<": function_less_than, ">": function_greater_than, ".": function_fullstop, ",": function_comma, "?": function_question, ";": function_semi_colon, ":": function_colon, "'": function_inv_comma_op, "&": function_inv_comma_clo, "[": function_sq_br_op, "]": function_sq_br_clo, "{": function_curly_op, "}": function_curly_clo}


    
def mainfunc():
    for i in f_list:
        for j in dict:
            if i is j in dict.keys():
                dict[j]()
                print(sep="")
                
                

mainfunc()
        
"""        
        for c in dict:
                    print("{key}: {function}".format(key=c, function=dict[c]()), end="")
        
"""        