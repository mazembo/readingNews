require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2016-08-11.yml"))
user_token = access_token["user_token"]
page_token = access_token["page_token"]

@graph_page = Koala::Facebook::API.new(page_token)
@articles.each do |article|
     @graph_page.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]})
end

@graph = Koala::Facebook::API.new(user_token)
@articles.each do |article|
    @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]})
end
