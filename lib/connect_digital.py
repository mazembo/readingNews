import digitalocean
manager = digitalocean.Manager(token="9cde07388f468b8d10dfc7db444a97c000f85fc7aa3f3048ae3ad13eed8a65e0")
my_droplets = manager.get_all_droplets()
account = digitalocean.Account(token="9cde07388f468b8d10dfc7db444a97c000f85fc7aa3f3048ae3ad13eed8a65e0").load()
print my_droplets
print account
