<<<<<<< HEAD
# short-circuit assignment
def result
  result = nil || 1
  return result
end
put result


# default values - "OR"

# tweets = timeline.tweets || []

# short-circuit evaluation. the second member is not evaluated unless current session is nit
# def sign_in
#   current_session || sign_user_in
# end

# conditional assignement
i_was_set = 1
i_was_set ||= 2
puts i_was_set

i_was_not_set ||= 2
puts i_was_not_set

options = {}
options[:country] ||= "US"
options[:privacy] ||= true
options[:geotag] || = true

# conditional return values
options[:path] = if true
  "/Lecongolais.net/Lecongolais.net"
else
  "/mazembo"

def list_url(user_name, list_name)
  if list_name
    "https://twitter.com/#{user_name}/#{list_name}"
  else
    "https://twitter.com/#{user_name}"
  end
end
#case statement value

client_name = web
client_url = case client_name
when "web"
  "http://twitter.com"
when "Facebook"
  "http://www.facebook.com/twitter"
else
  nil
end
puts client_url

#case -ranges
popularity = case tweet.retweet_count
when 0..9
  nil
when 10..99
  "trending"
else
  "hot"
end

tweet_type = case tweet.status
when /\A@\w+/
  :mention
when /\Ad\s+\w+/
  :direct_message
else
  :public
end

tweet_type = case tweet.status
when /\A@\w+/ then :mention
when /\Ad\s+\w+/ then :direct_message
else                  :public
end

# Not the best
# if ! tweets.empty?
#   puts "Timeline:"
#   puts tweets
# end
unless tweets.empty?
  puts "Timeline: "
  puts tweets
end

# Not the best || unless with else is confusing
# unless tweets.empty?
#   puts "Timeline: "
#   puts tweets
# else
#   puts "No tweets found -better follow some people!"
# end

if tweets.empty
  puts "No tweets found -better follow some people!"
else
  puts "Timeline: "
  puts tweets
end

# Nil is false
# Not best
# if attachment.file_path != nil
#   attachment.post
# end
if attachment.file_path
  attachment.post
end

#In ruby only nil is false

name = ""
quantity = 0
tweets = []

unless name.length
  warn "User name required "
end
# the statement above will never be false

#inline conditionals
#Not the best
if password.length < 8
  fail "Password too short "
end
unless user_name
  fail "No username set "
end

# Rather the below inline statements
fail "Password too short " if password.length < 8
fail "No user same set " unless username

#short circuit "AND"
# not the best...
if user
  if user.signed_in?
  end
end

# Rather this || If user is nil, second half never runs v
if user && user.signed_in?
end

#Methods and Classes
#Optional arguments
#Not optimal
def tweet(message, lat, long)
  #
end
tweet("Practicing Ruby-Fu", nil, nil) #location isn't always used, so let's add defaults

def tweet (message, lat = nil, long = nil )
  #
end
tweet ("Practicing Ruby-Fu") # location is now optional

def tweet(message, lat = nil, long = nil, reply_id = nil)
 #
end
tweet("Practicing Ruby Fu", 28.55, -81.33, 227946) # calls to it are hard to read
tweet("Practicing Ruby Fu", nil, nil, 227946) # have to keep placeholders for arguments you're not using

#Hash arguments
def tweet(message, options = {})
  status = Status.new
  status.lat = options[:lat]
  status.long = options[:long]
  status.body = message
  status.reply_id = options[:reply_id]
  status.post
end
tweet("Practicing Ruby-Fu!",
  :lat => 28.55,
  :long => -81.33
  :reply_id => 227946
)
# keys show meaning || all combined into options argument 
=======
# short-circuit assignment
def result
  result = nil || 1
  return result
end
put result


# default values - "OR"

# tweets = timeline.tweets || []

# short-circuit evaluation. the second member is not evaluated unless current session is nit
# def sign_in
#   current_session || sign_user_in
# end

# conditional assignement
i_was_set = 1
i_was_set ||= 2jj
puts i_was_set

i_was_not_set ||= 2
puts i_was_not_set

options = {}
options[:country] ||= "US"
options[:privacy] ||= true
options[:geotag] || = true

# conditional return values
options[:path] = if true
  "/Lecongolais.net/Lecongolais.net"
else
  "/mazembo"

def list_url(user_name, list_name)
  if list_name
    "https://twitter.com/#{user_name}/#{list_name}"
  else
    "https://twitter.com/#{user_name}"
  end
end
#case statement value

client_name = web
client_url = case client_name
when "web"
  "http://twitter.com"
when "Facebook"
  "http://www.facebook.com/twitter"
else
  nil
end
puts client_url

#case -ranges
popularity = case tweet.retweet_count
when 0..9
  nil
when 10..99
  "trending"
else
  "hot"
end

tweet_type = case tweet.status
when /\A@\w+/
  :mention
when /\Ad\s+\w+/
  :direct_message
else
  :public
end

tweet_type = case tweet.status
when /\A@\w+/ then :mention
when /\Ad\s+\w+/ then :direct_message
else                  :public
end

# Not the best
# if ! tweets.empty?
#   puts "Timeline:"
#   puts tweets
# end
unless tweets.empty?
  puts "Timeline: "
  puts tweets
end

# Not the best || unless with else is confusing
# unless tweets.empty?
#   puts "Timeline: "
#   puts tweets
# else
#   puts "No tweets found -better follow some people!"
# end

if tweets.empty
  puts "No tweets found -better follow some people!"
else
  puts "Timeline: "
  puts tweets
end

# Nil is false
# Not best
# if attachment.file_path != nil
#   attachment.post
# end
if attachment.file_path
  attachment.post
end

#In ruby only nil is false

name = ""
quantity = 0
tweets = []

unless name.length
  warn "User name required "
end
# the statement above will never be false

#inline conditionals
#Not the best
if password.length < 8
  fail "Password too short "
end
unless user_name
  fail "No username set "
end

# Rather the below inline statements
fail "Password too short " if password.length < 8
fail "No user same set " unless username

#short circuit "AND"
# not the best...
if user
  if user.signed_in?
  end
end

# Rather this || If user is nil, second half never runs v
if user && user.signed_in?
end

#Methods and Classes
#Optional arguments
#Not optimal
def tweet(message, lat, long)
  #
end
tweet("Practicing Ruby-Fu", nil, nil) #location isn't always used, so let's add defaults

def tweet (message, lat = nil, long = nil )
  #
end
tweet ("Practicing Ruby-Fu") # location is now optional

def tweet(message, lat = nil, long = nil, reply_id = nil)
 #
end
tweet("Practicing Ruby Fu", 28.55, -81.33, 227946) # calls to it are hard to read
tweet("Practicing Ruby Fu", nil, nil, 227946) # have to keep placeholders for arguments you're not using

#Hash arguments
def tweet(message, options = {})
  status = Status.new
  status.lat = options[:lat]
  status.long = options[:long]
  status.body = message
  status.reply_id = options[:reply_id]
  status.post
end
tweet("Practicing Ruby-Fu!",
  :lat => 28.55,
  :long => -81.33
  :reply_id => 227946
)
# keys show meaning || all combined into options argument
>>>>>>> sinatra stuff and docker scripts
