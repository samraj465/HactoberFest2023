def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps were made in this pass
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made in this pass, the list is already sorted
        if not swapped:
            break

def main():
    # Input a list of numbers
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        unsorted_list = [int(num) for num in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter a list of numbers.")
        return

    # Call the bubble_sort function to sort the list
    bubble_sort(unsorted_list)

    # Display the sorted list
    print("Sorted List:", unsorted_list)

if __name__ == "__main":
    main()
