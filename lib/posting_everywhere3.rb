require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2017-02-10.yml"))
user_token = access_token["user_token"]
lecongolais = access_token["lecongolais"]

# posting to my page lecongolais.net
@custom_message = "lecongolais.net --Aimez notre page facebook www.facebook.com/lecongolais.net/ --Nous suivre sur Twitter @LecongolaisNet"

# @graph_page = Koala::Facebook::API.new(lecongolais)
# @articles.each do |article|
#   begin
#      short_message = article[1]["tweet_message"] + " " + @custom_message
#      @graph_page.put_picture("#{article[1]["picture"]}", {:message => short_message})
#   rescue
#     puts "There was a problem trying to post to the Lecongolais Page"
#     exit
#   end
# end
# puts "Successfully posted to the Lecongolais Page"
# # #posting to my profile maz mav
# #
 @graph = Koala::Facebook::API.new(user_token)
# @articles.each do |article|
#   begin
#     short_message = article[1]["tweet_message"] + " " + @custom_message
#     @graph.put_picture("#{article[1]["picture"]}", {:message => short_message})
#   rescue
#     puts "There was an error trying to post to maz mav timeline"
#     exit
#   end
# end
# puts "Successfully posted to the Maz Mav Timeline"

#posting to my groups
#here are my groups:
#@groups1 = ["1403814586528158","1419902181603029", "1651431211749292", "150076661761567"]
#@groups2 = ["129291017177108", "438378432950495", "126654487476400", "394952713912519"]
#@groups3 = ["381352271995489", "241805262672345", "430118960425259", "1726773537548951" ]
#@groups4 = ["1530763560470990", "230841617013848", "385190645015189", "1726773537548951" ]
#@groups5 = ["275804219283723", "507394756121592", "1601694110080719", "184531028414513"]
#@groups6 = ["768847873176770", "1551810621756122", "598150520219330", "251920001492480"]
#@groups7 = ["1608364782756689", "1324206717608472", "431778150305957", "441164396039365"]
#@groups8 = ["1644785879098263", "1676075629346572", "1173734575975580"]

# group error: "1173734575975580", "441164396039365","1651431211749292", "385190645015189"

# I initialize arrays with groups' numbers

# @groups1 = ["1403814586528158","1419902181603029" ]
# @groups2 = ["129291017177108", "438378432950495", "126654487476400", "394952713912519"]
# @groups3 = ["381352271995489", "241805262672345", "430118960425259", "1726773537548951" ]
# @groups4 = ["1530763560470990", "230841617013848"]
# @groups5 = ["275804219283723", "507394756121592", "184531028414513", "1726773537548951"]
# @groups6 = ["768847873176770", "1551810621756122", "598150520219330"]
# @groups7 = ["1608364782756689", "1324206717608472", "1631475210474977"]
# @groups8 = [ "1676075629346572", "150076661761567"]
# @groups9 = ["919465771505711", "1631475210474977", "251920001492480"]
#
# # groups generating errors when posting: ["1644785879098263",1601694110080719, , "251920001492480"]
#
@groups1 = ["1403814586528158","1419902181603029"]
@groups2 = ["129291017177108", "126654487476400"]
@groups3 = [ "241805262672345", "430118960425259", "275804219283723" ]
@groups4 = ["1530763560470990", "230841617013848"]
@groups5 = [ "381352271995489", "507394756121592", "184531028414513"]
@groups6 = ["1601694110080719", "598150520219330"]
@groups7 = ["1608364782756689", "1324206717608472", "1631475210474977"]
@groups8 = [ "1676075629346572", "1726773537548951"]
@groups9 = ["150076661761567", "394952713912519", "919465771505711"]

# @groups1.each do |group|
#   @articles.each do |article|
#     begin
#       short_message = article[1]["tweet_message"] + " " + @custom_message
#       @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups1"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups1 Collection"
# sleep 180
# @groups2.each do |group|
#   @articles.each do |article|
#     begin
#       short_message = article[1]["tweet_message"] + " " + @custom_message
#       @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups2"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups2 Collection"
# sleep 180
@groups3.each do |group|
  @articles.each do |article|
    begin
      short_message = article[1]["tweet_message"] + " " + @custom_message
      @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups3"
      exit
    end
  end
end
puts "Successfully Posted to the @groups3 Collection"
sleep 180

@groups4.each do |group|
  @articles.each do |article|
    begin
      short_message = article[1]["tweet_message"] + " " + @custom_message
      @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups4"
      exit
    end
  end
end
puts "Successfully Posted to the @groups4 Collection"
sleep 180

@groups5.each do |group|
  @articles.each do |article|
    begin
      short_message = article[1]["tweet_message"] + " " + @custom_message
      @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups5"
      exit
    end
  end
end
puts "Successfully Posted to the @groups5 Collection"
sleep 180

@groups6.each do |group|
  @articles.each do |article|
    begin
      short_message = article[1]["tweet_message"] + " " + @custom_message
      @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups6"
      exit
    end
  end
end
puts "Successfully Posted to the @groups6 Collection"
sleep 180

@groups7.each do |group|
  @articles.each do |article|
    # begin
      short_message = article[1]["tweet_message"] + " " + @custom_message
      @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
    # rescue
    #   puts "There was an error while posting to the group #{group} of the collection @groups7"
    #   exit
    # end
  end
end
puts "Successfully Posted to the @groups7 Collection"
sleep 180
@groups8.each do |group|
  @articles.each do |article|
    begin
      short_message = article[1]["tweet_message"] + " " + @custom_message
      @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups8"
      exit
    end
  end
end
puts "Successfully Posted to the @groups8 Collection"
sleep 180
@groups9.each do |group|
  @articles.each do |article|
    begin
      short_message = article[1]["tweet_message"] + " " + @custom_message
      @graph.put_picture("#{article[1]["picture"]}", {:message => short_message}, "#{group}")
    rescue
      puts "There was an error while posting to the group #{group} of the collection @groups9"
      exit
    end
  end
end
puts "Successfully Posted to the @groups9 Collection"
puts "Congratulations! Everything has been posted in all the groups"
