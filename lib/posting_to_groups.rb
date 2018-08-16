require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2016-07-12.yml"))
#@groups1 = ["1403814586528158","1419902181603029", "1651431211749292", "150076661761567", "385190645015189"]
#@groups2 = ["129291017177108", "438378432950495", "126654487476400", "394952713912519", "1676075629346572"]
#@groups3 = ["381352271995489", "241805262672345", "430118960425259", "1726773537548951"]
@groups4 = ["1530763560470990", "230841617013848"]
user_token = access_token["user_token"]
page_token = access_token["page_token"]
@graph = Koala::Facebook::API.new(user_token)
@groups4.each do |group|
  @articles.each do |article|
      @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["message"]}, "#{group}")
  end
end


# First posting on my user timeline
#@graph = Koala::Facebook::API.new(user_token)
#  @articles.each do |article|
#    @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["message"]})
#  end
#@graph = Koala::Facebook::API.new(user_token)
#  @articles.each do |article|
#    @graph.put_wall_post("#{article[1]["message"]}", {:picture => "#{article[1]["picture"]}"})
#  end
#
#@graph_page = Koala::Facebook::API.new(page_token)
#  @articles.each do |article|
#    @graph_page.put_picture("#{article[1]["picture"]}", {:message => article[1]["message"]})
#  end
# Secondly posting on my facebook page lecongolais.net
