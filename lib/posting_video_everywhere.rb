require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2017-02-20-video.yml"))
user_token = access_token["user_token"]
page_token = access_token["lecongolais"]

# posting to my page lecongolais.net
#
@graph_page = Koala::Facebook::API.new(page_token)
@articles.each do |article|
  begin
     @graph_page.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "Lecongolais.net")
  rescue
    puts "There was a problem trying to post to the Lecongolais Page"
    exit
  end
end
puts "Successfully posted to the Lecongolais Page"
#posting to my profile maz mav

@graph = Koala::Facebook::API.new(user_token)
@articles.each do |article|
  begin
    @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "me")
  rescue
    puts "There was an error trying to post to maz mav timeline"
    exit
  end
end
puts "Successfully posted to the Maz Mav Timeline"

#posting to my groups
#here are my groups:
# @groups1 = ["1403814586528158","1419902181603029", "1651431211749292"]
# @groups2 = ["129291017177108", "438378432950495", "126654487476400"]
# @groups3 = ["381352271995489", "241805262672345", "430118960425259" ]
# @groups4 = ["1530763560470990", "230841617013848", "385190645015189"]
# @groups5 = ["275804219283723", "507394756121592", "1601694110080719"]
# @groups6 = ["1551810621756122", "598150520219330", "251920001492480"]
# @groups7 = ["1608364782756689", "1324206717608472", "431778150305957"]
# @groups8 = ["1644785879098263", "1676075629346572", "1173734575975580"]
# @groups9 = ["150076661761567", "394952713912519", "1726773537548951"]
# @groups10 = ["1726773537548951", "184531028414513", "441164396039365"

# I initialize arrays with groups' numbers

@groups1 = ["1403814586528158","1419902181603029"]
@groups2 = ["129291017177108", "126654487476400", "241805262672345"]
@groups3 = [ "430118960425259", "275804219283723" ]
@groups4 = ["1530763560470990", "230841617013848", "381352271995489"]
@groups5 = [ "507394756121592", "1601694110080719"]
@groups6 = [ "598150520219330", "251920001492480"]
@groups7 = ["1608364782756689", "1324206717608472", "1631475210474977"]
@groups8 = [ "1676075629346572", "1726773537548951"]
@groups9 = ["150076661761567", "394952713912519", "919465771505711", "184531028414513"]

@groups1.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups1"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups2.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups1"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups3.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups1"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups4.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups1"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups5.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups1"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups6.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups6"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups7.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups7"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups8.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups8"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
sleep 120
@groups9.each do |group|
  @articles.each do |article|
    begin
      @graph.put_video("#{article[1]["video"]}", "#{article[1]["type"]}", {:title => article[1]["title"], :description => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups9"
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection"
puts "Congratulations! Everything has been posted in all the groups"
