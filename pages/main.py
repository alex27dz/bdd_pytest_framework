def reverse_middle_words():
    N = int(input().strip())
    results = []

    for _ in range(N):
        line = input().strip()
        words = line.split()

        if len(words) > 2:
            result = [words[0]] + words[1:-1][::-1] + [words[-1]]
        else:
            result = words

        results.append(" ".join(result))

    for result in results:
        print(result)


reverse_middle_words()