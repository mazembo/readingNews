require "active_record"
class LegacyProjectBase < ActiveRecord::Base
  establish_connection :legacy_database
  self.abstract_class = true
   
end
