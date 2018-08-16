require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))

#@groups1 = ["1403814586528158","1419902181603029", "1651431211749292", "150076661761567"]
#@groups2 = ["129291017177108", "438378432950495", "126654487476400", "394952713912519"]
#@groups3 = ["381352271995489", "241805262672345", "430118960425259", "1726773537548951" ]
#@groups4 = ["1530763560470990", "230841617013848", "385190645015189", "1726773537548951" ]
#@groups5 = ["1676075629346572"]

#below are groups for lecongolaisNet
# the first group is not present above. for now just for lecongolais.net

@groups1 = ["323329727829585", "132342043632095", "1676075629346572", "149201935433557" ]
#@groups2 = [ "1530763560470990", "129291017177108", "1651431211749292", "241805262672345"]
#@groups3 = ["1409238022680428", "381352271995489", "1419902181603029", "438378432950495"]
# "919465771505711",
@user_token = access_token["user_token"]
@page_token = access_token["page_token"]
@graph = Koala::Facebook::API.new(@user_token)
@message = "#RDC Mercredi 03/08/2016 Lire notre sélection des tweets du jour(suite)--http://lecongolais.net/?p=1676 Aimez notre page www.facebook.com/lecongolais.net/ --Nous suivre sur Twitter www.twitter.com/LecongolaisNet (@LecongolaisNet)"
Dir.foreach("/home/mavungu/Lecongolais.net/facebook/images/2016-08-03a") do |fname|
  next if fname == '.' or fname == '..'
  @groups1.each do |group|
       @graph.put_picture(fname, {:message => @message}, "#{group}")
  end
end
