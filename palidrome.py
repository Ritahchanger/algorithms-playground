# Unique Length-3 Palindromic Subsequences
def count_palindromic_subsequences(s):
    n = len(s)
    palindromes = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if s[i] == s[k]:
                    palindrome = s[i] + s[j] + s[k]
                    palindromes.add(palindrome)
    return len(palindromes), palindromes
input_string = "abca"
count, palindromic_subsequences = count_palindromic_subsequences(input_string)
print(f"Number of unique length-3 palindromic subsequences: {count}")
print("Palindromic Subsequences:", palindromic_subsequences)
