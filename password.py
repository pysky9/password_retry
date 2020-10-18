# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出登入成功
# 如果不正確 就印出 "密碼錯誤!還有__次機會"

password = 'a123456'
i = 1
while i < 4:
	pwd = input("請輸入密碼: ")
	if pwd == password:
		print("登入成功")
		break
	else :
		times = 3 - i
		if times == 0:
			break
		else:
			print(f"密碼錯誤!還有{times}次機會")
		i += 1
		if i == 4 :
			break
