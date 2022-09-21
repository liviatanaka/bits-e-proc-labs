#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        # soma.next = (not(a) and b) or (a and not(b))
        soma.next = a ^ b
        carry.next = a & b
    return instances()

'''
@block
def fullAdder(a, b, c, soma, carry):
    @always_comb
    def comb():
        # soma.next = (((not(a) and b) or (a and not(b))) and not(c)) or (not((not(a) and b) or (a and not(b))) and c)
        soma.next = a ^ b ^ c
        carry.next = (a and b) or (a and c) or (b and c)

    return instances()

@block
def fullAdder(a, b, c, soma, carry):
    # s0 = Signal(bool(0))
    # s1 = Signal(bool(0))
    # s2 = Signal(bool(0))
    s = [Signal(bool(0)) for i in range(3)]

    half_1 = halfAdder(a,b,s[0],s[1])
    half_2 = halfAdder(c,s[0],soma,s[2])

    @always_comb
    def comb():
        carry.next = s[1] or s[2]

    return instances()

'''

@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]  


    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()

@block
def adder2bits(x, y, soma, carry):

    c = Signal(bool(0))
    
    half = halfAdder(x[0], y[0], soma[0], c)
    full = fullAdder(x[1],y[1],c, soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):
    n = len(x)
    faList = [None for i in range(n)]
    c = [Signal(bool(0)) for i in range(n)]
    faList[0] = fullAdder(x[0], y[0], 0, soma[0], c[0])

    for i in range(1,n-1):
        faList[i] = fullAdder(x[i], y[i], c[i-1], soma[i], c[i])
    
    faList[n-1] = fullAdder(x[n-1], y[n-1], c[n-2], soma[n-1], carry)


    return instances()

# @block
# def adderModbv(x,y,soma,carry):
#     @always_comb
#     def comb():
#         sum = x + y
#         soma.next = sum
#         if sum > x.max -1:
#             carry.next = 1
#         else:
#             carry.next =0
    
#     return comb
