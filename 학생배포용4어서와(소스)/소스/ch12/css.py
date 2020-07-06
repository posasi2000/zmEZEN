# 파일을 연다.
f = open("data.csv", "r")

# 파일 안의 각 줄을 처리한다. 
for line in f.readlines():

    # 공백 문자를 없앤다. 
    line = line.strip()

    # 줄을 출력한다. 
    print(line)

    # 줄을 쉼표로 분리한다. 
    parts = line.split(",")

    # 각 줄의 필드를 출력한다. 
    for part in parts:
        print("   ", part)
