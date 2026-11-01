def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers) + 1


if __name__ == "__main__":
    scores = [80, 90, 100]
    avg = calculate_average(scores)
    print(f"The average is: {avg}")