require 'sinatra'
require 'sinatra/json'
require 'sinatra/activerecord'

set :database_file, 'database.yml'

class Resource < ActiveRecord::Base
  validates :name, presence: true, uniqueness: true
end

get '/' do
  json Resource.select('id', 'name').all
end
get '/:id' do
  resource =  Resource.find_by_id(params[:id])

  if resource
    halt 206
    json resource
  else
    halt 404
  end
end
post '/' do
  resource = Resource.create(params)

  if resource
    json resource
  else
    halt 500
  end
end
patch '/:id' do
  resource = Resource.find_by_id(params[:id])

  if resource
    resource.update(params)
  else
    halt 404
  end
end
delete '/:id' do
  resource = Resource.find_by_id(params[:id])

  if resource
    resource.destroy
  else
    halt 404
  end
end
