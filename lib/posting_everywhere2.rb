require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2016-09-19.yml"))
user_token = access_token["user_token"]

#posting to my profile maz mav

@graph = Koala::Facebook::API.new(user_token)
@articles.each do |article|
  begin
    @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]})
  rescue
    puts "There was an error trying to post to Lecongolais timeline"
  end
end
puts "successfully posted to the LecongolaisNet timeline"

#posting to my groups
#here are groups of lecongolaisNet:
#uncommon groups with maz mav
#@groups1 = ["323329727829585", "132342043632095", "1676075629346572", "149201935433557" ]

#common groups with maz mav
#@groups2 = [ "1530763560470990", "129291017177108", "1651431211749292", "241805262672345"]
#@groups3 = ["1409238022680428", "381352271995489", "1419902181603029", "438378432950495"]

#I initialize the arrays of groups' numbers

@groups1 = ["323329727829585", "132342043632095", "1676075629346572", "149201935433557" ]
@groups2 = [ "1530763560470990", "129291017177108", "1651431211749292", "241805262672345"]
@groups3 = ["1409238022680428", "381352271995489", "1419902181603029", "438378432950495"]

@groups1.each do |group|
  @articles.each do |article|
    begin
      @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was a problem trying to post to the group #{group} of the collection @groups1 "
      exit
    end
  end
end
puts "Successfully Posted to the @groups1 Collection of LecongolaisNet Account"
sleep 300

@groups2.each do |group|
  @articles.each do |article|
    begin
      @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was a problem trying to post to the group #{group} of the collection @groups1 "
    end
  end
end
puts "Successfully Posted to the @groups2 Collection of LecongolaisNet Account"
sleep 300

@groups3.each do |group|
  @articles.each do |article|
    begin
      @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]}, "#{group}")
    rescue
      puts "There was a problem trying to post to the group #{group} of the collection @groups1 "
    end
  end
end
puts "Successfully Posted to the @groups3 Collection of LecongolaisNet Account"
puts "Congratulations! Everything has been posted in all the groups of LecongolaisNet Account"
