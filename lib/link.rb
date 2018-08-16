require "yaml"
require "mysql2"
require "active_record"
load "helper.rb"

ActiveRecord::Base.establish_connection(
  :adapter => "mysql2",
  :host => "localhost",
  :username => "root",
  :password => "nditukulu77",
  :database => "newsapp"
  )
class Link < ActiveRecord::Base

end
class Article < ActiveRecord::Base
   
end

# url = "http://www.lecongolais.net"
# page = Nokogiri::HTML(open(url))
# page.to_s.size
# page.css.(selector)
# page.css.selector.name
# page.css.selector.text
