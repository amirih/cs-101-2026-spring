
def hanoi(n, source, target, helper):
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        hanoi(n - 1, source, helper, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, helper, target, source)


if __name__ == "__main__":
    
    num_disks = 3
    hanoi(num_disks, 'A', 'C', 'B')