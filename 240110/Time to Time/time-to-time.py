a, b, c, d = input().split()
a, b, c, d = int(a),int(b),int(c),int(d)
hour, mins = a, b
elapsed_time = 0

# while True:
#     if hour == c and mins == d:
#         break
#     elapsed_time += 1
#     mins += 1

#     if mins == 60:
#         hour += 1
#         mins =0
passed = c*60 +d
start = a*60 + b
gap = passed - start 
print(gap)