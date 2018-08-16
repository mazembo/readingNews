class LegacyProjectBase < ActiveRecord::Base
  establish_connection "legacy_#{Rails.env}"
  self.abstract_class = true  
end
