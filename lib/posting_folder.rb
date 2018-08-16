require 'yaml'
require 'koala'
access_token = YAML.load(File.read('access-data.yml'))

@user_token = access_token['user_token']
@page_token = access_token['page_token']
@message = '#RDC Mardi 09/08/2016 Lire notre sélection des tweets du jour(suite)-- http://lecongolais.net/?p=1761 Envoyez-nous votre tweet composé d’une image expressive et d’un texte clair avec les mentions #lecongolais.net ou @LecongolaisNet et nous les diffuserons très largement pour sensibiliser l’opinion nationale et internationale. Aimez notre page www.facebook.com/lecongolais.net/ --Nous suivre sur Twitter www.twitter.com/LecongolaisNet (@LecongolaisNet)'
@graph = Koala::Facebook::API.new(@user_token)
@graph_page = Koala::Facebook::API.new(@page_token)

#getting filenames from the folder
@filenames = []
Dir.foreach('/home/mavungu/Lecongolais.net/facebook/images/20160809b') do |fname|
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
