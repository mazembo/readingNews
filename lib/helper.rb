require "date"
def convert_to_date(date_published)
  my_date = DateTime.strptime(date_published, "%Y-%m-%d")
end
