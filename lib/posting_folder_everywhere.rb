require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@user_token = access_token["user_token"]
@page_token = access_token["page_token"]
@graph = Koala::Facebook::API.new(@user_token)
@graph_page = Koala::Facebook::API.new(@page_token)
@message = "#RDC: Les tweets du jour: Lundi 23 Janvier 2017 (suite) http://lecongolais.net/?p=3006. Aimez notre page www.facebook.com/lecongolais.net/ --Nous suivre sur Twitter www.twitter.com/LecongolaisNet (@LecongolaisNet)"

#getting filenames from the folder
@filenames = []
Dir.foreach('/home/mavungu/Lecongolais.net/facebook/images/2017-01-23-2') do |fname|
  next if fname == '.' or fname == '..'
  @filenames << fname
end

#Posting to my timeline Maz Mav and my page Lecongolais.net
@filenames.each do |filename|
  begin
      @graph.put_picture(filename, {:message => @message})
      @graph_page.put_picture(filename, {:message => @message})
  rescue
    puts "There was an error posting to Maz Mav Timeline or to the page Lecongolais.net"
    exit
  end
end
puts "Successfully posted to Maz Mav and your page Lecongolais.net"

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
#errors: , "1173734575975580"
# I initialize arrays with groups' numbers

@groups1 = ["1403814586528158","1419902181603029"]
@groups2 = ["129291017177108", "126654487476400"]
@groups3 = [ "241805262672345", "430118960425259"]
@groups4 = ["1530763560470990", "230841617013848", "275804219283723" ]
@groups5 = [ "381352271995489", "507394756121592", "184531028414513"]
@groups6 = ["1601694110080719", "598150520219330", "251920001492480"]
@groups7 = ["1608364782756689", "1324206717608472", "1631475210474977"]
@groups8 = [ "1676075629346572", "1726773537548951"]
@groups9 = ["150076661761567", "394952713912519", "919465771505711"]


#groups generating errors when posting: ["1644785879098263",1601694110080719 , "1726773537548951", "1551810621756122", "438378432950495", "441164396039365", , "1651431211749292"]
@groups1.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups1."
sleep 240
@groups2.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups2."
sleep 240
@groups3.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups3."
sleep 240
@groups4.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups4."
sleep 240
@groups5.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups5."
sleep 240
@groups6.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups6."
sleep 240
@groups7.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups7."
sleep 240
@groups8.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups8."
sleep 240
@groups9.each do |group|
  @filenames.each do |filename|
    begin
       @graph.put_picture(filename, {:message => @message}, "#{group}")
    rescue
       puts "There was an error posting to the group: #{group}"
       exit
    end
  end
end
puts "successfully posted all photos of the folder to groups of the collection @groups9."
puts "congratulations! You have successfully posted the entire folder to all the groups"
