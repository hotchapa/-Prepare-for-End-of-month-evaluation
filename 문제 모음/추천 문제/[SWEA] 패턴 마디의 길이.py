T = int(input())
for tc in range(1, T+1):
    str_list = input()
    word = ""
    for i in str_list:
        word += i
        length = len(word)
        if word == str_list[length:length+length]:
            break

    print(f"#{tc} {len(word)}")
