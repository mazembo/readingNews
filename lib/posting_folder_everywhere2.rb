require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@user_token = access_token["user_token"]
@page_token = access_token["page_token"]
@graph = Koala::Facebook::API.new(@user_token)
@graph_page = Koala::Facebook::API.new(@page_token)
@message = "#RDC Ce Mardi 20/09/2016, le Peuple Congolais continue de manifester à Kinshasa pour réclamer le départ de Kabila, de son gouvernement et de Corneille Naanga(président de la CENI). Ils ont eu 5 ans pour préparer les élections. Ils ne l'ont pas fait. A la place, ils ont préparé un dialogue aux contours flous dont l'objectif ultime est de permettre à Mr Kabila de rester au pouvoir au-délà de la limite constitutionnelle de 2 mandats. La CENI a totalement vendu son indépendance. Elle a multiplié les prétextes pour ne pas convoquer l'électorat le 19 Septembre comme prévu par la loi suprême à laquelle Corneille Naanga et Kabila avaient juré fidélité. Ils ont commis le crime de haute trahison. Ce n'est pas le monologue q'ils orchestrent au camp militaire Tshatshi qui va les disculper. Aujourd'hui le peuple dit: trop, c'est trop. Aucune armée n'est plus puissante qu'un peuple qui se prend en charge et agit à l'unisson. #Alternance #KABILA_DOIT_PARTIR Lire plus-- http://lecongolais.net/?p=2302. Envoyez-nous votre tweet composé d’une image expressive et d’un texte clair avec les mentions #lecongolais.net ou @LecongolaisNet et nous les diffuserons très largement pour sensibiliser l’opinion nationale et internationale. Aimez notre page www.facebook.com/lecongolais.net/ --Nous suivre sur Twitter www.twitter.com/LecongolaisNet (@LecongolaisNet)"

#getting filenames from the folder
@filenames = []
Dir.foreach('/home/mavungu/Lecongolais.net/facebook/images/20160920a') do |fname|
  next if fname == '.' or fname == '..'
  @filenames << fname
end


#Posting to my timeline Maz Mav and my page Lecongolais.net
@filenames.each do |filename|
  begin
  @graph.put_picture(filename, {:message => @message})
  rescue
    puts "There was an error posting to LecongolaisNet"
    exit
  end
end
puts "Successfully posted to Maz Mav and your page Lecongolais.net"

#posting to my groups
#here are groups of lecongolaisNet:
#uncommon groups with maz mav
#@groups1 = ["323329727829585", "132342043632095", "1676075629346572", "149201935433557" ]

#common groups with maz mav
#@groups2 = [ "1530763560470990", "129291017177108", "1651431211749292", "241805262672345"]
#@groups3 = ["1409238022680428", "381352271995489", "1419902181603029", "438378432950495"]

#I initialize the arrays of groups' numbers

@groups1 = ["323329727829585", "132342043632095", "1676075629346572", "149201935433557" ]
@groups2 = [ "1530763560470990", "129291017177108", "1651431211749292"]
@groups3 = ["1409238022680428", "381352271995489", "1419902181603029"]
@groups4 = [ "241805262672345", "438378432950495"]


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
sleep 420
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
sleep 420
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
sleep 420
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
puts "congratulations! You have successfully posted the entire folder to all the groups"
