import random
import time
import matplotlib.pyplot as plt
from typing import List, Callable, Tuple, Dict


def deterministic_quick_sort(arr: List[int]) -> List[int]:
    """
    Deterministyczny algorytm QuickSort, który wykorzystuje środkowy element jako pivot.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def randomized_quick_sort(arr: List[int]) -> List[int]:
    """
    Losowy algorytm QuickSort, który wykorzystuje losowo wybrany element jako pivot.
    """
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def measure_time(sort_function: Callable[[List[int]], List[int]], arr: List[int]) -> float:
    """
    Mierzy czas wykonania funkcji sortującej.
    """
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time


def compare_quick_sorts() -> Tuple[List[int], Dict[str, List[float]]]:
    """
    Porównuje działanie losowego i deterministycznego QuickSort.
    """
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = {"deterministic": [], "randomized": []}

    for size in sizes:
        arr = [random.randint(1, 1_000_000) for _ in range(size)]

        # Pomiar czasu dla deterministycznego QuickSort
        det_times = [measure_time(deterministic_quick_sort, arr.copy()) for _ in range(5)]
        det_avg_time = sum(det_times) / len(det_times)
        results["deterministic"].append(det_avg_time)

        # Pomiar czasu dla losowego QuickSort
        rand_times = [measure_time(randomized_quick_sort, arr.copy()) for _ in range(5)]
        rand_avg_time = sum(rand_times) / len(rand_times)
        results["randomized"].append(rand_avg_time)

        print(f"\nRozmiar tablicy: {size}")
        print(f"   Losowy QuickSort: {rand_avg_time:.4f} sekund")
        print(f"   Deterministyczny QuickSort: {det_avg_time:.4f} sekund")

    return sizes, results


def plot_results(sizes: List[int], results: Dict[str, List[float]]) -> None:
    """
    Rysuje wykres wydajności QuickSort.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results["randomized"], label="Losowy QuickSort", marker="o")
    plt.plot(sizes, results["deterministic"], label="Deterministyczny QuickSort", marker="o")
    plt.title("Porównanie losowego i deterministycznego QuickSort")
    plt.xlabel("Rozmiar tablicy")
    plt.ylabel("Średni czas wykonania (sekundy)")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    sizes, results = compare_quick_sorts()
    plot_results(sizes, results)
