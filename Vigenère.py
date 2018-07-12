import string 					#알파벳 대문자를 모아놓은 문자열을 얻기위해서 호출

def make_dict():				#알파벳:숫자 로 이루어진 딕셔너리 Alpha_dict와 그반대로 숫자:알파벳으로 이루어진 딕셔너리 Number_dict를 생성하는 함수
	Alpha_dict = {}
	Number_dict = {}
	for x in range(26):
		Alpha_dict[chr(65+x)] = x
		Number_dict[x] = chr(65+x)
	return Alpha_dict,Number_dict	

def enc(plaintext,keyword):		#암호화 함수, 암호문을 리턴
	Alpha_dict,Number_dict = make_dict()
	ciphered = '' 				#암호문을 저장할 문자열
	y = 0						#비느제르표에 영어만 있어서 평문에서 영어만 암호화되도록하고 영어가아닌 문자들은 암호화를 진행x

	for x in plaintext:
		if x not in string.ascii_uppercase:
			ciphered += x
			continue
		
		ciphered += Number_dict[(Alpha_dict[x] + Alpha_dict[keyword[y%len(keyword)]])%26]
		y += 1
	return ciphered
	
def dec(ciphered,keyword):		#복호화를 담당하는 함수, 암호문을 복호화 한 결과를 리턴
	Alpha_dict,Number_dict = make_dict()
	deciphered = ''				#복호화된 결과를 받아줄 빈문자열 선언
	y =0
	
	for x in ciphered:
		if x not in string.ascii_uppercase:
			deciphered += x
			continue
		deciphered += Number_dict[(Alpha_dict[x] - Alpha_dict[keyword[y%len(keyword)]])%26]
		y += 1
	return deciphered
		
	
	
	
def main():
	plaintext = input("input palintext :")
	plaintext = plaintext.upper()#입력받은 평문을 대문자로 바꿔주는 과정

	keyword = input("input keyword :")
	keyword = keyword.upper()
	
	ciphered = enc(plaintext,keyword)
	deciphered = dec(ciphered,keyword)
	
	print('ORIGINAL:\t%s'%plaintext)		
	print('CIPHERED:\t%s'%ciphered)
	print('DECIPHERED:\t%s'%deciphered)


if __name__ == '__main__':
	main()