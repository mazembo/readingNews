<<<<<<< HEAD
require "mongoid"
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
  field :date_published, :type => String
  field :date_accessed, :type => Date
  field :categories, :type => String
end
puts Articles.count

#The method below returns all the titles of the articles found in the mongodb collection articles
def articles_titles
  @titles = []
  Articles.all.each do |article|
    @titles << article.title
  end
  return @titles
end
# The method below get only the tweet_messages for all articles in the mongodb collection
def tweet_messages
  @tweet_messages = []
  Articles.all.each do |article|
    @tweet_messages << article.tweet_message
  end
  return @tweet_messages
end
# The method below get the titles and the pictures for all articles in the mongodb collection
def titles_pictures
  @titles = []
  Articles.all.each do |article|
    title = []
    title[0] = article.title
    title[1] = article.picture
    @titles << title
  end
  return @titles
end
# The method below gets the tweet_messages and the pictures for all articles in the mongodb collection
def tweets_pictures
  @titles = []
  Articles.all.each do |article|
    title = []
    title[0] = article.tweet_message
    title[1] = article.picture
    @titles << title
  end
  return @titles
end

# mytitles = titles_pictures
# mytitles.each do |title|
#   puts title[0]
#   puts title[1]
# end


# mytitles = articles_titles
# mytitles.each do |title|
#   puts title
# end
# puts mytitles.length
=======
require "mongoid"
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
  field :date_published, :type => String
  field :date_accessed, :type => Date
  field :categories, :type => String
end
puts Articles.count

#The method below returns all the titles of the articles found in the mongodb collection articles
def articles_titles
  @titles = []
  Articles.all.each do |article|
    @titles << article.title
  end
  return @titles
end
# The method below get only the tweet_messages for all articles in the mongodb collection
def tweet_messages
  @tweet_messages = []
  Articles.all.each do |article|
    @tweet_messages << article.tweet_message
  end
  return @tweet_messages
end
# The method below get the titles and the pictures for all articles in the mongodb collection
def titles_pictures
  @titles = []
  Articles.all.each do |article|
    title = []
    title[0] = article.title
    title[1] = article.picture
    @titles << title
  end
  return @titles
end
# The method below gets the tweet_messages and the pictures for all articles in the mongodb collection
def tweets_pictures
  @titles = []
  Articles.all.each do |article|
    title = []
    title[0] = article.tweet_message
    title[1] = article.picture
    @titles << title
  end
  return @titles
end

# mytitles = titles_pictures
# mytitles.each do |title|
#   puts title[0]
#   puts title[1]
# end


# mytitles = articles_titles
# mytitles.each do |title|
#   puts title
# end
# puts mytitles.length
>>>>>>> sinatra stuff and docker scripts
