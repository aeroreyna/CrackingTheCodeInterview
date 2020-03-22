def replace_space(url, l):
    count = 0
    for i in range(l):
        count += url[i] == " "
    for i in range(l):
        j = l-i-1
        if url[j] != " ":
            url[j + count*2] = url[j]
        else:
            url[j + count*2] = "0"
            url[j + count*2-1] = "2"
            url[j + count*2-2] = "%"
            count -= 1
    return url

if __name__ == '__main__':
    print(replace_space(list("I am I               "), 6))
