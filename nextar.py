def longest_common_substring(str1, str2):
    # Создаем двумерный массив для хранения длин общих подстрок
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Переменные для хранения длины и позиции наибольшей общей подстроки
    longest_len = 0
    end_pos = 0

    # Заполняем dp-таблицу
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_len:
                    longest_len = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0

    # Извлекаем наибольшую общую подстроку
    start_pos = end_pos - longest_len
    return str1[start_pos:end_pos]

# Пример использования
str1 = "abcdfghijk"
str2 = "abdfghiabc"
result = longest_common_substring(str1, str2)
print("Наибольшая общая подстрока:", result)
