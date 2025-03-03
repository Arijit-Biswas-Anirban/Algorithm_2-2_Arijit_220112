# Lab 08: Tower of Hanoi

def toh(disk, s, h, d):
    if disk == 1:
        print(f"Move Disk {disk} from {s} to {d}")
        return
    toh(disk-1, s, d, h)
    print(f"Move Disk {disk} from {s} to {d}")
    toh(disk-1, h, s, d)

def main():
    disk = int(input("Enter number of Disks: "))
    toh(disk, "source", "help", "destination")
main()