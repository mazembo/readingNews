require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2016-08-11.yml"))
user_token = access_token["user_token"]
page_token = access_token["page_token"]
# First posting on my user timeline
@graph = Koala::Facebook::API.new(user_token)
@articles.each do |article|
    @graph.put_connections("me", "feed", :link => "#{article[1]["link"]}")
end
#Then posting no my page
@graph_page = Koala::Facebook::API.new(page_token)
@articles.each do |article|
   @graph_page.put_connections("Lecongolais.net", "feed", :link => "#{article[1]["link"]}")
end
