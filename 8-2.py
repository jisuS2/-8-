index = input("문자열:")
print("개별 문자 출력 :",index)

def rev(index):
  index_rev ="".join(reversed(index))
  return index_rev
print("역순 개별 문자 출력 :",rev(index))
