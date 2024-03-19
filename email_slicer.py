#The Email slicer using python:

#Step-1 get the email ID from the user
email=input("Enter Your Email Address:").strip()

#Step-2 Slice out the username and domain
username=email[:email.index('@')]
domain_name=email[email.index('@')+1:]

#Now, let's see the results
print(f"Hello, Your username is'{username}'and your domain name is'{domain_name}'")
