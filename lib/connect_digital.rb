require "droplet_kit"
token = "9cde07388f468b8d10dfc7db444a97c000f85fc7aa3f3048ae3ad13eed8a65e0"
client = DropletKit::Client.new(access_token: token)
puts client.account.info
