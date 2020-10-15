# praw_data_proj

This repository contains sample for extracting data of subreddits and reddit posts using Reddit PRAW API.  

Prerequisites:

	Reddit Account:	A Reddit account is required to access Reddit’s API. Create one at reddit.com.

	Client ID & Client Secret:These two values are needed to access Reddit’s API as a script application (see Authenticating via OAuth for other application types). They can be created as follow
	
	Go to your app preferences. Click the "Create app" or "Create another app" button. Fill out the form like so:

	name: My Example App
	App type: Choose the script option
	description: You can leave this blank
	about url: You can leave this blank
	redirect url: http://www.example.com/unused/redirect/uri (We won't be using this as a redirect)
	Note: These examples will only work for script type apps, which will ONLY have access to accounts registered as "developers" of the app and require the application to know the user's password. Read more about app types.

	Hit the "create app" button. Make note of the client ID and client secret. For the rest of this page, it will be assumed that:

	Your username is: reddit_bot
	Your password is: snoo
	Your app's client ID is: p-jcoLKBynTLew
	Your app's client secret is: gko_LXELoV07ZBNUXrvWZfzE3aI


Running the scripts:

	Add client ID, Client Secret, User Agent from the newly created app above.
	Add username at username field
	password is passed as parameter and user has to authenticate their reddit credentials to sucessfully run the script
