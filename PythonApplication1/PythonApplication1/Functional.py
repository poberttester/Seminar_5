# 1.  �������� ���������, ��������� �� ������ ��� �����, ���������� ""���"".
def deleteWord(text, keywords):
	afterDeleted = []
	splitedText = text.split(" ")
	for word in splitedText:
		if keywords not in word:
			afterDeleted.append(word)

	# ���������� ������ "afterDeleted" � ������
	return " ".join(afterDeleted)
	


# 4.  ���������� RLE ��������: ���������� ������ ������ � ��������������
# ������.
def encode(data): 
	encoding = '' 
	prev_char = '' 
	count = 1


	for char in data:
	
		if char != prev_char: 
			if prev_char: 
				encoding += str(count) + prev_char 
			count = 1 
			prev_char = char 
		else: 
			count += 1 
	else: 
		encoding += str(count) + prev_char 	
		return encoding

def decode(data): 
 
	decode = '' 
	count = '' 

	for char in data: 
	   if char.isdigit():
	      count += char
	   else:
	     decode += char * int(count)
	     count = " "
		 
	return decode


