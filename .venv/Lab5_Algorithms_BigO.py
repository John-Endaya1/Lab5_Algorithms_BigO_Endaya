def get_inputs():
    last_name = input("Enter LAST_NAME: ").strip().upper() or "STUDENT"
    artist = input("Enter FAVORITE_ARTIST: ").strip().upper() or "ARTIST"
    try:
        seed_num = int(input("Enter SEED_NUM (integer): "))
    except ValueError:
        seed_num = 123
        print("Invalid SEED_NUM; using 123.")
    try:
        seed_digit = int(input("Enter SEED_DIGIT (0-9): "))
    except ValueError:
        seed_digit = abs(seed_num) % 10
    try:
        id_sum = int(input("Enter ID_SUM (integer): "))
    except ValueError:
        id_sum = sum(map(int, str(abs(seed_num))))
    return last_name, artist, seed_num, seed_digit, id_sum


def heading(title):
    print("\\n" + "=" * 72)
    print(title)
    print("=" * 72)


# EXERCISE 1: LINEAR SEARCH
def linear_search(data, target):
    comparisons = 0
    for i, value in enumerate(data):
        comparisons += 1
        if value == target:
            return i, comparisons
    return -1, comparisons


def exercise_one(last_name, artist, seed_num):
    heading("1. LINEAR SEARCH ANALYZER")
    artist_code = sum(ord(c) for c in artist if c.isalpha())
    data = [seed_num + artist_code % 13 + i * 3 for i in range(10)]
    data.insert(4, data[1])
    print("Generated dataset:", data)
    for label, target in [("Existing target", data[-1]), ("Missing target", max(data) + 999)]:
        index, comparisons = linear_search(data, target)
        print(f"\\n{label}: {target}")
        print("Result:", f"found at index {index}" if index >= 0 else "not found")
        print("Comparison count:", comparisons)
    print("\\nComplexity analysis:")
    print("Best case: O(1); average case: O(n); worst case: O(n).")
    print("Time complexity: O(n); auxiliary space: O(1).")
    print("Final Output: Linear search results and comparison counts displayed.")


# EXERCISE 2: MERGE SORTED ENROLLMENT DATASETS
def merge_sorted(a, b):
    i = j = comparisons = 0
    merged = []
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, comparisons


def exercise_two(last_name, artist, seed_digit, id_sum):
    heading("2. UNIVERSITY ENROLLMENT RECORDS")
    a_base = abs(id_sum) + abs(seed_digit) * 10
    dataset_a = sorted([a_base + x for x in (3, 8, 13, 18, 23)])
    b_base = len(artist.replace(" ", "")) * 10 + len(last_name)
    dataset_b = sorted([b_base + x for x in (1, 6, 11, 16, 21)])
    merged, comparisons = merge_sorted(dataset_a, dataset_b)
    print("Department A dataset:", dataset_a)
    print("Department B dataset:", dataset_b)
    print("Consolidated dataset:", merged)
    print("Records before consolidation:", len(dataset_a) + len(dataset_b))
    print("Records after consolidation:", len(merged))
    print("Comparison count:", comparisons)
    print("Ordering verified:", merged == sorted(merged))
    print("Record count verified:", len(merged) == len(dataset_a) + len(dataset_b))
    print("Time complexity: O(n + m); auxiliary space: O(n + m).")
    print("Final Output: Sorted enrollment records merged and verified.")


# EXERCISE 3: SORTING ALGORITHM COMPARISON
def bubble_sort(values):
    a = values.copy()
    comparisons = movements = 0
    start = perf_counter()
    for end in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(end):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movements += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, movements, perf_counter() - start


def selection_sort(values):
    a = values.copy()
    comparisons = movements = 0
    start = perf_counter()
    for i in range(len(a) - 1):
        minimum = i
        for j in range(i + 1, len(a)):
            comparisons += 1
            if a[j] < a[minimum]:
                minimum = j
        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
            movements += 1
    return a, comparisons, movements, perf_counter() - start


def insertion_sort(values):
    a = values.copy()
    comparisons = movements = 0
    start = perf_counter()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                movements += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        movements += 1
    return a, comparisons, movements, perf_counter() - start


def exercise_three(last_name, artist, seed_num):
    heading("3. E-COMMERCE ORDER PROCESSING")
    rng = random.Random(seed_num + sum(ord(c) for c in artist if c.isalpha()))
    order_ids = [abs(seed_num) % 500 + len(last_name) * 10 + rng.randint(1, 999)
                 for _ in range(12)]
    conditions = {
        "Sorted": sorted(order_ids),
        "Reverse-ordered": sorted(order_ids, reverse=True),
        "Random": order_ids.copy()
    }
    rng.shuffle(conditions["Random"])
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort)
    ]
    print("Generated order dataset:", order_ids)
    for condition, values in conditions.items():
        print(f"\\n--- {condition} input ---")
        print("Input:", values)
        for name, algorithm in algorithms:
            result, comparisons, movements, elapsed = algorithm(values)
            print(f"{name}:")
            print("  Result:", result)
            print("  Comparisons:", comparisons)
            print("  Movements/shifts:", movements)
            print(f"  Execution time: {elapsed:.8f} seconds")
            print("  Correctly sorted:", result == sorted(values))
    print("\\nBig O analysis:")
    print("Bubble Sort: best O(n) with early stopping; average/worst O(n^2).")
    print("Selection Sort: best/average/worst O(n^2); generally few swaps.")
    print("Insertion Sort: best O(n); average/worst O(n^2).")
    print("Auxiliary space for each implementation: O(1).")
    print("Actual execution times vary by computer and dataset.")
    print("Final Output: Comparisons, movements, execution times, and sorting verification displayed.")


def main():
    heading("LAB 5: ALGORITHMS AND BIG-O")
    last_name, artist, seed_num, seed_digit, id_sum = get_inputs()
    print("\\nStudent-specific inputs:")
    print("LAST_NAME:", last_name)
    print("FAVORITE_ARTIST:", artist)
    print("SEED_NUM:", seed_num)
    print("SEED_DIGIT:", seed_digit)
    print("ID_SUM:", id_sum)
    exercise_one(last_name, artist, seed_num)
    exercise_two(last_name, artist, seed_digit, id_sum)
    exercise_three(last_name, artist, seed_num)
    heading("ALL EXERCISES COMPLETED")


if __name__ == "__main__":
    main()

