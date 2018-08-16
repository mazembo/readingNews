require "yaml"
require "koala"
access_token = YAML.load(File.read("access-data.yml"))
@articles = YAML.load(File.read("2016-08-04.yml"))
#@groups1 = ["1403814586528158","1419902181603029", "1651431211749292", "150076661761567"]
#@groups2 = ["129291017177108", "438378432950495", "126654487476400", "394952713912519", "1676075629346572"]
#@groups3 = ["381352271995489", "241805262672345", "430118960425259", "1726773537548951" ]
#@groups4 = ["1530763560470990", "230841617013848", "385190645015189", "1726773537548951" ]
#@groups5 = ["275804219283723", "507394756121592", "1601694110080719", "184531028414513", "1173734575975580"]
#@groups6 = ["768847873176770", "1551810621756122", "598150520219330", "251920001492480"]
#@groups7 = ["1608364782756689", "1324206717608472", "441164396039365"]
#@groups8 = ["1644785879098263","1631475210474977"]

#below are groups for lecongolaisNet
# the first group is not present above. for now just for lecongolais.net

#@groups1 = ["323329727829585", "132342043632095", "1676075629346572", "149201935433557" ]
#@groups2 = [ "1530763560470990", "129291017177108", "1651431211749292", "241805262672345"]
#@groups3 = ["1409238022680428", "381352271995489", "1419902181603029", "438378432950495"]

user_token = access_token["user_token"]
page_token = access_token["page_token"]
@graph = Koala::Facebook::API.new(user_token)
@groups1.each do |group|
  @articles.each do |article|
      @graph.put_picture("#{article[1]["picture"]}", {:message => article[1]["short_message"]}, "#{group}")
  end
end
#groups for maz mav:
#@groups1 = ["1403814586528158":"télé 24 dans le monde","1419902181603029":"télé 24 live angleterre", "1651431211749292":"télé 24 live", "150076661761567":"congo ma patrie"]
#@groups2 = ["129291017177108":"RD Congo amour, mboka kitoko", "438378432950495":"télé 24 central", "126654487476400":"réseau congolais anti-balkanisation", "394952713912519":"Ba mpangi ya maitre Puela", "1676075629346572":"2016 yebela po owumela"]
#@groups3 = ["381352271995489":"Les amis de boma", "241805262672345":"john image news", "430118960425259":"alula 2016", "1726773537548951":"Elections 2016 en RDC:parlons-en" ]
#@groups4 = ["1530763560470990":"generation R Kongo", "230841617013848":"Generation Lumbe Lumbe Mwete Mwete", "385190645015189":"Les amis de l'IRDH" ]
#@groups5 = ["275804219283723":"www.congo top N1.com","507394756121592":"tozokendewapi news", "1601694110080719":"les amis de Gi Bakolo states", "184531028414513":"les amis du MPB.TV", "1173734575975580":"solola bien pona Kongo"]
#@groups6 = ["768847873176770":"voix du peuple news", "1551810621756122":"congolais miso polelepolele", "598150520219330":"conseils de resistants congolais", "251920001492480":"gouvernement provincial de kinshasa" ]
#@groups7 = ["1608364782756689":"friends of Africa", "1324206717608472":"point commun", "441164396039365":"qui soigne ses pensées" ]
#@groups8 = ["1644785879098263":"le pouvoir au peuple", "1631475210474977":université UKV, ]
