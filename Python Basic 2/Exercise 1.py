# We just got hired by a gaming company and we're creating this wizard game.
# 
# And this wizard game has the is magician in the user's profile and for now we'll just set it to false.

# We also have is.
# Expert.
# And whether this user is an expert at this game.
# We'll leave it at true for now.
# And then.
# Hmm.
# Let's.
# Let's do this here.
# I want you to check if both or check if.
# Magician.
# And expert.
# And if that's the case, if true, then I want you to print.
# You are a master magician.
# And also, I want you to check.
# If.
# Magician.
# But not expert.
# If that's the case, I want to just print.
# At least you're getting there.
# And then finally, let's do a check that says if you're not a magician.
# I want to say.
# Well, you need magic powers.

is_magician = False
is_expert   = True
# I want you to check if both or check if both Magician And expert.
if is_magician and is_expert:
    print('YOU ARE A MASTER MAGICIAN')
# check if is magician but not expert     
elif is_magician and not is_expert:
    print('you getting there')
# is expert but not a magician
elif not is_magician :
    print('you need magic power')
