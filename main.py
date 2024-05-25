import os

def main():
    while True:
        print("Choose the interpolation method:")
        print("1. Lagrange")
        print("2. Newton")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            os.system('python interpolation.py lagrange')
        elif choice == '2':
            os.system('python interpolation.py newton')
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue
        
        print("Would you like to choose another method or exit?")
        print("1. Choose another method")
        print("2. Exit")
        next_choice = input("Enter 1 or 2: ")

        if next_choice == '2':
            break

if __name__ == "__main__":
    main()
