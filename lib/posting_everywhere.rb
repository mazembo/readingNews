require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2017-07-05.yml"))
user_token = access_token["user_token"]
lecongolais = access_token["lecongolais"]

# Initiating few stuff
@graph = Koala::Facebook::API.new(user_token)
@graph_page = Koala::Facebook::API.new(lecongolais)
@action = "Aimez notre page https://www.facebook.com/LekongolaisNet/ --Nous suivre sur Twitter https://twitter.com/LecongolaisNet (@LecongolaisNet)"

# posting to my page lecongolais.net
@articles.each do |article|
  begin
     message = article[1]["title"] + "---" + article[1]["short_message"]+ "---" + @action
     @graph_page.put_picture("#{article[1]["picture"]}", {:message => message })
  rescue
    puts "There was a problem trying to post to the Lecongolais Page"
    exit
  end
end
puts "Successfully posted to the Lecongolais Page"
# # #posting to my profile maz mav
# #
#
@articles.each do |article|
  begin
    message = article[1]["title"] + "---" + article[1]["short_message"]+ "---" + @action
    @graph.put_picture("#{article[1]["picture"]}", {:message => message})
  rescue
    puts "There was an error trying to post to maz mav timeline"
    exit
  end
end
puts "Successfully posted to the Maz Mav Timeline"

#posting to my groups
#here are my groups:
# @groups1 = ['150076661761567', '323329727829585', '354893107994110', '369797506556620']
# @groups2 = ['538051876375575', '571082696311181', '652560668222855', '768847873176770']
# @groups3 = ['824889157530719', '886886388051903', '1233372286708235', '1529201294011005']
# @groups4 = ['385190645015189', '945047448946885', '1651431211749292']
# @groups5 = ['639477702914691']
# @groups6 = []
# @groups7 = []
# @groups8 = []

#group error: '824889157530719',

#I initialize arrays with groups' numbers
# @groups1 = ['150076661761567', '323329727829585', '354893107994110']
# @groups2 = ['538051876375575', '571082696311181', '652560668222855']
# @groups3 = [ '824889157530719', '886886388051903']
# @groups4 = ['385190645015189', '945047448946885', '1651431211749292']
# @groups5 = ['639477702914691', '369797506556620', '768847873176770']
# @groups6 = ['1529201294011005']

#
# @groups1.each do |group|
#   @articles.each do |article|
#     begin
#       message = article[1]["title"] + "---" + article[1]["short_message"] + "---" + @action
#       @graph.put_picture("#{article[1]["picture"]}", {:message => message}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups1"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups1 Collection"
# sleep 300
# @groups2.each do |group|
#   @articles.each do |article|
#     begin
#       message = article[1]["title"] + "---" + article[1]["short_message"] + "---" + @action
#       @graph.put_picture("#{article[1]["picture"]}", {:message => message}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups2"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups2 Collection"
# sleep 300
# @groups3.each do |group|
#   @articles.each do |article|
#     # begin
#       message = article[1]["title"] + "---" + article[1]["short_message"] + "---" + @action
#       @graph.put_picture("#{article[1]["picture"]}", {:message => message}, "#{group}")
#     # rescue
#     #   puts "There was an error while posting to the group #{group} of the collection @groups3"
#     #   exit
#     # end
#   end
# end
# puts "Successfully Posted to the @groups3 Collection"
# sleep 300

# @groups4.each do |group|
#   @articles.each do |article|
#     begin
#       message = article[1]["title"] + "---" + article[1]["short_message"]  + "---" + @action
#       @graph.put_picture("#{article[1]["picture"]}", {:message => message}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups4"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups4 Collection"
# sleep 300
#
# @groups5.each do |group|
#   @articles.each do |article|
#     begin
#       message = article[1]["title"] + "---" + article[1]["short_message"] + "---" + @action
#       @graph.put_picture("#{article[1]["picture"]}", {:message => message}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups5"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups5 Collection"
# sleep 300
#
# @groups6.each do |group|
#   @articles.each do |article|
#     begin
#       message = article[1]["title"] + "---" + article[1]["short_message"] + "---" + @action
#       @graph.put_picture("#{article[1]["picture"]}", {:message => message}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups6"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups6 Collection"
#sleep 180

# @groups7.each do |group|
#   @articles.each do |article|
#     begin
#       @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups7"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups7 Collection"
# sleep 180
# @groups8.each do |group|
#   @articles.each do |article|
#     begin
#       @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups8"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups8 Collection"
# sleep 180
# @groups9.each do |group|
#   @articles.each do |article|
#     begin
#       @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]}, "#{group}")
#     rescue
#       puts "There was an error while posting to the group #{group} of the collection @groups9"
#       exit
#     end
#   end
# end
# puts "Successfully Posted to the @groups9 Collection"
# puts "Congratulations! Everything has been posted in all the groups"
