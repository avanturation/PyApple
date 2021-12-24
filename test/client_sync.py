from pyapple import Client

if __name__ == "__main__":
    client = Client.sync()

    a = client.fetch_device("iPhone12,1")

    print(dir(a))
