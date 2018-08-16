<<<<<<< HEAD
# This script takes a directory of yamlfiles and read the content and insert it into mongodb
require "yaml"
require "mongoid"

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
  field :date_published, :type => String
  field :date_accessed, :type => Date
  field :categories, :type => String
end

# I provide a directory and the output is a list of files from that directory
@directory = "C:/Lecongolais.net/ymlfiles"
@filenames = []
Dir.foreach(@directory) do |fname|
  next if fname == '.' or fname == '..'
  absolute_file = @directory + "/" + fname
  @filenames << absolute_file
end

# I then proceed with processing one file at a time
# A yaml file produces first a dictionnary, later a list of individual news articles
# The list of articles is iterated and a news item is inserted in the DB at a time
@filenames.each do |filename|
    begin
      @articles = YAML.load(File.read(filename))
      @articles_list = @articles.values
      @articles_list.each do |article|
        Articles.create!(article)
      end
    rescue
     puts "there was an error either in reading file or inserting in DB"
    end
end
puts "we have successfully saved the articles into the mongoDB "
=======
# This script takes a directory of yamlfiles and read the content and insert it into mongodb
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

# I provide a directory and the output is a list of files from that directory
@directory = "C:/Lecongolais.net/ymlfiles"
@filenames = []
Dir.foreach(@directory) do |fname|
  next if fname == '.' or fname == '..'
  absolute_file = @directory + "/" + fname
  @filenames << absolute_file
end

# I then proceed with processing one file at a time
# A yaml file produces first a dictionnary, later a list of individual news articles
# The list of articles is iterated and a news item is inserted in the DB at a time
@filenames.each do |filename|
    begin
      @articles = YAML.load(File.read(filename))
      @articles_list = @articles.values
      @articles_list.each do |article|
        article["date_published"] = convert_to_date(article["date_published"])
        Articles.create!(article)
      end
    rescue
     puts "there was an error either in reading file or inserting in DB"
    end
end
puts "we have successfully saved the articles into the mongoDB "
>>>>>>> sinatra stuff and docker scripts
