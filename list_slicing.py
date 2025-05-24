def list_slicing_demo():
    numbers = list(range(1, 11))
    first_five = numbers[:5]
    reversed_first_five = first_five[::-1]

    print("Extracted list:", first_five)
    print("Reversed extracted list:", reversed_first_five)

if __name__ == "__main__":
    list_slicing_demo()
