require "twitter"
require "yaml"
require "koala"

#puts "write the file name in the format 2018-01-31.yml"
date = Time.new
date_formatted = date.strftime("%Y-%m-%d")
filename = date_formatted + ".yml" 
yaml_folder = "/var/jenkins_home/data/readingNewsCongo/assets/content_yaml_files/"
image_folder = "/var/jenkins_home/data/readingNewsCongo/assets/images/"
full_filename= yaml_folder + filename
@articles = YAML.load(File.read(full_filename, :encoding => 'utf-8'))
@size = @articles.length

# Client for lecongolais.ne

@client_lecongolais = Twitter::REST::Client.new do |config|
  config.consumer_key        = ""
  config.consumer_secret     = ""
  config.access_token        = ""
  config.access_token_secret = ""
end
#
# #client for Dr Mazembo Mavungu account
#
@client_mazembo = Twitter::REST::Client.new do |config|
  config.consumer_key        = "p"
  config.consumer_secret     = "d"
  config.access_token        = ""
  config.access_token_secret = "r"
end
@articles.each do |article|
   begin
        @client_lecongolais.update_with_media("#{article[1]["tweet_message"]}", File.new(image_folder + "#{article[1]["picture"]}"))
   rescue
        puts "there was an error"
	puts "#{article[1]["tweet_message"]}" 
   end
   sleep 5
   begin
        @client_mazembo.update_with_media("#{article[1]["tweet_message"]}", File.new(image_folder + "#{article[1]["picture"]}"))
   rescue
        puts "there was an error"
	puts "#{article[1]["tweet_message"]}"
   end
   sleep 5
end

puts "You have Successfully tweeted a collection of #{@size} tweets"


# Initiating few stuff
# access_token = YAML.load(File.read("access-data.yml"))
# lecongolais = access_token["lecongolais"]
# user_token = access_token["user_token"]
# @graph = Koala::Facebook::API.new(user_token)
# @graph_page = Koala::Facebook::API.new(lecongolais)
# @action = "Aimez notre page https://www.facebook.com/LekongolaisNet/ --Nous suivre sur Twitter https://twitter.com/LecongolaisNet (@LecongolaisNet)"
#
# # posting to my page lecongolais.net
# @articles.each do |article|
#   begin
#      message = article[1]["title"] + "---" + article[1]["short_message"]+ "---" + @action
#      @graph_page.put_picture("#{article[1]["picture"]}", {:message => message })
#   rescue
#     puts "There was a problem trying to post to the Lecongolais Page"
#     exit
#   end
# end
# puts "Successfully posted to the Lecongolais Page"
# @articles.each do |article|
#   begin
#     message = article[1]["title"] + "---" + article[1]["short_message"]+ "---" + @action
#     @graph.put_picture("#{article[1]["picture"]}", {:message => message})
#   rescue
#     puts "There was an error trying to post to maz mav timeline"
#     exit
#   end
# end
# puts "Successfully posted to the Maz Mav Timeline"


# puts "Now wait while we are trying to post them on facebook pages"

# @access_token = YAML.load(File.read("access-data.yml"))
# user_token = @access_token["user_token"]
# lecongolais = @access_token["lecongolais"]
# exetat = @access_token["exetat"]
# dielais = @access_token["dielais"]
# asfade = @access_token["asfade"]
#
# @graph = Koala::Facebook::API.new(user_token)
# @graph_lecongolais = Koala::Facebook::API.new(lecongolais)
# @graph_exetat = Koala::Facebook::API.new(exetat)
# @graph_dielais = Koala::Facebook::API.new(dielais)
# @graph_asfade = Koala::Facebook::API.new(asfade)
#
# @custom_message = "lecongolais.net --Aimez notre page facebook www.facebook.com/lecongolais.net/ --Nous suivre sur Twitter @LecongolaisNet"
#
# # Posting to Mazembo profile
# @articles.each do |article|
#   # begin
#     short_message = article[1]["title"] + "--" + article[1]["short_message"] + " " + @custom_message
#     @graph.put_picture("#{article[1]["picture"]}", {:message => short_message})
#   # rescue
#   #   puts "There was an error trying to post to maz mav timeline"
#   #   exit
#   # end
# end
# puts "Successfully posted to the Maz Mav Timeline"
# sleep 180
#
# # Posting to Lecongolais
# @articles.each do |article|
#   begin
#     short_message = article[1]["title"] + "--" + article[1]["short_message"] + " " + @custom_message
#     @graph_lecongolais.put_picture("#{article[1]["picture"]}", {:message => short_message})
#   rescue
#     puts "There was an error trying to post to lecongolais"
#     exit
#   end
# end
# puts "Successfully posted to lecongolais"
# sleep 180
# # Posting to Exetat
# @articles.each do |article|
#   begin
#     short_message = article[1]["title"] + "--" + article[1]["short_message"] + " " + @custom_message
#     @graph_exetat.put_picture("#{article[1]["picture"]}", {:message => short_message})
#   rescue
#     puts "There was an error trying to post to exetat"
#     exit
#   end
# end
# puts "Successfully exetat"
# sleep 180
# # Posting to dielais
# @articles.each do |article|
#   begin
#     short_message = article[1]["title"] + "--" + article[1]["short_message"] + " " + @custom_message
#     @graph_dielais.put_picture("#{article[1]["picture"]}", {:message => short_message})
#   rescue
#     puts "There was an error trying to post to maz mav timeline"
#     exit
#   end
# end
# puts "Successfully posted to dielais"
# sleep 180
# #Posting to asfade
# @articles.each do |article|
#   begin
#     short_message = article[1]["title"] + "--" + article[1]["short_message"] + " " + @custom_message
#     @graph_asfade.put_picture("#{article[1]["picture"]}", {:message => short_message})
#   rescue
#     puts "There was an error trying to post to maz mav timeline"
#     exit
#   end
# end
# puts "Successfully posted to asfade page"
# puts "Congratulations!!! You have Successfully posted a collection of #{@size} tweets to your facebook pages"
