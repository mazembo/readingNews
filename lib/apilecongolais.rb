require "sinatra"
require "mongoid"

class Articles
  include Mongoid::Document

  Mongoid.load!("mongoid.yml")

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


get "/" do
  articles = Articles.all
  articles.to_json
end
