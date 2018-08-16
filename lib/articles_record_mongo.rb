require "yaml"
require "mongoid"
load "helper.rb"

# A class to map articles fields in the yaml file with fields of documents in the mongodb
class Articles
  include Mongoid::Document

  Mongoid.load!("mongoid.yml", :development)

  field :title, :type => String
  field :picture, :type => String
  field :original_url, :type => String
  field :lecongolais_url, :type => String
  field :message, :type => String
  field :short_message, :type => String
  field :tweet_message, :type => String
  field :date_published, :type => Date
  field :date_accessed, :type => Date
  field :categories, :type => String
end
