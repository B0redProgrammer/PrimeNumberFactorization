nums = []
for i in range(2, 10000):
	nums.append(i)
	
for num in nums:
	count = 2
	
	while num*count < 10000:
		if num*count in nums:
			nums.remove(num*count)
		count += 1
		

files = []		
for i in range(1, 10):
	files.append(open("{}.txt".format(i), "w"))
	
for num in nums:
	last_digit = str(num)[len(str(num))-1]
	print(int(last_digit)-1)
	files[int(last_digit)-1].write(str(num)+"\n")
	
for file in files:
	file.close()
	
File = open("calc_nums.txt", "w")
for i in range(1, 10):
	for j in range(1, 10):
		File.write("{} {} {}\n".format(i, j, i*j))
		
File.close()
