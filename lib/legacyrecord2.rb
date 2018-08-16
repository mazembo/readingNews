require "active_record"
require "sqlite3"

class TempProject < ActiveRecord::Base
  establish_connection adapter: "sqlite3", database: ":memory:"
end
