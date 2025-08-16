import os, sys
main = Mr_Code().Main()
try:
    __import__("TEX").main()
except Exception as e:
    exit(str(e))
