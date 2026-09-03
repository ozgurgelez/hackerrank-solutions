def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    lines = []
    
    for i in range(size):
        left = [alphabet[size - 1 - j] for j in range(i)]
        center = alphabet[size - 1 - i]
        right = left[::-1]
        
        row_str = "-".join(left + [center] + right)
        lines.append(row_str.center(width, "-"))
    
    full_pattern = lines + lines[:-1][::-1]
    print("\n".join(full_pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)