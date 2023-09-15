# for _ in range(3):
#     print("#")

def main():
#     print_column(3)
# 
# def print_column(height):
# #     for _ in range(height):
# #         print("#")
#     print("#\n" * height, end="")

#     print_row(4)
# 
# def print_row(width):
#     print("?"*width)

    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
