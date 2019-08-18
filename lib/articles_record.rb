gem "mysql2", :version=>'=0.4.10'
require "mysql2"
require "active_record"
ActiveRecord::Base.establish_connection(
  :adapter => "mysql2",
  :host => "localhost",
  :username => "root",
  :password => "nd****9",
  :database => "newsapp"
  )
class Article < ActiveRecord::Base
  scope :created_between, lambda {|start_date, end_date| where("date_published >= ? AND date_published <= ?", start_date, end_date )}

end
