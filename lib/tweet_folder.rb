require "twitter"
#@articles = YAML.load(File.read("2016-07-19.yml"))

# Client for lecongolais.net

@client_lecongolais = Twitter::REST::Client.new do |config|
  config.consumer_key        = "hF5tiIO8uRHa7qPWdVEmAoMMv"
  config.consumer_secret     = "uskmD4n5SWXNYaXwq1RksDzLG8v2vwLbGVodymNkXqEbowFzw6"
  config.access_token        = "3190485058-AuMa7qDLvJIFKqahsCNS5buZKYthMklTZUVmxtY"
  config.access_token_secret = "7ihVPRU3xXIYYFvlYvZAUl7SCthocIm7g34lv7ibXaL8U"
end

#client for Dr Mazembo Mavungu account

@client_mazembo = Twitter::REST::Client.new do |config|
  config.consumer_key        = "pjq2CgyrFUMNNBx7V6UIUFZnI"
  config.consumer_secret     = "dcaoqVVV53qgD3ag50e82qfGRzBdevTPeZ6pkVAnC9PfoXljE7"
  config.access_token        = "69027768-a7dk65Qedsaad0JKEUtMmJAVuaeaN81YMFNC1FuYx"
  config.access_token_secret = "r0EX0CJLK1Um5BuX5e5f6pO09v5vFeEKZXUi0SsC4QZJ2"
end

@message = "#RDC: Les tweets du jour: Lundi 23 Janvier 2017 (suite) http://lecongolais.net/?p=3006"
Dir.foreach("/home/mavungu/Lecongolais.net/facebook/images/2017-01-23-2") do |fname|
  next if fname == '.' or fname == '..'
  @client_lecongolais.update_with_media(@message, File.new(fname))
  @client_mazembo.update_with_media(@message, File.new(fname))
end
