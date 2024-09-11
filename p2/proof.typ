= Problema 2

== Link

https://codeforces.com/problemset/problem/1777/F

== Definicion

Se te da un arreglo \(a\) que consiste en \(n\) enteros no negativos.

La "apatía" de un subarreglo $a#sub[l], a#sub[l+1], #sym.dots.h, a#sub[r]  $ se define como

$ max(a#sub[l], a#sub[l+1], #sym.dots.h, a#sub[r]) #sym.xor (a#sub[l] #sym.xor a#sub[l+1] #sym.xor #sym.dots.h #sym.xor a#sub[r]) $

donde $#sym.xor$ denota la operación XOR bit a bit.

Encuentra la apatía máxima entre todos los subarreglos.

== Solucion

