'''
Problem Name: Largest and smallest value from the Addition
Author: Ayushi Rawat
Date: 13-09-2020
'''
n = input()
n = n.split(' ')
n = list(map(int,n))
n.sort()
print(str(n[0]+n[1]+n[2]+n[3])+ " " + str(n[1]+n[2]+n[3]+n[4]))