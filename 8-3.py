a= int(input("점수 : "))

if a>=0 and a<=100:
  if (a>=90 and a<=100):
    print(a,": A")
  elif (a>=80 and a<=89):
    print(a,": B")
  elif (a>=70 and a<=79):
    print(a,": C")
  elif (a>=60 and a<=69):
    print(a,": D")
  elif (a>=0 and a<=59):
    print(a,": F")
else:
  print("입력 가능한 점수 범위는 0~100입니다.")

        
        

        
