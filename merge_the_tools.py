def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique_substring = ""
        for char in substring:
            if char not in unique_substring:
                unique_substring += char
        print(unique_substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)