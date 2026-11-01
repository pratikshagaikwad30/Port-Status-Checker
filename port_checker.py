
import socket

print("Port Status Checker")
print("-------------------")

target = input("Enter target IP address: ")

print("Target Host:", target)

start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("Invalid port range!")
else:
    print("Port Range:", start_port, "to", end_port)

    print("\nScanning Ports...")
    print("-------------------")

    print(f"\n{'PORT':<10} STATUS")
    print("-------------------")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        try:
            sock.connect((target, port))
            status = "OPEN"

        except ConnectionRefusedError:
            status = "CLOSED"

        except socket.timeout:
            status = "FILTERED"

        except OSError:
            status = "FILTERED"

        finally:
            sock.close()

        print(f"{port:<10} {status}")
