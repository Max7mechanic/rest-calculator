#!/usr/bin/env python
import math


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return -1
    return a / b


def mod(a, b):
    return a % b


def exp(a, b):
    return a ** b


def average(a, b):
    return (a + b) / 2


def log(a, b):
    return math.log(a, b)
