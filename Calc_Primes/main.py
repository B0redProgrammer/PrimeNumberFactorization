nums = []
for i in range(2, 1000000):
	nums.append(i)
	if i % 100000 == 0:
		print(i)
	
for num in nums:
	count = 2
	
	while num*count < 1000000:
		if num*count in nums:
			nums.remove(num*count)
		if count % 100000 == 0:
			print(count)
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
